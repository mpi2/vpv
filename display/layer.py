from PyQt5 import QtCore, Qt
from lookup_tables import Lut
import numpy as np
import pyqtgraph as pg
from common import Orientation


class Layer(Qt.QObject):

    volume_label_signal = QtCore.pyqtSignal(str)

    def __init__(self, parent, layer_type, model):
        """
        The base class that controls the display of of one layer of data. Is extended to display heatmap data and vector
        data. The main function is to get data into a pytgraph.ImageItem object which is then

        Attributes
        ----------
        model: model.model
            contains all the data
        parent: display.SliceWidget
            the parent view widget
        image_item: pyqtgrapgh.ImageItem
            The image to be displayed is put in here

        """
        super(Layer, self).__init__()
        # If it's a data volume, dont add slider, add number box to filter q-values
        self.model = model
        self.parent = parent
        self.image_items = []
        self.image_item = None  # Set in the subclasses
        self.vol = None  # When setting to "None" in the view manager we get problems. Needs rewriting
        self.layer_type = layer_type # this should be unique
        self.lt = Lut()

    def clear(self):
        slice_ = np.copy(self.image_item.image)
        slice_[:] = 0
        self.image_item.setImage(slice_)

    def update(self, auto_levels=False):
        """
        Sets the orientation and centres the image at the mid-slice
        :param orientation:
        :param auto_levels:
        :return:
        """
        if self.vol and self.vol != 'None':
            self.image_item.setLevels(self.vol.levels, update=False)
            self.image_item.setLookupTable(self.lut[0])
            self.reload()

    def reload(self):
        """
        reload the current image. For example when the orientation has changed
        """
        self.set_slice(self.parent.current_slice_idx)
        # self.image_item.setImage()

    def set_volume(self, volname, initial=False):
        """
        :param vol, Volume object from model.py
        """

        if volname == "None":
            self.volume_label_signal.emit("None")
            self.clear()  # This clears the image
            self.vol = None
            return
        self.volume_label_signal.emit(volname)

        self.vol = self.model.getvol(volname)

        self.set_series_slider()

        orientation = self.parent.orientation
        self.name = self.vol.name
        self.image_item.setZValue(self.layer_type.value)

        dim_len = self.vol.dimension_length(orientation)

        # Try setting the new volume to the slice index of the current volume. If out of bounds, set to midslice
        if self.parent.current_slice_idx + 1 > dim_len or initial:
            slice_indx = dim_len / 2
        else:
            slice_indx = self.parent.current_slice_idx
        # slice_ = self.vol.get_data(orientation, int(slice_indx))  # DELETE
        self.parent.set_slice_slider(dim_len, slice_indx)

        # This fixes problem with linked zooming
        self.parent.viewbox.autoRange()
        self.parent.scalebar.updateBar()

    def set_slice(self, index):
         if self.vol:
            self.image_item.setImage(self.vol.get_data(self.parent.orientation, index - 1,
                                                       self.parent.flipped_x, self.parent.flipped_z, self.parent.flipped_y),
                                     autoLevels=False)

    def set_series_slider(self):
        if self.vol.data_type == 'series':
            num_vols_in_series = len(self.vol.images)
            self.parent.ui.seriesSlider.setRange(0, num_vols_in_series - 1)
            self.parent.ui.seriesSlider.valueChanged.connect(self.series_slider_changed)
            self.parent.ui.seriesSlider.show()
            self.parent.ui.labelImageSeriesNumber.show()
        else:
            self.parent.ui.seriesSlider.hide()
            self.parent.ui.labelImageSeriesNumber.hide()

    def series_slider_changed(self, idx):
        self.vol.set_image(idx)
        self.parent.ui.labelImageSeriesNumber.setText(str(idx))
        self.reload()
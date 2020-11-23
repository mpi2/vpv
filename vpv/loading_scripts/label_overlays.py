"""
A work in progress.

Given a root directory, load image, inverted labels and set opacity etc.
Set window title.

Make it configurable
"""

from pathlib import Path
import sys
from itertools import chain
from PyQt5 import QtGui
from vpv.vpv_temp import Vpv
from vpv.common import Layers, Orientation
from lama.common import get_file_paths
from lama.elastix import RESOLUTION_IMGS_DIR, IMG_PYRAMID_DIR



ORIS = ['sagittal', 'coronal', 'axial']
VOL_CMAP = 'grey'
LAB_CMAP = 'anatomy_labels'

# root_dir = Path('/mnt/bit_nfs/neil/impc_e15_5/phenotyping_tests/TCP_E15_5_test_060720/output/baseline/output/baseline/1677880_download/try_configs/reg/new')
# outdir = Path('/mnt/bit_nfs/neil/impc_e15_5/phenotyping_tests/TCP_E15_5_test_060720/output/baseline/output/baseline/1677880_download/try_configs/reg/vpvloaders')
IGNORE = [RESOLUTION_IMGS_DIR, IMG_PYRAMID_DIR]

OPACITY = 0.4

def load(line_dir):
    app = QtGui.QApplication([])
    ex = Vpv()

    vol_dir = next(line_dir.rglob('*/reg*/*rigid*'))
    lab_dir = next(line_dir.rglob('inverted_labels/similarity'))

    vol = get_file_paths(vol_dir, ignore_folders=IGNORE)[0]
    lab = get_file_paths(lab_dir, ignore_folders=IGNORE)[0]

    ex.load_volumes([vol, lab], 'vol')

    # Vpv deals with images with the same name by appending parenthetical digits. We need to know the ids it will assign
    # if we are to get a handle once loaded
    img_ids = ex.img_ids()

    num_top_views = 3

    # Set the top row of views
    for i in range(num_top_views):

        vol_id = img_ids[0]
        # label_id = top_labels[i].stem
        label_id = img_ids[1]
        # if label_id == vol_id:
        #     label_id = f'{label_id}(1)'
        ex.views[i].layers[Layers.vol1].set_volume(vol_id)
        ex.views[i].layers[Layers.vol2].set_volume(label_id)


    ex.mainwindow.setWindowTitle(line_dir.name)
    print('Finished loading')

    # Show two rows
    ex.data_manager.show2Rows(False)

    # Set orientation
    # ex.data_manager.on_orientation('sagittal')

    # Set colormap
    ex.data_manager.on_vol2_lut_changed('anatomy_labels')

    # opacity
    ex.data_manager.modify_layer(Layers.vol2, 'set_opacity', OPACITY)

    sys.exit(app.exec_())


if __name__ == '__main__':
    load(Path(sys.argv[1]))

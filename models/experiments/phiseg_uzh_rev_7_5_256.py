import torch
import torch.nn as nn
from models.phiseg import PHISeg
from data.uzh_prostate_data import uzh_prostate_data
from utils import normalise_image
experiment_name = 'PHISegUZHRev_7_5_256'
log_dir_name = 'uzh'
data_loader = uzh_prostate_data


# number of filter for the latent levels, they will be applied in the order as loaded into the list
filter_channels = [32, 64, 128, 192, 192, 192, 192]
latent_levels = 5

iterations = 5000000

n_classes = 3
num_labels_per_subject = 6

no_convs_fcomb = 4 # not used
beta = 10.0 # not used
#
use_reversible = True
exponential_weighting = True

# use 1 for grayscale, 3 for RGB images
input_channels = 1
epochs_to_train = 20
batch_size = 12
image_size = (1, 256, 256)
resize_to = [256, 256]
target_resolution = (0.46875, 0.46875) # calculated s.t. 192/200 of pixels is kept, i.e. 4 percent of pixels are cropped

augmentation_options = {'do_flip_lr': True,
                        'do_flip_ud': True,
                        'do_rotations': True,
                        'do_scaleaug': True,
                        'nlabels': n_classes}

input_normalisation = normalise_image

validation_samples = 16
num_validation_images = 'all'

logging_frequency = 1000
validation_frequency = 1000

weight_decay = 10e-5

pretrained_model = None
# model
model = PHISeg

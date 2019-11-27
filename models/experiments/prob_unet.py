import torch
import torch.nn as nn
from models.probabilistic_unet import ProbabilisticUnet
from utils import normalise_image

experiment_name = 'ProbabilisticUnet'
log_dir_name = 'lidc'

# number of filter for the latent levels, they will be applied in the order as loaded into the list
filter_channels = [32, 64, 128, 192]
latent_levels = 2 # TODO: this is passed to latent dim and latent levels, should not be like that
n_classes = 2
no_convs_fcomb = 4
beta = 10.0 # for loss function
#
use_reversible = False

# use 1 for grayscale, 3 for RGB images
input_channels = 1

epochs_to_train = 20
batch_size = [12, 1, 1]

validation_samples = 16

logging_frequency = 10
validation_frequency = 100

input_normalisation = normalise_image

# model
model = ProbabilisticUnet

import os
from PIL import Image

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
path = 'crop_images_'
lr = 1e-02

seed = 0
epochs = 10

batchSize = {
	'train': 50,
	'test': 10
}

numWorkers = {
	'train': 0,
	'test': 0
}

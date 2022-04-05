# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Utilies for image preprocessing and augmentation.

Deprecated: `tf.keras.preprocessing.image` APIs do not operate on tensors and
are not recommended for new code. Prefer loading data with
`tf.keras.utils.image_dataset_from_directory`, and then transforming the output
`tf.data.Dataset` with preprocessing layers. For more information, see the
tutorials for [loading images](
https://www.tensorflow.org/tutorials/load_data/images) and [augmenting images](
https://www.tensorflow.org/tutorials/images/data_augmentation), as well as the
[preprocessing layer guide](
https://www.tensorflow.org/guide/keras/preprocessing_layers).

"""

import sys as _sys

from keras.preprocessing.image import DirectoryIterator
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import Iterator
from keras.preprocessing.image import NumpyArrayIterator
from keras.preprocessing.image import apply_affine_transform
from keras.preprocessing.image import apply_brightness_shift
from keras.preprocessing.image import apply_channel_shift
from keras.preprocessing.image import random_brightness
from keras.preprocessing.image import random_channel_shift
from keras.preprocessing.image import random_rotation
from keras.preprocessing.image import random_shear
from keras.preprocessing.image import random_shift
from keras.preprocessing.image import random_zoom
from keras.utils.image_utils import array_to_img
from keras.utils.image_utils import img_to_array
from keras.utils.image_utils import load_img
from keras.utils.image_utils import save_img
from keras.utils.image_utils import smart_resize
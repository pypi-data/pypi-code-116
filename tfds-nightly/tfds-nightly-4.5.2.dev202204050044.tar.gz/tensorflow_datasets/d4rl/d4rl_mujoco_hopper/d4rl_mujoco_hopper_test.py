# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""D4Rl Hopper dataset from Mujoco."""

from tensorflow_datasets.d4rl.d4rl_mujoco_hopper import d4rl_mujoco_hopper
import tensorflow_datasets.public_api as tfds


class D4rlMujocoHopperTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for hopper datasets."""
  DATASET_CLASS = d4rl_mujoco_hopper.D4rlMujocoHopper
  SPLITS = {
      'train': 2,  # Number of fake train example
  }
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'hopper_medium.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'hopper_medium.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['v0-medium']


class D4rlMujocoHopperInfosTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for hopper datasets with step metadata."""
  DATASET_CLASS = d4rl_mujoco_hopper.D4rlMujocoHopper
  SPLITS = {
      'train': 2,  # Number of fake train example
  }
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'hopper_random-v1.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'hopper_random-v1.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['v1-random']


class D4rlMujocoHopperReplayTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for hopper datasets with replay.

  These datasets have the following special features:
    * Contain step metadata.
    * Contain two fields of episode metadata.
    * Use float64 types (instead of float32)
    * Rewards are stored with shape (1,) instead of scalar

  """
  DATASET_CLASS = d4rl_mujoco_hopper.D4rlMujocoHopper
  SPLITS = {
      'train': 2,  # Number of fake train example
  }
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'hopper_medium_replay-v1.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'hopper_medium_replay-v1.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['v1-medium-replay']


class D4rlMujocoHopperMetadataTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for hopper datasets with all the metadata fields."""
  DATASET_CLASS = d4rl_mujoco_hopper.D4rlMujocoHopper
  SPLITS = {
      'train': 2,  # Number of fake train example
  }
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'hopper_medium-v2.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'hopper_medium-v2.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['v2-medium']


if __name__ == '__main__':
  tfds.testing.test_main()

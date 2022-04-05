'''
Copyright 2022 fvl

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
import os

import torch

from PyDeepfake.datasets.dataset import DeepFakeDataset
from PyDeepfake.utils.registries import DATASET_REGISTRY

from .utils import get_image_from_path

'''
DATASET:
  DATASET_NAME: CelebDF
  ROOT_DIR: /share_io02_ssd/ouyang/celeb-df-v1
  TRAIN_INFO_TXT: '/share_io02_ssd/ouyang/celeb-df-v1/splits/train.txt'
  VAL_INFO_TXT: '/share_io02_ssd/ouyang/celeb-df-v1/splits/eval.txt'
  TEST_INFO_TXT: '/share_io02_ssd/ouyang/celeb-df-v1/splits/eval.txt'
  IMG_SIZE: 380
  SCALE_RATE: 1.0
'''
'''
DATASET:
  DATASET_NAME: CelebDF
  ROOT_DIR: /share_io02_ssd/ouyang/celeb-df-v2
  TRAIN_INFO_TXT: '/share_io02_ssd/ouyang/celeb-df-v2/splits/train.txt'
  VAL_INFO_TXT: '/share_io02_ssd/ouyang/celeb-df-v2/splits/eval.txt'
  TEST_INFO_TXT: '/share_io02_ssd/ouyang/celeb-df-v2/splits/eval.txt'
  IMG_SIZE: 380
  SCALE_RATE: 1.0
'''


@DATASET_REGISTRY.register()
class CelebDF(DeepFakeDataset):
    def __getitem__(self, idx):
        info_line = self.info_list[idx]
        image_info = info_line.strip('\n').split()
        image_path = image_info[0]
        image_abs_path = os.path.join(self.root_dir, image_path)

        img, _ = get_image_from_path(
            image_abs_path, None, self.mode, self.dataset_cfg
        )
        img_label_binary = int(image_info[1])

        sample = {
            'img': img,
            'bin_label': [int(img_label_binary)],
        }

        sample['img'] = torch.FloatTensor(sample['img'])
        sample['bin_label'] = torch.FloatTensor(sample['bin_label'])
        sample['bin_label_onehot'] = self.label_to_one_hot(
            sample['bin_label'], 2
        ).squeeze()
        return sample

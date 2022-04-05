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
from PyDeepfake.datasets.utils import (
    get_image_from_path,
    get_mask_path_from_img_path,
)
from PyDeepfake.utils.registries import DATASET_REGISTRY

'''
DATASET:
  DATASET_NAME: ForgeryNet
  ROOT_DIR: /share/test/ouyang/ForgeryNet
  # TRAIN_INFO_TXT: '/share/home/zhangchao/works/temp_train.txt'
  # VAL_INFO_TXT: '/share/home/zhangchao/works/temp_val.txt'
  # TEST_INFO_TXT: '/share/home/zhangchao/works/temp_test.txt'
  IMG_SIZE: 380
  SCALE_RATE: 1.0
  ROTATE_ANGLE: 10
  CUTOUT_H: 10
  CUTOUT_W: 10
  COMPRESSION_LOW: 65
  COMPRESSION_HIGH: 80
'''


@DATASET_REGISTRY.register()
class ForgeryNet(DeepFakeDataset):
    def __init__(self, dataset_cfg, mode='train'):
        self.dataset_name = dataset_cfg['DATASET_NAME']
        self.mode = mode
        self.dataset_cfg = dataset_cfg
        info_txt_tag = mode.upper() + '_INFO_TXT'
        if mode == 'train':
            self.root_dir = os.path.join(dataset_cfg['ROOT_DIR'], 'Training')
            if dataset_cfg[info_txt_tag] != '':
                self.info_txt = dataset_cfg[info_txt_tag]
            else:
                self.info_txt = os.path.join(
                    self.root_dir, 'image_list_train_retina2.txt'
                )
        else:
            self.root_dir = os.path.join(dataset_cfg['ROOT_DIR'], 'Validation')
            if dataset_cfg[info_txt_tag] != '':
                self.info_txt = dataset_cfg[info_txt_tag]
            else:
                self.info_txt = os.path.join(self.root_dir, 'image_list.txt')

        info_list = open(self.info_txt).readlines()
        self.info_list = info_list

    def __getitem__(self, idx):
        info_line = self.info_list[idx]
        image_info = info_line.strip('\n').split()
        image_path = image_info[0]
        image_abs_path = os.path.join(self.root_dir, 'image2', image_path)
        mask_abs_path = get_mask_path_from_img_path(
            self.dataset_name, self.root_dir, image_path
        )
        img, mask = get_image_from_path(
            image_abs_path, mask_abs_path, self.mode, self.dataset_cfg
        )
        img_label_binary = int(image_info[1])
        img_label_triple = int(image_info[2])
        img_label_mul = int(image_info[3])

        sample = {
            'img': img,
            'bin_label': [int(img_label_binary)],
            'tri_label': [int(img_label_triple)],
            'mul_label': [int(img_label_mul)],
        }

        sample['img'] = torch.FloatTensor(sample['img'])
        sample['bin_label'] = torch.FloatTensor(sample['bin_label'])
        sample['bin_label_onehot'] = self.label_to_one_hot(
            sample['bin_label'], 2
        ).squeeze()
        sample['tri_label'] = torch.FloatTensor(sample['tri_label'])
        sample['mul_label'] = torch.FloatTensor(sample['mul_label'])
        sample['mask'] = torch.FloatTensor(mask)

        return sample

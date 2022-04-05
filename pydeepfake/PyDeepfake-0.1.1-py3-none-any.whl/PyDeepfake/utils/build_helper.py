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
import torch
from torch.utils.data import DataLoader

import PyDeepfake.datasets
import PyDeepfake.models
import PyDeepfake.utils.distributed as du
import PyDeepfake.utils.logging as logging
from PyDeepfake.utils.registries import (
    DATASET_REGISTRY,
    LOSS_REGISTRY,
    MODEL_REGISTRY,
)

logger = logging.get_logger(__name__)


def build_model(cfg, gpu_id=None):
    # Construct the model
    model_cfg = cfg['MODEL']
    name = model_cfg['MODEL_NAME']
    logger.info('MODEL_NAME: ' + name)
    model = MODEL_REGISTRY.get(name)(model_cfg)

    assert torch.cuda.is_available(), "Cuda is not available."
    assert (
        cfg['NUM_GPUS'] <= torch.cuda.device_count()
    ), "Cannot use more GPU devices than available"

    if gpu_id is None:
        # Determine the GPU used by the current process
        cur_device = torch.cuda.current_device()
    else:
        cur_device = gpu_id
    # Transfer the model to the current GPU device
    model = model.cuda(device=cur_device)
    # Use multi-process data parallel model in the multi-gpu setting
    if cfg['NUM_GPUS'] > 1:
        # Make model replica operate on the current device
        model = torch.nn.parallel.DistributedDataParallel(
            module=model, device_ids=[cur_device], output_device=cur_device
        )

    return model


def build_loss_fun(cfg):
    loss_cfg = cfg['LOSS']
    name = loss_cfg['LOSS_FUN']
    logger.info('LOSS_FUN: ' + name)
    loss_fun = LOSS_REGISTRY.get(name)(loss_cfg)
    return loss_fun


def build_dataset(mode, cfg):
    dataset_cfg = cfg['DATASET']
    name = dataset_cfg['DATASET_NAME']
    logger.info('DATASET_NAME: ' + name + '  ' + mode)
    return DATASET_REGISTRY.get(name)(dataset_cfg, mode)


def build_dataloader(dataset, mode, cfg):
    dataloader_cfg = cfg['DATALOADER']
    num_tasks = du.get_world_size()
    global_rank = du.get_rank()

    sampler = torch.utils.data.DistributedSampler(
        dataset,
        num_replicas=num_tasks,
        rank=global_rank,
        shuffle=True if mode == 'train' else False,
    )

    return DataLoader(
        dataset,
        batch_size=dataloader_cfg['BATCH_SIZE'],
        sampler=sampler,
        num_workers=dataloader_cfg['NUM_WORKERS'],
        pin_memory=dataloader_cfg['PIN_MEM'],
        drop_last=True if mode == 'train' else False,
    )

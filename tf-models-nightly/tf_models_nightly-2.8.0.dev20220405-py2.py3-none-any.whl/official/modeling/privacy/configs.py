# Copyright 2022 The TensorFlow Authors. All Rights Reserved.
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

"""Configs for differential privacy."""
import dataclasses

from official.modeling.hyperparams import base_config


@dataclasses.dataclass
class DifferentialPrivacyConfig(base_config.Config):
  # Applied to the gradients
  # Setting to a large number so nothing is clipped.
  clipping_norm: float = 100000000.0  # 10^9
  noise_multiplier: float = 0.0

# ***************************************************************
# Copyright (c) 2021 Jittor. All Rights Reserved. 
# Maintainers: 
#     Wenyang Zhou <576825820@qq.com>
#     Dun Liang <randonlang@gmail.com>. 
# 
# This file is subject to the terms and conditions defined in
# file 'LICENSE.txt', which is part of this source code package.
# ***************************************************************
# This model is generated by pytorch converter.
import jittor as jt
import jittor.nn as nn

__all__ = ['AlexNet', 'alexnet']

class AlexNet(nn.Module):
    """ AlexNet model architecture.

    Args:

    * num_classes: Number of classes. Default: 1000.

    Example::
    
        model = jittor.models.AlexNet(500)
        x = jittor.random([10,3,224,224])
        y = model(x) # [10, 500]

    """

    def __init__(self, num_classes=1000):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv(3, 64, kernel_size=11, stride=4, padding=2),
            nn.Relu(), 
            nn.Pool(kernel_size=3, stride=2, op='maximum'), 
            nn.Conv(64, 192, kernel_size=5, padding=2), 
            nn.Relu(), nn.Pool(kernel_size=3, stride=2, op='maximum'), 
            nn.Conv(192, 384, kernel_size=3, padding=1), 
            nn.Relu(), 
            nn.Conv(384, 256, kernel_size=3, padding=1), 
            nn.Relu(), 
            nn.Conv(256, 256, kernel_size=3, padding=1), 
            nn.Relu(), 
            nn.Pool(kernel_size=3, stride=2, op='maximum')
        )
        self.avgpool = nn.AdaptiveAvgPool2d((6, 6))
        self.classifier = nn.Sequential(
            nn.Dropout(), 
            nn.Linear(((256 * 6) * 6), 4096), 
            nn.Relu(), 
            nn.Dropout(), 
            nn.Linear(4096, 4096), 
            nn.Relu(), 
            nn.Linear(4096, num_classes)
        )

    def execute(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = jt.reshape(x, (x.shape[0], (- 1)))
        x = self.classifier(x)
        return x

def alexnet(pretrained=False, **kwargs):
    model = AlexNet(**kwargs)
    if pretrained: model.load("jittorhub://alexnet.pkl")
    return model

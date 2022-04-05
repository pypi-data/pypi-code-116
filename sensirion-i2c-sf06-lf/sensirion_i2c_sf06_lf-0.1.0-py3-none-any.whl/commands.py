#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2022 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:    sensirion-driver-generator 0.9.0
# Product:      sf06_lf
# Version:      1.0
#

from enum import Enum
from sensirion_i2c_adapter.transfer import Transfer, TxData, RxData
from sensirion_driver_support_types.bitfield import BitField, BitfieldContainer


class InvFlowScaleFactors(Enum):
    SLF3C_1300F = 500
    SLF3S_1300F = 500
    SLF3S_4000B = 32
    SLF3S_0600F = 10
    LD20_0600L = 1200
    LD20_2600B = 20

    def __int__(self):
        return self.value


class SignalingFlagsT(BitfieldContainer):
    air_in_line_flag = BitField(offset=0, width=1)
    high_flow_flag = BitField(offset=1, width=1)
    exp_smoothing_active = BitField(offset=5, width=1)


class StartH2oContinuousMeasurement(Transfer):
    CMD_ID = 0x3608

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.012, slave_address=None, ignore_ack=False)


class StartIpaContinuousMeasurement(Transfer):
    CMD_ID = 0x3615

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.012, slave_address=None, ignore_ack=False)


class ReadMeasurementDataRaw(Transfer):

    def pack(self):
        return None

    rx = RxData('>hhH')


class StopContinuousMeasurement(Transfer):
    CMD_ID = 0x3ff9

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.001, slave_address=None, ignore_ack=False)


class StartSingleThermalConductivityMeasurementSync(Transfer):
    CMD_ID = 0x3646

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=2.3, slave_address=None, ignore_ack=False)


class StartSingleThermalConductivityMeasurementAsync(Transfer):
    CMD_ID = 0x3646

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H')


class ReadThermalConductivityMeasurementData(Transfer):

    def pack(self):
        return None

    rx = RxData('>hhh')


class EnterSleep(Transfer):
    CMD_ID = 0x3677

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.0, slave_address=None, ignore_ack=True)


class ExitSleep(Transfer):
    CMD_ID = 0x0

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B', device_busy_delay=0.025, slave_address=None, ignore_ack=True)


class ReadProductIdentifierPrepare(Transfer):
    CMD_ID = 0x367c

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H')


class ReadProductIdentifier(Transfer):
    CMD_ID = 0xe102

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H')
    rx = RxData('>I8s')

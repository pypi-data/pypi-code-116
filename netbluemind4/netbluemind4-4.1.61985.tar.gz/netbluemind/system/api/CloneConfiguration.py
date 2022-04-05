#
#  BEGIN LICENSE
#  Copyright (c) Blue Mind SAS, 2012-2016
# 
#  This file is part of BlueMind. BlueMind is a messaging and collaborative
#  solution.
# 
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of either the GNU Affero General Public License as
#  published by the Free Software Foundation (version 3 of the License).
# 
# 
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# 
#  See LICENSE.txt
#  END LICENSE
#
import requests
from netbluemind.python import serder

class CloneConfiguration :
    def __init__( self):
        self.sourceInstallationId = None
        self.uidToIpMapping = None
        self.sysconfOverride = None
        self.mode = None
        pass

class __CloneConfigurationSerDer__:
    def __init__( self ):
        pass

    def parse(self, value):
        if(value == None):
            return None
        instance = CloneConfiguration()

        self.parseInternal(value, instance)
        return instance

    def parseInternal(self, value, instance):
        sourceInstallationIdValue = value['sourceInstallationId']
        instance.sourceInstallationId = serder.STRING.parse(sourceInstallationIdValue)
        uidToIpMappingValue = value['uidToIpMapping']
        instance.uidToIpMapping = serder.MapSerDer(serder.STRING).parse(uidToIpMappingValue)
        sysconfOverrideValue = value['sysconfOverride']
        instance.sysconfOverride = serder.MapSerDer(serder.STRING).parse(sysconfOverrideValue)
        from netbluemind.system.api.CloneConfigurationMode import CloneConfigurationMode
        from netbluemind.system.api.CloneConfigurationMode import __CloneConfigurationModeSerDer__
        modeValue = value['mode']
        instance.mode = __CloneConfigurationModeSerDer__().parse(modeValue)
        return instance

    def encode(self, value):
        if(value == None):
            return None
        instance = dict()
        self.encodeInternal(value,instance)
        return instance

    def encodeInternal(self, value, instance):

        sourceInstallationIdValue = value.sourceInstallationId
        instance["sourceInstallationId"] = serder.STRING.encode(sourceInstallationIdValue)
        uidToIpMappingValue = value.uidToIpMapping
        instance["uidToIpMapping"] = serder.MapSerDer(serder.STRING).encode(uidToIpMappingValue)
        sysconfOverrideValue = value.sysconfOverride
        instance["sysconfOverride"] = serder.MapSerDer(serder.STRING).encode(sysconfOverrideValue)
        from netbluemind.system.api.CloneConfigurationMode import CloneConfigurationMode
        from netbluemind.system.api.CloneConfigurationMode import __CloneConfigurationModeSerDer__
        modeValue = value.mode
        instance["mode"] = __CloneConfigurationModeSerDer__().encode(modeValue)
        return instance


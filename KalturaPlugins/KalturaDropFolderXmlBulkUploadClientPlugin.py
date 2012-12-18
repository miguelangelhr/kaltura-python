import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaDropFolderClientPlugin import *
from KalturaClientBase import *

########## enums ##########
########## classes ##########
class KalturaDropFolderXmlBulkUploadFileHandlerConfig(KalturaDropFolderFileHandlerConfig):
    def __init__(self,
            handlerType=NotImplemented):
        KalturaDropFolderFileHandlerConfig.__init__(self,
            handlerType)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDropFolderFileHandlerConfig.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDropFolderXmlBulkUploadFileHandlerConfig.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolderFileHandlerConfig.toParams(self)
        kparams.put("objectType", "KalturaDropFolderXmlBulkUploadFileHandlerConfig")
        return kparams


########## services ##########
########## main ##########
class KalturaDropFolderXmlBulkUploadClientPlugin(KalturaClientPlugin):
    # KalturaDropFolderXmlBulkUploadClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaDropFolderXmlBulkUploadClientPlugin
    @staticmethod
    def get(client):
        if KalturaDropFolderXmlBulkUploadClientPlugin.instance == None:
            KalturaDropFolderXmlBulkUploadClientPlugin.instance = KalturaDropFolderXmlBulkUploadClientPlugin(client)
        return KalturaDropFolderXmlBulkUploadClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaDropFolderXmlBulkUploadFileHandlerConfig': KalturaDropFolderXmlBulkUploadFileHandlerConfig,
        }

    # @return string
    def getName(self):
        return 'dropFolderXmlBulkUpload'


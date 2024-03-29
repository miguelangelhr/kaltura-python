import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
class KalturaFileSyncOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    READY_AT_ASC = "+readyAt"
    READY_AT_DESC = "-readyAt"
    SYNC_TIME_ASC = "+syncTime"
    SYNC_TIME_DESC = "-syncTime"
    FILE_SIZE_ASC = "+fileSize"
    FILE_SIZE_DESC = "-fileSize"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaFileSyncStatus:
    ERROR = -1
    PENDING = 1
    READY = 2
    DELETED = 3
    PURGED = 4

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaFileSyncType:
    FILE = 1
    LINK = 2
    URL = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaFileSyncBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            partnerIdEqual=NotImplemented,
            fileObjectTypeEqual=NotImplemented,
            fileObjectTypeIn=NotImplemented,
            objectIdEqual=NotImplemented,
            objectIdIn=NotImplemented,
            versionEqual=NotImplemented,
            versionIn=NotImplemented,
            objectSubTypeEqual=NotImplemented,
            objectSubTypeIn=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            originalEqual=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            readyAtGreaterThanOrEqual=NotImplemented,
            readyAtLessThanOrEqual=NotImplemented,
            syncTimeGreaterThanOrEqual=NotImplemented,
            syncTimeLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            fileTypeEqual=NotImplemented,
            fileTypeIn=NotImplemented,
            linkedIdEqual=NotImplemented,
            linkCountGreaterThanOrEqual=NotImplemented,
            linkCountLessThanOrEqual=NotImplemented,
            fileSizeGreaterThanOrEqual=NotImplemented,
            fileSizeLessThanOrEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var KalturaFileSyncObjectType
        self.fileObjectTypeEqual = fileObjectTypeEqual

        # @var string
        self.fileObjectTypeIn = fileObjectTypeIn

        # @var string
        self.objectIdEqual = objectIdEqual

        # @var string
        self.objectIdIn = objectIdIn

        # @var string
        self.versionEqual = versionEqual

        # @var string
        self.versionIn = versionIn

        # @var int
        self.objectSubTypeEqual = objectSubTypeEqual

        # @var string
        self.objectSubTypeIn = objectSubTypeIn

        # @var string
        self.dcEqual = dcEqual

        # @var string
        self.dcIn = dcIn

        # @var int
        self.originalEqual = originalEqual

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual

        # @var int
        self.readyAtGreaterThanOrEqual = readyAtGreaterThanOrEqual

        # @var int
        self.readyAtLessThanOrEqual = readyAtLessThanOrEqual

        # @var int
        self.syncTimeGreaterThanOrEqual = syncTimeGreaterThanOrEqual

        # @var int
        self.syncTimeLessThanOrEqual = syncTimeLessThanOrEqual

        # @var KalturaFileSyncStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var KalturaFileSyncType
        self.fileTypeEqual = fileTypeEqual

        # @var string
        self.fileTypeIn = fileTypeIn

        # @var int
        self.linkedIdEqual = linkedIdEqual

        # @var int
        self.linkCountGreaterThanOrEqual = linkCountGreaterThanOrEqual

        # @var int
        self.linkCountLessThanOrEqual = linkCountLessThanOrEqual

        # @var int
        self.fileSizeGreaterThanOrEqual = fileSizeGreaterThanOrEqual

        # @var int
        self.fileSizeLessThanOrEqual = fileSizeLessThanOrEqual


    PROPERTY_LOADERS = {
        'partnerIdEqual': getXmlNodeInt, 
        'fileObjectTypeEqual': (KalturaEnumsFactory.createString, "KalturaFileSyncObjectType"), 
        'fileObjectTypeIn': getXmlNodeText, 
        'objectIdEqual': getXmlNodeText, 
        'objectIdIn': getXmlNodeText, 
        'versionEqual': getXmlNodeText, 
        'versionIn': getXmlNodeText, 
        'objectSubTypeEqual': getXmlNodeInt, 
        'objectSubTypeIn': getXmlNodeText, 
        'dcEqual': getXmlNodeText, 
        'dcIn': getXmlNodeText, 
        'originalEqual': getXmlNodeInt, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'readyAtGreaterThanOrEqual': getXmlNodeInt, 
        'readyAtLessThanOrEqual': getXmlNodeInt, 
        'syncTimeGreaterThanOrEqual': getXmlNodeInt, 
        'syncTimeLessThanOrEqual': getXmlNodeInt, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaFileSyncStatus"), 
        'statusIn': getXmlNodeText, 
        'fileTypeEqual': (KalturaEnumsFactory.createInt, "KalturaFileSyncType"), 
        'fileTypeIn': getXmlNodeText, 
        'linkedIdEqual': getXmlNodeInt, 
        'linkCountGreaterThanOrEqual': getXmlNodeInt, 
        'linkCountLessThanOrEqual': getXmlNodeInt, 
        'fileSizeGreaterThanOrEqual': getXmlNodeInt, 
        'fileSizeLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFileSyncBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaFileSyncBaseFilter")
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringEnumIfDefined("fileObjectTypeEqual", self.fileObjectTypeEqual)
        kparams.addStringIfDefined("fileObjectTypeIn", self.fileObjectTypeIn)
        kparams.addStringIfDefined("objectIdEqual", self.objectIdEqual)
        kparams.addStringIfDefined("objectIdIn", self.objectIdIn)
        kparams.addStringIfDefined("versionEqual", self.versionEqual)
        kparams.addStringIfDefined("versionIn", self.versionIn)
        kparams.addIntIfDefined("objectSubTypeEqual", self.objectSubTypeEqual)
        kparams.addStringIfDefined("objectSubTypeIn", self.objectSubTypeIn)
        kparams.addStringIfDefined("dcEqual", self.dcEqual)
        kparams.addStringIfDefined("dcIn", self.dcIn)
        kparams.addIntIfDefined("originalEqual", self.originalEqual)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntIfDefined("readyAtGreaterThanOrEqual", self.readyAtGreaterThanOrEqual)
        kparams.addIntIfDefined("readyAtLessThanOrEqual", self.readyAtLessThanOrEqual)
        kparams.addIntIfDefined("syncTimeGreaterThanOrEqual", self.syncTimeGreaterThanOrEqual)
        kparams.addIntIfDefined("syncTimeLessThanOrEqual", self.syncTimeLessThanOrEqual)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addIntEnumIfDefined("fileTypeEqual", self.fileTypeEqual)
        kparams.addStringIfDefined("fileTypeIn", self.fileTypeIn)
        kparams.addIntIfDefined("linkedIdEqual", self.linkedIdEqual)
        kparams.addIntIfDefined("linkCountGreaterThanOrEqual", self.linkCountGreaterThanOrEqual)
        kparams.addIntIfDefined("linkCountLessThanOrEqual", self.linkCountLessThanOrEqual)
        kparams.addIntIfDefined("fileSizeGreaterThanOrEqual", self.fileSizeGreaterThanOrEqual)
        kparams.addIntIfDefined("fileSizeLessThanOrEqual", self.fileSizeLessThanOrEqual)
        return kparams

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getFileObjectTypeEqual(self):
        return self.fileObjectTypeEqual

    def setFileObjectTypeEqual(self, newFileObjectTypeEqual):
        self.fileObjectTypeEqual = newFileObjectTypeEqual

    def getFileObjectTypeIn(self):
        return self.fileObjectTypeIn

    def setFileObjectTypeIn(self, newFileObjectTypeIn):
        self.fileObjectTypeIn = newFileObjectTypeIn

    def getObjectIdEqual(self):
        return self.objectIdEqual

    def setObjectIdEqual(self, newObjectIdEqual):
        self.objectIdEqual = newObjectIdEqual

    def getObjectIdIn(self):
        return self.objectIdIn

    def setObjectIdIn(self, newObjectIdIn):
        self.objectIdIn = newObjectIdIn

    def getVersionEqual(self):
        return self.versionEqual

    def setVersionEqual(self, newVersionEqual):
        self.versionEqual = newVersionEqual

    def getVersionIn(self):
        return self.versionIn

    def setVersionIn(self, newVersionIn):
        self.versionIn = newVersionIn

    def getObjectSubTypeEqual(self):
        return self.objectSubTypeEqual

    def setObjectSubTypeEqual(self, newObjectSubTypeEqual):
        self.objectSubTypeEqual = newObjectSubTypeEqual

    def getObjectSubTypeIn(self):
        return self.objectSubTypeIn

    def setObjectSubTypeIn(self, newObjectSubTypeIn):
        self.objectSubTypeIn = newObjectSubTypeIn

    def getDcEqual(self):
        return self.dcEqual

    def setDcEqual(self, newDcEqual):
        self.dcEqual = newDcEqual

    def getDcIn(self):
        return self.dcIn

    def setDcIn(self, newDcIn):
        self.dcIn = newDcIn

    def getOriginalEqual(self):
        return self.originalEqual

    def setOriginalEqual(self, newOriginalEqual):
        self.originalEqual = newOriginalEqual

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual

    def getReadyAtGreaterThanOrEqual(self):
        return self.readyAtGreaterThanOrEqual

    def setReadyAtGreaterThanOrEqual(self, newReadyAtGreaterThanOrEqual):
        self.readyAtGreaterThanOrEqual = newReadyAtGreaterThanOrEqual

    def getReadyAtLessThanOrEqual(self):
        return self.readyAtLessThanOrEqual

    def setReadyAtLessThanOrEqual(self, newReadyAtLessThanOrEqual):
        self.readyAtLessThanOrEqual = newReadyAtLessThanOrEqual

    def getSyncTimeGreaterThanOrEqual(self):
        return self.syncTimeGreaterThanOrEqual

    def setSyncTimeGreaterThanOrEqual(self, newSyncTimeGreaterThanOrEqual):
        self.syncTimeGreaterThanOrEqual = newSyncTimeGreaterThanOrEqual

    def getSyncTimeLessThanOrEqual(self):
        return self.syncTimeLessThanOrEqual

    def setSyncTimeLessThanOrEqual(self, newSyncTimeLessThanOrEqual):
        self.syncTimeLessThanOrEqual = newSyncTimeLessThanOrEqual

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getFileTypeEqual(self):
        return self.fileTypeEqual

    def setFileTypeEqual(self, newFileTypeEqual):
        self.fileTypeEqual = newFileTypeEqual

    def getFileTypeIn(self):
        return self.fileTypeIn

    def setFileTypeIn(self, newFileTypeIn):
        self.fileTypeIn = newFileTypeIn

    def getLinkedIdEqual(self):
        return self.linkedIdEqual

    def setLinkedIdEqual(self, newLinkedIdEqual):
        self.linkedIdEqual = newLinkedIdEqual

    def getLinkCountGreaterThanOrEqual(self):
        return self.linkCountGreaterThanOrEqual

    def setLinkCountGreaterThanOrEqual(self, newLinkCountGreaterThanOrEqual):
        self.linkCountGreaterThanOrEqual = newLinkCountGreaterThanOrEqual

    def getLinkCountLessThanOrEqual(self):
        return self.linkCountLessThanOrEqual

    def setLinkCountLessThanOrEqual(self, newLinkCountLessThanOrEqual):
        self.linkCountLessThanOrEqual = newLinkCountLessThanOrEqual

    def getFileSizeGreaterThanOrEqual(self):
        return self.fileSizeGreaterThanOrEqual

    def setFileSizeGreaterThanOrEqual(self, newFileSizeGreaterThanOrEqual):
        self.fileSizeGreaterThanOrEqual = newFileSizeGreaterThanOrEqual

    def getFileSizeLessThanOrEqual(self):
        return self.fileSizeLessThanOrEqual

    def setFileSizeLessThanOrEqual(self, newFileSizeLessThanOrEqual):
        self.fileSizeLessThanOrEqual = newFileSizeLessThanOrEqual


class KalturaFileSyncFilter(KalturaFileSyncBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            partnerIdEqual=NotImplemented,
            fileObjectTypeEqual=NotImplemented,
            fileObjectTypeIn=NotImplemented,
            objectIdEqual=NotImplemented,
            objectIdIn=NotImplemented,
            versionEqual=NotImplemented,
            versionIn=NotImplemented,
            objectSubTypeEqual=NotImplemented,
            objectSubTypeIn=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            originalEqual=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            readyAtGreaterThanOrEqual=NotImplemented,
            readyAtLessThanOrEqual=NotImplemented,
            syncTimeGreaterThanOrEqual=NotImplemented,
            syncTimeLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            fileTypeEqual=NotImplemented,
            fileTypeIn=NotImplemented,
            linkedIdEqual=NotImplemented,
            linkCountGreaterThanOrEqual=NotImplemented,
            linkCountLessThanOrEqual=NotImplemented,
            fileSizeGreaterThanOrEqual=NotImplemented,
            fileSizeLessThanOrEqual=NotImplemented):
        KalturaFileSyncBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            partnerIdEqual,
            fileObjectTypeEqual,
            fileObjectTypeIn,
            objectIdEqual,
            objectIdIn,
            versionEqual,
            versionIn,
            objectSubTypeEqual,
            objectSubTypeIn,
            dcEqual,
            dcIn,
            originalEqual,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            readyAtGreaterThanOrEqual,
            readyAtLessThanOrEqual,
            syncTimeGreaterThanOrEqual,
            syncTimeLessThanOrEqual,
            statusEqual,
            statusIn,
            fileTypeEqual,
            fileTypeIn,
            linkedIdEqual,
            linkCountGreaterThanOrEqual,
            linkCountLessThanOrEqual,
            fileSizeGreaterThanOrEqual,
            fileSizeLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFileSyncBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFileSyncFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFileSyncBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaFileSyncFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaFileSyncClientPlugin(KalturaClientPlugin):
    # KalturaFileSyncClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaFileSyncClientPlugin
    @staticmethod
    def get(client):
        if KalturaFileSyncClientPlugin.instance == None:
            KalturaFileSyncClientPlugin.instance = KalturaFileSyncClientPlugin(client)
        return KalturaFileSyncClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaFileSyncOrderBy': KalturaFileSyncOrderBy,
            'KalturaFileSyncStatus': KalturaFileSyncStatus,
            'KalturaFileSyncType': KalturaFileSyncType,
        }

    def getTypes(self):
        return {
            'KalturaFileSyncBaseFilter': KalturaFileSyncBaseFilter,
            'KalturaFileSyncFilter': KalturaFileSyncFilter,
        }

    # @return string
    def getName(self):
        return 'fileSync'


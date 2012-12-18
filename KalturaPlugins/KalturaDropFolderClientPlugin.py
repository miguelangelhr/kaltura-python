import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
class KalturaDropFolderContentFileHandlerMatchPolicy:
    ADD_AS_NEW = 1
    MATCH_EXISTING_OR_ADD_AS_NEW = 2
    MATCH_EXISTING_OR_KEEP_IN_FOLDER = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDropFolderFileDeletePolicy:
    MANUAL_DELETE = 1
    AUTO_DELETE = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDropFolderFileErrorCode:
    ERROR_UPDATE_ENTRY = "1"
    ERROR_ADD_ENTRY = "2"
    FLAVOR_NOT_FOUND = "3"
    FLAVOR_MISSING_IN_FILE_NAME = "4"
    SLUG_REGEX_NO_MATCH = "5"
    ERROR_READING_FILE = "6"
    ERROR_DOWNLOADING_FILE = "7"
    LOCAL_FILE_WRONG_SIZE = "dropFolderXmlBulkUpload.LOCAL_FILE_WRONG_SIZE"
    LOCAL_FILE_WRONG_CHECKSUM = "dropFolderXmlBulkUpload.LOCAL_FILE_WRONG_CHECKSUM"
    ERROR_WRITING_TEMP_FILE = "dropFolderXmlBulkUpload.ERROR_WRITING_TEMP_FILE"
    ERROR_ADDING_BULK_UPLOAD = "dropFolderXmlBulkUpload.ERROR_ADDING_BULK_UPLOAD"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDropFolderFileHandlerType:
    CONTENT = "1"
    XML = "dropFolderXmlBulkUpload.XML"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDropFolderFileOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    FILE_NAME_ASC = "+fileName"
    FILE_NAME_DESC = "-fileName"
    FILE_SIZE_ASC = "+fileSize"
    FILE_SIZE_DESC = "-fileSize"
    FILE_SIZE_LAST_SET_AT_ASC = "+fileSizeLastSetAt"
    FILE_SIZE_LAST_SET_AT_DESC = "-fileSizeLastSetAt"
    PARSED_SLUG_ASC = "+parsedSlug"
    PARSED_SLUG_DESC = "-parsedSlug"
    PARSED_FLAVOR_ASC = "+parsedFlavor"
    PARSED_FLAVOR_DESC = "-parsedFlavor"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDropFolderFileStatus:
    UPLOADING = 1
    PENDING = 2
    WAITING = 3
    HANDLED = 4
    IGNORE = 5
    DELETED = 6
    PURGED = 7
    NO_MATCH = 8
    ERROR_HANDLING = 9
    ERROR_DELETING = 10
    DOWNLOADING = 11
    ERROR_DOWNLOADING = 12

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDropFolderOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDropFolderStatus:
    DISABLED = 0
    ENABLED = 1
    DELETED = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDropFolderType:
    LOCAL = "1"
    FTP = "2"
    SCP = "3"
    SFTP = "4"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaFtpDropFolderOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaRemoteDropFolderOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaScpDropFolderOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSftpDropFolderOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSshDropFolderOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaDropFolderFileHandlerConfig(KalturaObjectBase):
    def __init__(self,
            handlerType=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var KalturaDropFolderFileHandlerType
        # @readonly
        self.handlerType = handlerType


    PROPERTY_LOADERS = {
        'handlerType': (KalturaEnumsFactory.createString, "KalturaDropFolderFileHandlerType"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDropFolderFileHandlerConfig.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDropFolderFileHandlerConfig")
        return kparams

    def getHandlerType(self):
        return self.handlerType


class KalturaDropFolder(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            type=NotImplemented,
            status=NotImplemented,
            conversionProfileId=NotImplemented,
            dc=NotImplemented,
            path=NotImplemented,
            fileSizeCheckInterval=NotImplemented,
            fileDeletePolicy=NotImplemented,
            autoFileDeleteDays=NotImplemented,
            fileHandlerType=NotImplemented,
            fileNamePatterns=NotImplemented,
            fileHandlerConfig=NotImplemented,
            tags=NotImplemented,
            ignoreFileNamePatterns=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var int
        # @insertonly
        self.partnerId = partnerId

        # @var string
        self.name = name

        # @var string
        self.description = description

        # @var KalturaDropFolderType
        self.type = type

        # @var KalturaDropFolderStatus
        self.status = status

        # @var int
        self.conversionProfileId = conversionProfileId

        # @var int
        self.dc = dc

        # @var string
        self.path = path

        # The ammount of time, in seconds, that should pass so that a file with no change in size we'll be treated as "finished uploading to folder"
        # @var int
        self.fileSizeCheckInterval = fileSizeCheckInterval

        # @var KalturaDropFolderFileDeletePolicy
        self.fileDeletePolicy = fileDeletePolicy

        # @var int
        self.autoFileDeleteDays = autoFileDeleteDays

        # @var KalturaDropFolderFileHandlerType
        self.fileHandlerType = fileHandlerType

        # @var string
        self.fileNamePatterns = fileNamePatterns

        # @var KalturaDropFolderFileHandlerConfig
        self.fileHandlerConfig = fileHandlerConfig

        # @var string
        self.tags = tags

        # @var string
        self.ignoreFileNamePatterns = ignoreFileNamePatterns

        # @var int
        # @readonly
        self.createdAt = createdAt

        # @var int
        # @readonly
        self.updatedAt = updatedAt


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'type': (KalturaEnumsFactory.createString, "KalturaDropFolderType"), 
        'status': (KalturaEnumsFactory.createInt, "KalturaDropFolderStatus"), 
        'conversionProfileId': getXmlNodeInt, 
        'dc': getXmlNodeInt, 
        'path': getXmlNodeText, 
        'fileSizeCheckInterval': getXmlNodeInt, 
        'fileDeletePolicy': (KalturaEnumsFactory.createInt, "KalturaDropFolderFileDeletePolicy"), 
        'autoFileDeleteDays': getXmlNodeInt, 
        'fileHandlerType': (KalturaEnumsFactory.createString, "KalturaDropFolderFileHandlerType"), 
        'fileNamePatterns': getXmlNodeText, 
        'fileHandlerConfig': (KalturaObjectFactory.create, KalturaDropFolderFileHandlerConfig), 
        'tags': getXmlNodeText, 
        'ignoreFileNamePatterns': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDropFolder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDropFolder")
        kparams.addIntIfDefined("partnerId", self.partnerId)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringEnumIfDefined("type", self.type)
        kparams.addIntEnumIfDefined("status", self.status)
        kparams.addIntIfDefined("conversionProfileId", self.conversionProfileId)
        kparams.addIntIfDefined("dc", self.dc)
        kparams.addStringIfDefined("path", self.path)
        kparams.addIntIfDefined("fileSizeCheckInterval", self.fileSizeCheckInterval)
        kparams.addIntEnumIfDefined("fileDeletePolicy", self.fileDeletePolicy)
        kparams.addIntIfDefined("autoFileDeleteDays", self.autoFileDeleteDays)
        kparams.addStringEnumIfDefined("fileHandlerType", self.fileHandlerType)
        kparams.addStringIfDefined("fileNamePatterns", self.fileNamePatterns)
        kparams.addObjectIfDefined("fileHandlerConfig", self.fileHandlerConfig)
        kparams.addStringIfDefined("tags", self.tags)
        kparams.addStringIfDefined("ignoreFileNamePatterns", self.ignoreFileNamePatterns)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getConversionProfileId(self):
        return self.conversionProfileId

    def setConversionProfileId(self, newConversionProfileId):
        self.conversionProfileId = newConversionProfileId

    def getDc(self):
        return self.dc

    def setDc(self, newDc):
        self.dc = newDc

    def getPath(self):
        return self.path

    def setPath(self, newPath):
        self.path = newPath

    def getFileSizeCheckInterval(self):
        return self.fileSizeCheckInterval

    def setFileSizeCheckInterval(self, newFileSizeCheckInterval):
        self.fileSizeCheckInterval = newFileSizeCheckInterval

    def getFileDeletePolicy(self):
        return self.fileDeletePolicy

    def setFileDeletePolicy(self, newFileDeletePolicy):
        self.fileDeletePolicy = newFileDeletePolicy

    def getAutoFileDeleteDays(self):
        return self.autoFileDeleteDays

    def setAutoFileDeleteDays(self, newAutoFileDeleteDays):
        self.autoFileDeleteDays = newAutoFileDeleteDays

    def getFileHandlerType(self):
        return self.fileHandlerType

    def setFileHandlerType(self, newFileHandlerType):
        self.fileHandlerType = newFileHandlerType

    def getFileNamePatterns(self):
        return self.fileNamePatterns

    def setFileNamePatterns(self, newFileNamePatterns):
        self.fileNamePatterns = newFileNamePatterns

    def getFileHandlerConfig(self):
        return self.fileHandlerConfig

    def setFileHandlerConfig(self, newFileHandlerConfig):
        self.fileHandlerConfig = newFileHandlerConfig

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getIgnoreFileNamePatterns(self):
        return self.ignoreFileNamePatterns

    def setIgnoreFileNamePatterns(self, newIgnoreFileNamePatterns):
        self.ignoreFileNamePatterns = newIgnoreFileNamePatterns

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt


class KalturaDropFolderBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            nameLike=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            conversionProfileIdEqual=NotImplemented,
            conversionProfileIdIn=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            pathLike=NotImplemented,
            fileHandlerTypeEqual=NotImplemented,
            fileHandlerTypeIn=NotImplemented,
            fileNamePatternsLike=NotImplemented,
            fileNamePatternsMultiLikeOr=NotImplemented,
            fileNamePatternsMultiLikeAnd=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var string
        self.partnerIdIn = partnerIdIn

        # @var string
        self.nameLike = nameLike

        # @var KalturaDropFolderType
        self.typeEqual = typeEqual

        # @var string
        self.typeIn = typeIn

        # @var KalturaDropFolderStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var int
        self.conversionProfileIdEqual = conversionProfileIdEqual

        # @var string
        self.conversionProfileIdIn = conversionProfileIdIn

        # @var int
        self.dcEqual = dcEqual

        # @var string
        self.dcIn = dcIn

        # @var string
        self.pathLike = pathLike

        # @var KalturaDropFolderFileHandlerType
        self.fileHandlerTypeEqual = fileHandlerTypeEqual

        # @var string
        self.fileHandlerTypeIn = fileHandlerTypeIn

        # @var string
        self.fileNamePatternsLike = fileNamePatternsLike

        # @var string
        self.fileNamePatternsMultiLikeOr = fileNamePatternsMultiLikeOr

        # @var string
        self.fileNamePatternsMultiLikeAnd = fileNamePatternsMultiLikeAnd

        # @var string
        self.tagsLike = tagsLike

        # @var string
        self.tagsMultiLikeOr = tagsMultiLikeOr

        # @var string
        self.tagsMultiLikeAnd = tagsMultiLikeAnd

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'nameLike': getXmlNodeText, 
        'typeEqual': (KalturaEnumsFactory.createString, "KalturaDropFolderType"), 
        'typeIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaDropFolderStatus"), 
        'statusIn': getXmlNodeText, 
        'conversionProfileIdEqual': getXmlNodeInt, 
        'conversionProfileIdIn': getXmlNodeText, 
        'dcEqual': getXmlNodeInt, 
        'dcIn': getXmlNodeText, 
        'pathLike': getXmlNodeText, 
        'fileHandlerTypeEqual': (KalturaEnumsFactory.createString, "KalturaDropFolderFileHandlerType"), 
        'fileHandlerTypeIn': getXmlNodeText, 
        'fileNamePatternsLike': getXmlNodeText, 
        'fileNamePatternsMultiLikeOr': getXmlNodeText, 
        'fileNamePatternsMultiLikeAnd': getXmlNodeText, 
        'tagsLike': getXmlNodeText, 
        'tagsMultiLikeOr': getXmlNodeText, 
        'tagsMultiLikeAnd': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDropFolderBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaDropFolderBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfDefined("nameLike", self.nameLike)
        kparams.addStringEnumIfDefined("typeEqual", self.typeEqual)
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addIntIfDefined("conversionProfileIdEqual", self.conversionProfileIdEqual)
        kparams.addStringIfDefined("conversionProfileIdIn", self.conversionProfileIdIn)
        kparams.addIntIfDefined("dcEqual", self.dcEqual)
        kparams.addStringIfDefined("dcIn", self.dcIn)
        kparams.addStringIfDefined("pathLike", self.pathLike)
        kparams.addStringEnumIfDefined("fileHandlerTypeEqual", self.fileHandlerTypeEqual)
        kparams.addStringIfDefined("fileHandlerTypeIn", self.fileHandlerTypeIn)
        kparams.addStringIfDefined("fileNamePatternsLike", self.fileNamePatternsLike)
        kparams.addStringIfDefined("fileNamePatternsMultiLikeOr", self.fileNamePatternsMultiLikeOr)
        kparams.addStringIfDefined("fileNamePatternsMultiLikeAnd", self.fileNamePatternsMultiLikeAnd)
        kparams.addStringIfDefined("tagsLike", self.tagsLike)
        kparams.addStringIfDefined("tagsMultiLikeOr", self.tagsMultiLikeOr)
        kparams.addStringIfDefined("tagsMultiLikeAnd", self.tagsMultiLikeAnd)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getNameLike(self):
        return self.nameLike

    def setNameLike(self, newNameLike):
        self.nameLike = newNameLike

    def getTypeEqual(self):
        return self.typeEqual

    def setTypeEqual(self, newTypeEqual):
        self.typeEqual = newTypeEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getConversionProfileIdEqual(self):
        return self.conversionProfileIdEqual

    def setConversionProfileIdEqual(self, newConversionProfileIdEqual):
        self.conversionProfileIdEqual = newConversionProfileIdEqual

    def getConversionProfileIdIn(self):
        return self.conversionProfileIdIn

    def setConversionProfileIdIn(self, newConversionProfileIdIn):
        self.conversionProfileIdIn = newConversionProfileIdIn

    def getDcEqual(self):
        return self.dcEqual

    def setDcEqual(self, newDcEqual):
        self.dcEqual = newDcEqual

    def getDcIn(self):
        return self.dcIn

    def setDcIn(self, newDcIn):
        self.dcIn = newDcIn

    def getPathLike(self):
        return self.pathLike

    def setPathLike(self, newPathLike):
        self.pathLike = newPathLike

    def getFileHandlerTypeEqual(self):
        return self.fileHandlerTypeEqual

    def setFileHandlerTypeEqual(self, newFileHandlerTypeEqual):
        self.fileHandlerTypeEqual = newFileHandlerTypeEqual

    def getFileHandlerTypeIn(self):
        return self.fileHandlerTypeIn

    def setFileHandlerTypeIn(self, newFileHandlerTypeIn):
        self.fileHandlerTypeIn = newFileHandlerTypeIn

    def getFileNamePatternsLike(self):
        return self.fileNamePatternsLike

    def setFileNamePatternsLike(self, newFileNamePatternsLike):
        self.fileNamePatternsLike = newFileNamePatternsLike

    def getFileNamePatternsMultiLikeOr(self):
        return self.fileNamePatternsMultiLikeOr

    def setFileNamePatternsMultiLikeOr(self, newFileNamePatternsMultiLikeOr):
        self.fileNamePatternsMultiLikeOr = newFileNamePatternsMultiLikeOr

    def getFileNamePatternsMultiLikeAnd(self):
        return self.fileNamePatternsMultiLikeAnd

    def setFileNamePatternsMultiLikeAnd(self, newFileNamePatternsMultiLikeAnd):
        self.fileNamePatternsMultiLikeAnd = newFileNamePatternsMultiLikeAnd

    def getTagsLike(self):
        return self.tagsLike

    def setTagsLike(self, newTagsLike):
        self.tagsLike = newTagsLike

    def getTagsMultiLikeOr(self):
        return self.tagsMultiLikeOr

    def setTagsMultiLikeOr(self, newTagsMultiLikeOr):
        self.tagsMultiLikeOr = newTagsMultiLikeOr

    def getTagsMultiLikeAnd(self):
        return self.tagsMultiLikeAnd

    def setTagsMultiLikeAnd(self, newTagsMultiLikeAnd):
        self.tagsMultiLikeAnd = newTagsMultiLikeAnd

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


class KalturaDropFolderFilter(KalturaDropFolderBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            nameLike=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            conversionProfileIdEqual=NotImplemented,
            conversionProfileIdIn=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            pathLike=NotImplemented,
            fileHandlerTypeEqual=NotImplemented,
            fileHandlerTypeIn=NotImplemented,
            fileNamePatternsLike=NotImplemented,
            fileNamePatternsMultiLikeOr=NotImplemented,
            fileNamePatternsMultiLikeAnd=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaDropFolderBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            nameLike,
            typeEqual,
            typeIn,
            statusEqual,
            statusIn,
            conversionProfileIdEqual,
            conversionProfileIdIn,
            dcEqual,
            dcIn,
            pathLike,
            fileHandlerTypeEqual,
            fileHandlerTypeIn,
            fileNamePatternsLike,
            fileNamePatternsMultiLikeOr,
            fileNamePatternsMultiLikeAnd,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDropFolderBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDropFolderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolderBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaDropFolderFilter")
        return kparams


class KalturaDropFolderListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaDropFolder
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaDropFolder), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDropFolderListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDropFolderListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaDropFolderFile(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            dropFolderId=NotImplemented,
            fileName=NotImplemented,
            fileSize=NotImplemented,
            fileSizeLastSetAt=NotImplemented,
            status=NotImplemented,
            parsedSlug=NotImplemented,
            parsedFlavor=NotImplemented,
            errorCode=NotImplemented,
            errorDescription=NotImplemented,
            lastModificationTime=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var int
        # @insertonly
        self.dropFolderId = dropFolderId

        # @var string
        # @insertonly
        self.fileName = fileName

        # @var int
        self.fileSize = fileSize

        # @var int
        # @readonly
        self.fileSizeLastSetAt = fileSizeLastSetAt

        # @var KalturaDropFolderFileStatus
        # @readonly
        self.status = status

        # @var string
        self.parsedSlug = parsedSlug

        # @var string
        self.parsedFlavor = parsedFlavor

        # @var KalturaDropFolderFileErrorCode
        self.errorCode = errorCode

        # @var string
        self.errorDescription = errorDescription

        # @var string
        self.lastModificationTime = lastModificationTime

        # @var int
        # @readonly
        self.createdAt = createdAt

        # @var int
        # @readonly
        self.updatedAt = updatedAt


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'dropFolderId': getXmlNodeInt, 
        'fileName': getXmlNodeText, 
        'fileSize': getXmlNodeInt, 
        'fileSizeLastSetAt': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createInt, "KalturaDropFolderFileStatus"), 
        'parsedSlug': getXmlNodeText, 
        'parsedFlavor': getXmlNodeText, 
        'errorCode': (KalturaEnumsFactory.createString, "KalturaDropFolderFileErrorCode"), 
        'errorDescription': getXmlNodeText, 
        'lastModificationTime': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDropFolderFile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDropFolderFile")
        kparams.addIntIfDefined("dropFolderId", self.dropFolderId)
        kparams.addStringIfDefined("fileName", self.fileName)
        kparams.addIntIfDefined("fileSize", self.fileSize)
        kparams.addStringIfDefined("parsedSlug", self.parsedSlug)
        kparams.addStringIfDefined("parsedFlavor", self.parsedFlavor)
        kparams.addStringEnumIfDefined("errorCode", self.errorCode)
        kparams.addStringIfDefined("errorDescription", self.errorDescription)
        kparams.addStringIfDefined("lastModificationTime", self.lastModificationTime)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getDropFolderId(self):
        return self.dropFolderId

    def setDropFolderId(self, newDropFolderId):
        self.dropFolderId = newDropFolderId

    def getFileName(self):
        return self.fileName

    def setFileName(self, newFileName):
        self.fileName = newFileName

    def getFileSize(self):
        return self.fileSize

    def setFileSize(self, newFileSize):
        self.fileSize = newFileSize

    def getFileSizeLastSetAt(self):
        return self.fileSizeLastSetAt

    def getStatus(self):
        return self.status

    def getParsedSlug(self):
        return self.parsedSlug

    def setParsedSlug(self, newParsedSlug):
        self.parsedSlug = newParsedSlug

    def getParsedFlavor(self):
        return self.parsedFlavor

    def setParsedFlavor(self, newParsedFlavor):
        self.parsedFlavor = newParsedFlavor

    def getErrorCode(self):
        return self.errorCode

    def setErrorCode(self, newErrorCode):
        self.errorCode = newErrorCode

    def getErrorDescription(self):
        return self.errorDescription

    def setErrorDescription(self, newErrorDescription):
        self.errorDescription = newErrorDescription

    def getLastModificationTime(self):
        return self.lastModificationTime

    def setLastModificationTime(self, newLastModificationTime):
        self.lastModificationTime = newLastModificationTime

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt


class KalturaDropFolderFileBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            dropFolderIdEqual=NotImplemented,
            dropFolderIdIn=NotImplemented,
            fileNameEqual=NotImplemented,
            fileNameIn=NotImplemented,
            fileNameLike=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            parsedSlugEqual=NotImplemented,
            parsedSlugIn=NotImplemented,
            parsedSlugLike=NotImplemented,
            parsedFlavorEqual=NotImplemented,
            parsedFlavorIn=NotImplemented,
            parsedFlavorLike=NotImplemented,
            errorCodeEqual=NotImplemented,
            errorCodeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var string
        self.partnerIdIn = partnerIdIn

        # @var int
        self.dropFolderIdEqual = dropFolderIdEqual

        # @var string
        self.dropFolderIdIn = dropFolderIdIn

        # @var string
        self.fileNameEqual = fileNameEqual

        # @var string
        self.fileNameIn = fileNameIn

        # @var string
        self.fileNameLike = fileNameLike

        # @var KalturaDropFolderFileStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var string
        self.parsedSlugEqual = parsedSlugEqual

        # @var string
        self.parsedSlugIn = parsedSlugIn

        # @var string
        self.parsedSlugLike = parsedSlugLike

        # @var string
        self.parsedFlavorEqual = parsedFlavorEqual

        # @var string
        self.parsedFlavorIn = parsedFlavorIn

        # @var string
        self.parsedFlavorLike = parsedFlavorLike

        # @var KalturaDropFolderFileErrorCode
        self.errorCodeEqual = errorCodeEqual

        # @var string
        self.errorCodeIn = errorCodeIn

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'dropFolderIdEqual': getXmlNodeInt, 
        'dropFolderIdIn': getXmlNodeText, 
        'fileNameEqual': getXmlNodeText, 
        'fileNameIn': getXmlNodeText, 
        'fileNameLike': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaDropFolderFileStatus"), 
        'statusIn': getXmlNodeText, 
        'parsedSlugEqual': getXmlNodeText, 
        'parsedSlugIn': getXmlNodeText, 
        'parsedSlugLike': getXmlNodeText, 
        'parsedFlavorEqual': getXmlNodeText, 
        'parsedFlavorIn': getXmlNodeText, 
        'parsedFlavorLike': getXmlNodeText, 
        'errorCodeEqual': (KalturaEnumsFactory.createString, "KalturaDropFolderFileErrorCode"), 
        'errorCodeIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDropFolderFileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaDropFolderFileBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("partnerIdIn", self.partnerIdIn)
        kparams.addIntIfDefined("dropFolderIdEqual", self.dropFolderIdEqual)
        kparams.addStringIfDefined("dropFolderIdIn", self.dropFolderIdIn)
        kparams.addStringIfDefined("fileNameEqual", self.fileNameEqual)
        kparams.addStringIfDefined("fileNameIn", self.fileNameIn)
        kparams.addStringIfDefined("fileNameLike", self.fileNameLike)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addStringIfDefined("parsedSlugEqual", self.parsedSlugEqual)
        kparams.addStringIfDefined("parsedSlugIn", self.parsedSlugIn)
        kparams.addStringIfDefined("parsedSlugLike", self.parsedSlugLike)
        kparams.addStringIfDefined("parsedFlavorEqual", self.parsedFlavorEqual)
        kparams.addStringIfDefined("parsedFlavorIn", self.parsedFlavorIn)
        kparams.addStringIfDefined("parsedFlavorLike", self.parsedFlavorLike)
        kparams.addStringEnumIfDefined("errorCodeEqual", self.errorCodeEqual)
        kparams.addStringIfDefined("errorCodeIn", self.errorCodeIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getDropFolderIdEqual(self):
        return self.dropFolderIdEqual

    def setDropFolderIdEqual(self, newDropFolderIdEqual):
        self.dropFolderIdEqual = newDropFolderIdEqual

    def getDropFolderIdIn(self):
        return self.dropFolderIdIn

    def setDropFolderIdIn(self, newDropFolderIdIn):
        self.dropFolderIdIn = newDropFolderIdIn

    def getFileNameEqual(self):
        return self.fileNameEqual

    def setFileNameEqual(self, newFileNameEqual):
        self.fileNameEqual = newFileNameEqual

    def getFileNameIn(self):
        return self.fileNameIn

    def setFileNameIn(self, newFileNameIn):
        self.fileNameIn = newFileNameIn

    def getFileNameLike(self):
        return self.fileNameLike

    def setFileNameLike(self, newFileNameLike):
        self.fileNameLike = newFileNameLike

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getParsedSlugEqual(self):
        return self.parsedSlugEqual

    def setParsedSlugEqual(self, newParsedSlugEqual):
        self.parsedSlugEqual = newParsedSlugEqual

    def getParsedSlugIn(self):
        return self.parsedSlugIn

    def setParsedSlugIn(self, newParsedSlugIn):
        self.parsedSlugIn = newParsedSlugIn

    def getParsedSlugLike(self):
        return self.parsedSlugLike

    def setParsedSlugLike(self, newParsedSlugLike):
        self.parsedSlugLike = newParsedSlugLike

    def getParsedFlavorEqual(self):
        return self.parsedFlavorEqual

    def setParsedFlavorEqual(self, newParsedFlavorEqual):
        self.parsedFlavorEqual = newParsedFlavorEqual

    def getParsedFlavorIn(self):
        return self.parsedFlavorIn

    def setParsedFlavorIn(self, newParsedFlavorIn):
        self.parsedFlavorIn = newParsedFlavorIn

    def getParsedFlavorLike(self):
        return self.parsedFlavorLike

    def setParsedFlavorLike(self, newParsedFlavorLike):
        self.parsedFlavorLike = newParsedFlavorLike

    def getErrorCodeEqual(self):
        return self.errorCodeEqual

    def setErrorCodeEqual(self, newErrorCodeEqual):
        self.errorCodeEqual = newErrorCodeEqual

    def getErrorCodeIn(self):
        return self.errorCodeIn

    def setErrorCodeIn(self, newErrorCodeIn):
        self.errorCodeIn = newErrorCodeIn

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


class KalturaDropFolderFileFilter(KalturaDropFolderFileBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            dropFolderIdEqual=NotImplemented,
            dropFolderIdIn=NotImplemented,
            fileNameEqual=NotImplemented,
            fileNameIn=NotImplemented,
            fileNameLike=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            parsedSlugEqual=NotImplemented,
            parsedSlugIn=NotImplemented,
            parsedSlugLike=NotImplemented,
            parsedFlavorEqual=NotImplemented,
            parsedFlavorIn=NotImplemented,
            parsedFlavorLike=NotImplemented,
            errorCodeEqual=NotImplemented,
            errorCodeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaDropFolderFileBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            dropFolderIdEqual,
            dropFolderIdIn,
            fileNameEqual,
            fileNameIn,
            fileNameLike,
            statusEqual,
            statusIn,
            parsedSlugEqual,
            parsedSlugIn,
            parsedSlugLike,
            parsedFlavorEqual,
            parsedFlavorIn,
            parsedFlavorLike,
            errorCodeEqual,
            errorCodeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDropFolderFileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDropFolderFileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolderFileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaDropFolderFileFilter")
        return kparams


class KalturaDropFolderFileListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaDropFolderFile
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaDropFolderFile), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDropFolderFileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDropFolderFileListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaRemoteDropFolderBaseFilter(KalturaDropFolderFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            nameLike=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            conversionProfileIdEqual=NotImplemented,
            conversionProfileIdIn=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            pathLike=NotImplemented,
            fileHandlerTypeEqual=NotImplemented,
            fileHandlerTypeIn=NotImplemented,
            fileNamePatternsLike=NotImplemented,
            fileNamePatternsMultiLikeOr=NotImplemented,
            fileNamePatternsMultiLikeAnd=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaDropFolderFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            nameLike,
            typeEqual,
            typeIn,
            statusEqual,
            statusIn,
            conversionProfileIdEqual,
            conversionProfileIdIn,
            dcEqual,
            dcIn,
            pathLike,
            fileHandlerTypeEqual,
            fileHandlerTypeIn,
            fileNamePatternsLike,
            fileNamePatternsMultiLikeOr,
            fileNamePatternsMultiLikeAnd,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDropFolderFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRemoteDropFolderBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolderFilter.toParams(self)
        kparams.put("objectType", "KalturaRemoteDropFolderBaseFilter")
        return kparams


class KalturaRemoteDropFolderFilter(KalturaRemoteDropFolderBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            nameLike=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            conversionProfileIdEqual=NotImplemented,
            conversionProfileIdIn=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            pathLike=NotImplemented,
            fileHandlerTypeEqual=NotImplemented,
            fileHandlerTypeIn=NotImplemented,
            fileNamePatternsLike=NotImplemented,
            fileNamePatternsMultiLikeOr=NotImplemented,
            fileNamePatternsMultiLikeAnd=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaRemoteDropFolderBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            nameLike,
            typeEqual,
            typeIn,
            statusEqual,
            statusIn,
            conversionProfileIdEqual,
            conversionProfileIdIn,
            dcEqual,
            dcIn,
            pathLike,
            fileHandlerTypeEqual,
            fileHandlerTypeIn,
            fileNamePatternsLike,
            fileNamePatternsMultiLikeOr,
            fileNamePatternsMultiLikeAnd,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaRemoteDropFolderBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRemoteDropFolderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRemoteDropFolderBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaRemoteDropFolderFilter")
        return kparams


class KalturaFtpDropFolderBaseFilter(KalturaRemoteDropFolderFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            nameLike=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            conversionProfileIdEqual=NotImplemented,
            conversionProfileIdIn=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            pathLike=NotImplemented,
            fileHandlerTypeEqual=NotImplemented,
            fileHandlerTypeIn=NotImplemented,
            fileNamePatternsLike=NotImplemented,
            fileNamePatternsMultiLikeOr=NotImplemented,
            fileNamePatternsMultiLikeAnd=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaRemoteDropFolderFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            nameLike,
            typeEqual,
            typeIn,
            statusEqual,
            statusIn,
            conversionProfileIdEqual,
            conversionProfileIdIn,
            dcEqual,
            dcIn,
            pathLike,
            fileHandlerTypeEqual,
            fileHandlerTypeIn,
            fileNamePatternsLike,
            fileNamePatternsMultiLikeOr,
            fileNamePatternsMultiLikeAnd,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaRemoteDropFolderFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFtpDropFolderBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRemoteDropFolderFilter.toParams(self)
        kparams.put("objectType", "KalturaFtpDropFolderBaseFilter")
        return kparams


class KalturaSshDropFolderBaseFilter(KalturaRemoteDropFolderFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            nameLike=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            conversionProfileIdEqual=NotImplemented,
            conversionProfileIdIn=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            pathLike=NotImplemented,
            fileHandlerTypeEqual=NotImplemented,
            fileHandlerTypeIn=NotImplemented,
            fileNamePatternsLike=NotImplemented,
            fileNamePatternsMultiLikeOr=NotImplemented,
            fileNamePatternsMultiLikeAnd=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaRemoteDropFolderFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            nameLike,
            typeEqual,
            typeIn,
            statusEqual,
            statusIn,
            conversionProfileIdEqual,
            conversionProfileIdIn,
            dcEqual,
            dcIn,
            pathLike,
            fileHandlerTypeEqual,
            fileHandlerTypeIn,
            fileNamePatternsLike,
            fileNamePatternsMultiLikeOr,
            fileNamePatternsMultiLikeAnd,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaRemoteDropFolderFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSshDropFolderBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRemoteDropFolderFilter.toParams(self)
        kparams.put("objectType", "KalturaSshDropFolderBaseFilter")
        return kparams


class KalturaSshDropFolderFilter(KalturaSshDropFolderBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            nameLike=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            conversionProfileIdEqual=NotImplemented,
            conversionProfileIdIn=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            pathLike=NotImplemented,
            fileHandlerTypeEqual=NotImplemented,
            fileHandlerTypeIn=NotImplemented,
            fileNamePatternsLike=NotImplemented,
            fileNamePatternsMultiLikeOr=NotImplemented,
            fileNamePatternsMultiLikeAnd=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaSshDropFolderBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            nameLike,
            typeEqual,
            typeIn,
            statusEqual,
            statusIn,
            conversionProfileIdEqual,
            conversionProfileIdIn,
            dcEqual,
            dcIn,
            pathLike,
            fileHandlerTypeEqual,
            fileHandlerTypeIn,
            fileNamePatternsLike,
            fileNamePatternsMultiLikeOr,
            fileNamePatternsMultiLikeAnd,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaSshDropFolderBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSshDropFolderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSshDropFolderBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaSshDropFolderFilter")
        return kparams


class KalturaScpDropFolderBaseFilter(KalturaSshDropFolderFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            nameLike=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            conversionProfileIdEqual=NotImplemented,
            conversionProfileIdIn=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            pathLike=NotImplemented,
            fileHandlerTypeEqual=NotImplemented,
            fileHandlerTypeIn=NotImplemented,
            fileNamePatternsLike=NotImplemented,
            fileNamePatternsMultiLikeOr=NotImplemented,
            fileNamePatternsMultiLikeAnd=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaSshDropFolderFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            nameLike,
            typeEqual,
            typeIn,
            statusEqual,
            statusIn,
            conversionProfileIdEqual,
            conversionProfileIdIn,
            dcEqual,
            dcIn,
            pathLike,
            fileHandlerTypeEqual,
            fileHandlerTypeIn,
            fileNamePatternsLike,
            fileNamePatternsMultiLikeOr,
            fileNamePatternsMultiLikeAnd,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaSshDropFolderFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaScpDropFolderBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSshDropFolderFilter.toParams(self)
        kparams.put("objectType", "KalturaScpDropFolderBaseFilter")
        return kparams


class KalturaSftpDropFolderBaseFilter(KalturaSshDropFolderFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            nameLike=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            conversionProfileIdEqual=NotImplemented,
            conversionProfileIdIn=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            pathLike=NotImplemented,
            fileHandlerTypeEqual=NotImplemented,
            fileHandlerTypeIn=NotImplemented,
            fileNamePatternsLike=NotImplemented,
            fileNamePatternsMultiLikeOr=NotImplemented,
            fileNamePatternsMultiLikeAnd=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaSshDropFolderFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            nameLike,
            typeEqual,
            typeIn,
            statusEqual,
            statusIn,
            conversionProfileIdEqual,
            conversionProfileIdIn,
            dcEqual,
            dcIn,
            pathLike,
            fileHandlerTypeEqual,
            fileHandlerTypeIn,
            fileNamePatternsLike,
            fileNamePatternsMultiLikeOr,
            fileNamePatternsMultiLikeAnd,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaSshDropFolderFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSftpDropFolderBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSshDropFolderFilter.toParams(self)
        kparams.put("objectType", "KalturaSftpDropFolderBaseFilter")
        return kparams


class KalturaFtpDropFolderFilter(KalturaFtpDropFolderBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            nameLike=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            conversionProfileIdEqual=NotImplemented,
            conversionProfileIdIn=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            pathLike=NotImplemented,
            fileHandlerTypeEqual=NotImplemented,
            fileHandlerTypeIn=NotImplemented,
            fileNamePatternsLike=NotImplemented,
            fileNamePatternsMultiLikeOr=NotImplemented,
            fileNamePatternsMultiLikeAnd=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaFtpDropFolderBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            nameLike,
            typeEqual,
            typeIn,
            statusEqual,
            statusIn,
            conversionProfileIdEqual,
            conversionProfileIdIn,
            dcEqual,
            dcIn,
            pathLike,
            fileHandlerTypeEqual,
            fileHandlerTypeIn,
            fileNamePatternsLike,
            fileNamePatternsMultiLikeOr,
            fileNamePatternsMultiLikeAnd,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFtpDropFolderBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFtpDropFolderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFtpDropFolderBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaFtpDropFolderFilter")
        return kparams


class KalturaScpDropFolderFilter(KalturaScpDropFolderBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            nameLike=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            conversionProfileIdEqual=NotImplemented,
            conversionProfileIdIn=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            pathLike=NotImplemented,
            fileHandlerTypeEqual=NotImplemented,
            fileHandlerTypeIn=NotImplemented,
            fileNamePatternsLike=NotImplemented,
            fileNamePatternsMultiLikeOr=NotImplemented,
            fileNamePatternsMultiLikeAnd=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaScpDropFolderBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            nameLike,
            typeEqual,
            typeIn,
            statusEqual,
            statusIn,
            conversionProfileIdEqual,
            conversionProfileIdIn,
            dcEqual,
            dcIn,
            pathLike,
            fileHandlerTypeEqual,
            fileHandlerTypeIn,
            fileNamePatternsLike,
            fileNamePatternsMultiLikeOr,
            fileNamePatternsMultiLikeAnd,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaScpDropFolderBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaScpDropFolderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaScpDropFolderBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaScpDropFolderFilter")
        return kparams


class KalturaSftpDropFolderFilter(KalturaSftpDropFolderBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            nameLike=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            conversionProfileIdEqual=NotImplemented,
            conversionProfileIdIn=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            pathLike=NotImplemented,
            fileHandlerTypeEqual=NotImplemented,
            fileHandlerTypeIn=NotImplemented,
            fileNamePatternsLike=NotImplemented,
            fileNamePatternsMultiLikeOr=NotImplemented,
            fileNamePatternsMultiLikeAnd=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaSftpDropFolderBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            nameLike,
            typeEqual,
            typeIn,
            statusEqual,
            statusIn,
            conversionProfileIdEqual,
            conversionProfileIdIn,
            dcEqual,
            dcIn,
            pathLike,
            fileHandlerTypeEqual,
            fileHandlerTypeIn,
            fileNamePatternsLike,
            fileNamePatternsMultiLikeOr,
            fileNamePatternsMultiLikeAnd,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaSftpDropFolderBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSftpDropFolderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSftpDropFolderBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaSftpDropFolderFilter")
        return kparams


class KalturaDropFolderFileResource(KalturaDataCenterContentResource):
    """Used to ingest media that dropped through drop folder"""

    def __init__(self,
            dropFolderFileId=NotImplemented):
        KalturaDataCenterContentResource.__init__(self)

        # Id of the drop folder file object
        # @var int
        self.dropFolderFileId = dropFolderFileId


    PROPERTY_LOADERS = {
        'dropFolderFileId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaDataCenterContentResource.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDropFolderFileResource.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDataCenterContentResource.toParams(self)
        kparams.put("objectType", "KalturaDropFolderFileResource")
        kparams.addIntIfDefined("dropFolderFileId", self.dropFolderFileId)
        return kparams

    def getDropFolderFileId(self):
        return self.dropFolderFileId

    def setDropFolderFileId(self, newDropFolderFileId):
        self.dropFolderFileId = newDropFolderFileId


class KalturaDropFolderContentFileHandlerConfig(KalturaDropFolderFileHandlerConfig):
    def __init__(self,
            handlerType=NotImplemented,
            contentMatchPolicy=NotImplemented,
            slugRegex=NotImplemented):
        KalturaDropFolderFileHandlerConfig.__init__(self,
            handlerType)

        # @var KalturaDropFolderContentFileHandlerMatchPolicy
        self.contentMatchPolicy = contentMatchPolicy

        # Regular expression that defines valid file names to be handled.
        # The following might be extracted from the file name and used if defined:
        # - (?P<referenceId>\w+) - will be used as the drop folder file's parsed slug.
        # - (?P<flavorName>\w+)  - will be used as the drop folder file's parsed flavor.
        # @var string
        self.slugRegex = slugRegex


    PROPERTY_LOADERS = {
        'contentMatchPolicy': (KalturaEnumsFactory.createInt, "KalturaDropFolderContentFileHandlerMatchPolicy"), 
        'slugRegex': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaDropFolderFileHandlerConfig.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDropFolderContentFileHandlerConfig.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolderFileHandlerConfig.toParams(self)
        kparams.put("objectType", "KalturaDropFolderContentFileHandlerConfig")
        kparams.addIntEnumIfDefined("contentMatchPolicy", self.contentMatchPolicy)
        kparams.addStringIfDefined("slugRegex", self.slugRegex)
        return kparams

    def getContentMatchPolicy(self):
        return self.contentMatchPolicy

    def setContentMatchPolicy(self, newContentMatchPolicy):
        self.contentMatchPolicy = newContentMatchPolicy

    def getSlugRegex(self):
        return self.slugRegex

    def setSlugRegex(self, newSlugRegex):
        self.slugRegex = newSlugRegex


class KalturaRemoteDropFolder(KalturaDropFolder):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            type=NotImplemented,
            status=NotImplemented,
            conversionProfileId=NotImplemented,
            dc=NotImplemented,
            path=NotImplemented,
            fileSizeCheckInterval=NotImplemented,
            fileDeletePolicy=NotImplemented,
            autoFileDeleteDays=NotImplemented,
            fileHandlerType=NotImplemented,
            fileNamePatterns=NotImplemented,
            fileHandlerConfig=NotImplemented,
            tags=NotImplemented,
            ignoreFileNamePatterns=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented):
        KalturaDropFolder.__init__(self,
            id,
            partnerId,
            name,
            description,
            type,
            status,
            conversionProfileId,
            dc,
            path,
            fileSizeCheckInterval,
            fileDeletePolicy,
            autoFileDeleteDays,
            fileHandlerType,
            fileNamePatterns,
            fileHandlerConfig,
            tags,
            ignoreFileNamePatterns,
            createdAt,
            updatedAt)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDropFolder.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRemoteDropFolder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolder.toParams(self)
        kparams.put("objectType", "KalturaRemoteDropFolder")
        return kparams


class KalturaFtpDropFolder(KalturaRemoteDropFolder):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            type=NotImplemented,
            status=NotImplemented,
            conversionProfileId=NotImplemented,
            dc=NotImplemented,
            path=NotImplemented,
            fileSizeCheckInterval=NotImplemented,
            fileDeletePolicy=NotImplemented,
            autoFileDeleteDays=NotImplemented,
            fileHandlerType=NotImplemented,
            fileNamePatterns=NotImplemented,
            fileHandlerConfig=NotImplemented,
            tags=NotImplemented,
            ignoreFileNamePatterns=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            host=NotImplemented,
            port=NotImplemented,
            username=NotImplemented,
            password=NotImplemented):
        KalturaRemoteDropFolder.__init__(self,
            id,
            partnerId,
            name,
            description,
            type,
            status,
            conversionProfileId,
            dc,
            path,
            fileSizeCheckInterval,
            fileDeletePolicy,
            autoFileDeleteDays,
            fileHandlerType,
            fileNamePatterns,
            fileHandlerConfig,
            tags,
            ignoreFileNamePatterns,
            createdAt,
            updatedAt)

        # @var string
        self.host = host

        # @var int
        self.port = port

        # @var string
        self.username = username

        # @var string
        self.password = password


    PROPERTY_LOADERS = {
        'host': getXmlNodeText, 
        'port': getXmlNodeInt, 
        'username': getXmlNodeText, 
        'password': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaRemoteDropFolder.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFtpDropFolder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRemoteDropFolder.toParams(self)
        kparams.put("objectType", "KalturaFtpDropFolder")
        kparams.addStringIfDefined("host", self.host)
        kparams.addIntIfDefined("port", self.port)
        kparams.addStringIfDefined("username", self.username)
        kparams.addStringIfDefined("password", self.password)
        return kparams

    def getHost(self):
        return self.host

    def setHost(self, newHost):
        self.host = newHost

    def getPort(self):
        return self.port

    def setPort(self, newPort):
        self.port = newPort

    def getUsername(self):
        return self.username

    def setUsername(self, newUsername):
        self.username = newUsername

    def getPassword(self):
        return self.password

    def setPassword(self, newPassword):
        self.password = newPassword


class KalturaSshDropFolder(KalturaRemoteDropFolder):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            type=NotImplemented,
            status=NotImplemented,
            conversionProfileId=NotImplemented,
            dc=NotImplemented,
            path=NotImplemented,
            fileSizeCheckInterval=NotImplemented,
            fileDeletePolicy=NotImplemented,
            autoFileDeleteDays=NotImplemented,
            fileHandlerType=NotImplemented,
            fileNamePatterns=NotImplemented,
            fileHandlerConfig=NotImplemented,
            tags=NotImplemented,
            ignoreFileNamePatterns=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            host=NotImplemented,
            port=NotImplemented,
            username=NotImplemented,
            password=NotImplemented,
            privateKey=NotImplemented,
            publicKey=NotImplemented,
            passPhrase=NotImplemented):
        KalturaRemoteDropFolder.__init__(self,
            id,
            partnerId,
            name,
            description,
            type,
            status,
            conversionProfileId,
            dc,
            path,
            fileSizeCheckInterval,
            fileDeletePolicy,
            autoFileDeleteDays,
            fileHandlerType,
            fileNamePatterns,
            fileHandlerConfig,
            tags,
            ignoreFileNamePatterns,
            createdAt,
            updatedAt)

        # @var string
        self.host = host

        # @var int
        self.port = port

        # @var string
        self.username = username

        # @var string
        self.password = password

        # @var string
        self.privateKey = privateKey

        # @var string
        self.publicKey = publicKey

        # @var string
        self.passPhrase = passPhrase


    PROPERTY_LOADERS = {
        'host': getXmlNodeText, 
        'port': getXmlNodeInt, 
        'username': getXmlNodeText, 
        'password': getXmlNodeText, 
        'privateKey': getXmlNodeText, 
        'publicKey': getXmlNodeText, 
        'passPhrase': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaRemoteDropFolder.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSshDropFolder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRemoteDropFolder.toParams(self)
        kparams.put("objectType", "KalturaSshDropFolder")
        kparams.addStringIfDefined("host", self.host)
        kparams.addIntIfDefined("port", self.port)
        kparams.addStringIfDefined("username", self.username)
        kparams.addStringIfDefined("password", self.password)
        kparams.addStringIfDefined("privateKey", self.privateKey)
        kparams.addStringIfDefined("publicKey", self.publicKey)
        kparams.addStringIfDefined("passPhrase", self.passPhrase)
        return kparams

    def getHost(self):
        return self.host

    def setHost(self, newHost):
        self.host = newHost

    def getPort(self):
        return self.port

    def setPort(self, newPort):
        self.port = newPort

    def getUsername(self):
        return self.username

    def setUsername(self, newUsername):
        self.username = newUsername

    def getPassword(self):
        return self.password

    def setPassword(self, newPassword):
        self.password = newPassword

    def getPrivateKey(self):
        return self.privateKey

    def setPrivateKey(self, newPrivateKey):
        self.privateKey = newPrivateKey

    def getPublicKey(self):
        return self.publicKey

    def setPublicKey(self, newPublicKey):
        self.publicKey = newPublicKey

    def getPassPhrase(self):
        return self.passPhrase

    def setPassPhrase(self, newPassPhrase):
        self.passPhrase = newPassPhrase


class KalturaScpDropFolder(KalturaSshDropFolder):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            type=NotImplemented,
            status=NotImplemented,
            conversionProfileId=NotImplemented,
            dc=NotImplemented,
            path=NotImplemented,
            fileSizeCheckInterval=NotImplemented,
            fileDeletePolicy=NotImplemented,
            autoFileDeleteDays=NotImplemented,
            fileHandlerType=NotImplemented,
            fileNamePatterns=NotImplemented,
            fileHandlerConfig=NotImplemented,
            tags=NotImplemented,
            ignoreFileNamePatterns=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            host=NotImplemented,
            port=NotImplemented,
            username=NotImplemented,
            password=NotImplemented,
            privateKey=NotImplemented,
            publicKey=NotImplemented,
            passPhrase=NotImplemented):
        KalturaSshDropFolder.__init__(self,
            id,
            partnerId,
            name,
            description,
            type,
            status,
            conversionProfileId,
            dc,
            path,
            fileSizeCheckInterval,
            fileDeletePolicy,
            autoFileDeleteDays,
            fileHandlerType,
            fileNamePatterns,
            fileHandlerConfig,
            tags,
            ignoreFileNamePatterns,
            createdAt,
            updatedAt,
            host,
            port,
            username,
            password,
            privateKey,
            publicKey,
            passPhrase)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaSshDropFolder.fromXml(self, node)
        self.fromXmlImpl(node, KalturaScpDropFolder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSshDropFolder.toParams(self)
        kparams.put("objectType", "KalturaScpDropFolder")
        return kparams


class KalturaSftpDropFolder(KalturaSshDropFolder):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            type=NotImplemented,
            status=NotImplemented,
            conversionProfileId=NotImplemented,
            dc=NotImplemented,
            path=NotImplemented,
            fileSizeCheckInterval=NotImplemented,
            fileDeletePolicy=NotImplemented,
            autoFileDeleteDays=NotImplemented,
            fileHandlerType=NotImplemented,
            fileNamePatterns=NotImplemented,
            fileHandlerConfig=NotImplemented,
            tags=NotImplemented,
            ignoreFileNamePatterns=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            host=NotImplemented,
            port=NotImplemented,
            username=NotImplemented,
            password=NotImplemented,
            privateKey=NotImplemented,
            publicKey=NotImplemented,
            passPhrase=NotImplemented):
        KalturaSshDropFolder.__init__(self,
            id,
            partnerId,
            name,
            description,
            type,
            status,
            conversionProfileId,
            dc,
            path,
            fileSizeCheckInterval,
            fileDeletePolicy,
            autoFileDeleteDays,
            fileHandlerType,
            fileNamePatterns,
            fileHandlerConfig,
            tags,
            ignoreFileNamePatterns,
            createdAt,
            updatedAt,
            host,
            port,
            username,
            password,
            privateKey,
            publicKey,
            passPhrase)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaSshDropFolder.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSftpDropFolder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSshDropFolder.toParams(self)
        kparams.put("objectType", "KalturaSftpDropFolder")
        return kparams


########## services ##########

class KalturaDropFolderService(KalturaServiceBase):
    """DropFolder service lets you create and manage drop folders"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, dropFolder):
        """Allows you to add a new KalturaDropFolder object"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("dropFolder", dropFolder)
        self.client.queueServiceActionCall("dropfolder_dropfolder", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDropFolder)

    def get(self, dropFolderId):
        """Retrieve a KalturaDropFolder object by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("dropFolderId", dropFolderId);
        self.client.queueServiceActionCall("dropfolder_dropfolder", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDropFolder)

    def update(self, dropFolderId, dropFolder):
        """Update an existing KalturaDropFolder object"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("dropFolderId", dropFolderId);
        kparams.addObjectIfDefined("dropFolder", dropFolder)
        self.client.queueServiceActionCall("dropfolder_dropfolder", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDropFolder)

    def delete(self, dropFolderId):
        """Mark the KalturaDropFolder object as deleted"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("dropFolderId", dropFolderId);
        self.client.queueServiceActionCall("dropfolder_dropfolder", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDropFolder)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List KalturaDropFolder objects"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("dropfolder_dropfolder", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDropFolderListResponse)


class KalturaDropFolderFileService(KalturaServiceBase):
    """DropFolderFile service lets you create and manage drop folder files"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, dropFolderFile):
        """Allows you to add a new KalturaDropFolderFile object"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("dropFolderFile", dropFolderFile)
        self.client.queueServiceActionCall("dropfolder_dropfolderfile", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDropFolderFile)

    def get(self, dropFolderFileId):
        """Retrieve a KalturaDropFolderFile object by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("dropFolderFileId", dropFolderFileId);
        self.client.queueServiceActionCall("dropfolder_dropfolderfile", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDropFolderFile)

    def update(self, dropFolderFileId, dropFolderFile):
        """Update an existing KalturaDropFolderFile object"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("dropFolderFileId", dropFolderFileId);
        kparams.addObjectIfDefined("dropFolderFile", dropFolderFile)
        self.client.queueServiceActionCall("dropfolder_dropfolderfile", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDropFolderFile)

    def updateStatus(self, dropFolderFileId, status):
        """Update status of KalturaDropFolderFile"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("dropFolderFileId", dropFolderFileId);
        kparams.addIntIfDefined("status", status);
        self.client.queueServiceActionCall("dropfolder_dropfolderfile", "updateStatus", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDropFolderFile)

    def delete(self, dropFolderFileId):
        """Mark the KalturaDropFolderFile object as deleted"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("dropFolderFileId", dropFolderFileId);
        self.client.queueServiceActionCall("dropfolder_dropfolderfile", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDropFolderFile)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List KalturaDropFolderFile objects"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("dropfolder_dropfolderfile", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDropFolderFileListResponse)

    def ignore(self, dropFolderFileId):
        """Set the KalturaDropFolderFile status to ignore (KalturaDropFolderFileStatus::IGNORE)"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("dropFolderFileId", dropFolderFileId);
        self.client.queueServiceActionCall("dropfolder_dropfolderfile", "ignore", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDropFolderFile)

########## main ##########
class KalturaDropFolderClientPlugin(KalturaClientPlugin):
    # KalturaDropFolderClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaDropFolderClientPlugin
    @staticmethod
    def get(client):
        if KalturaDropFolderClientPlugin.instance == None:
            KalturaDropFolderClientPlugin.instance = KalturaDropFolderClientPlugin(client)
        return KalturaDropFolderClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'dropFolder': KalturaDropFolderService,
            'dropFolderFile': KalturaDropFolderFileService,
        }

    def getEnums(self):
        return {
            'KalturaDropFolderContentFileHandlerMatchPolicy': KalturaDropFolderContentFileHandlerMatchPolicy,
            'KalturaDropFolderFileDeletePolicy': KalturaDropFolderFileDeletePolicy,
            'KalturaDropFolderFileErrorCode': KalturaDropFolderFileErrorCode,
            'KalturaDropFolderFileHandlerType': KalturaDropFolderFileHandlerType,
            'KalturaDropFolderFileOrderBy': KalturaDropFolderFileOrderBy,
            'KalturaDropFolderFileStatus': KalturaDropFolderFileStatus,
            'KalturaDropFolderOrderBy': KalturaDropFolderOrderBy,
            'KalturaDropFolderStatus': KalturaDropFolderStatus,
            'KalturaDropFolderType': KalturaDropFolderType,
            'KalturaFtpDropFolderOrderBy': KalturaFtpDropFolderOrderBy,
            'KalturaRemoteDropFolderOrderBy': KalturaRemoteDropFolderOrderBy,
            'KalturaScpDropFolderOrderBy': KalturaScpDropFolderOrderBy,
            'KalturaSftpDropFolderOrderBy': KalturaSftpDropFolderOrderBy,
            'KalturaSshDropFolderOrderBy': KalturaSshDropFolderOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaDropFolderFileHandlerConfig': KalturaDropFolderFileHandlerConfig,
            'KalturaDropFolder': KalturaDropFolder,
            'KalturaDropFolderBaseFilter': KalturaDropFolderBaseFilter,
            'KalturaDropFolderFilter': KalturaDropFolderFilter,
            'KalturaDropFolderListResponse': KalturaDropFolderListResponse,
            'KalturaDropFolderFile': KalturaDropFolderFile,
            'KalturaDropFolderFileBaseFilter': KalturaDropFolderFileBaseFilter,
            'KalturaDropFolderFileFilter': KalturaDropFolderFileFilter,
            'KalturaDropFolderFileListResponse': KalturaDropFolderFileListResponse,
            'KalturaRemoteDropFolderBaseFilter': KalturaRemoteDropFolderBaseFilter,
            'KalturaRemoteDropFolderFilter': KalturaRemoteDropFolderFilter,
            'KalturaFtpDropFolderBaseFilter': KalturaFtpDropFolderBaseFilter,
            'KalturaSshDropFolderBaseFilter': KalturaSshDropFolderBaseFilter,
            'KalturaSshDropFolderFilter': KalturaSshDropFolderFilter,
            'KalturaScpDropFolderBaseFilter': KalturaScpDropFolderBaseFilter,
            'KalturaSftpDropFolderBaseFilter': KalturaSftpDropFolderBaseFilter,
            'KalturaFtpDropFolderFilter': KalturaFtpDropFolderFilter,
            'KalturaScpDropFolderFilter': KalturaScpDropFolderFilter,
            'KalturaSftpDropFolderFilter': KalturaSftpDropFolderFilter,
            'KalturaDropFolderFileResource': KalturaDropFolderFileResource,
            'KalturaDropFolderContentFileHandlerConfig': KalturaDropFolderContentFileHandlerConfig,
            'KalturaRemoteDropFolder': KalturaRemoteDropFolder,
            'KalturaFtpDropFolder': KalturaFtpDropFolder,
            'KalturaSshDropFolder': KalturaSshDropFolder,
            'KalturaScpDropFolder': KalturaScpDropFolder,
            'KalturaSftpDropFolder': KalturaSftpDropFolder,
        }

    # @return string
    def getName(self):
        return 'dropFolder'


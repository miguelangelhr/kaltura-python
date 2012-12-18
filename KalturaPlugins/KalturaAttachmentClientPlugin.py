import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
class KalturaAttachmentAssetOrderBy:
    SIZE_ASC = "+size"
    SIZE_DESC = "-size"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    DELETED_AT_ASC = "+deletedAt"
    DELETED_AT_DESC = "-deletedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAttachmentAssetStatus:
    ERROR = -1
    QUEUED = 0
    READY = 2
    DELETED = 3
    IMPORTING = 7

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAttachmentType:
    TEXT = "1"
    MEDIA = "2"
    DOCUMENT = "3"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaAttachmentAsset(KalturaAsset):
    def __init__(self,
            id=NotImplemented,
            entryId=NotImplemented,
            partnerId=NotImplemented,
            version=NotImplemented,
            size=NotImplemented,
            tags=NotImplemented,
            fileExt=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            deletedAt=NotImplemented,
            description=NotImplemented,
            partnerData=NotImplemented,
            partnerDescription=NotImplemented,
            filename=NotImplemented,
            title=NotImplemented,
            format=NotImplemented,
            status=NotImplemented):
        KalturaAsset.__init__(self,
            id,
            entryId,
            partnerId,
            version,
            size,
            tags,
            fileExt,
            createdAt,
            updatedAt,
            deletedAt,
            description,
            partnerData,
            partnerDescription)

        # The filename of the attachment asset content
        # @var string
        self.filename = filename

        # Attachment asset title
        # @var string
        self.title = title

        # The attachment format
        # @var KalturaAttachmentType
        self.format = format

        # The status of the asset
        # @var KalturaAttachmentAssetStatus
        # @readonly
        self.status = status


    PROPERTY_LOADERS = {
        'filename': getXmlNodeText, 
        'title': getXmlNodeText, 
        'format': (KalturaEnumsFactory.createString, "KalturaAttachmentType"), 
        'status': (KalturaEnumsFactory.createInt, "KalturaAttachmentAssetStatus"), 
    }

    def fromXml(self, node):
        KalturaAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAttachmentAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAsset.toParams(self)
        kparams.put("objectType", "KalturaAttachmentAsset")
        kparams.addStringIfDefined("filename", self.filename)
        kparams.addStringIfDefined("title", self.title)
        kparams.addStringEnumIfDefined("format", self.format)
        return kparams

    def getFilename(self):
        return self.filename

    def setFilename(self, newFilename):
        self.filename = newFilename

    def getTitle(self):
        return self.title

    def setTitle(self, newTitle):
        self.title = newTitle

    def getFormat(self):
        return self.format

    def setFormat(self, newFormat):
        self.format = newFormat

    def getStatus(self):
        return self.status


class KalturaAttachmentAssetListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaAttachmentAsset
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaAttachmentAsset), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAttachmentAssetListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAttachmentAssetListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaAttachmentAssetBaseFilter(KalturaAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            entryIdEqual=NotImplemented,
            entryIdIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            sizeGreaterThanOrEqual=NotImplemented,
            sizeLessThanOrEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            deletedAtGreaterThanOrEqual=NotImplemented,
            deletedAtLessThanOrEqual=NotImplemented,
            formatEqual=NotImplemented,
            formatIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented):
        KalturaAssetFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            entryIdEqual,
            entryIdIn,
            partnerIdEqual,
            partnerIdIn,
            sizeGreaterThanOrEqual,
            sizeLessThanOrEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            deletedAtGreaterThanOrEqual,
            deletedAtLessThanOrEqual)

        # @var KalturaAttachmentType
        self.formatEqual = formatEqual

        # @var string
        self.formatIn = formatIn

        # @var KalturaAttachmentAssetStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var string
        self.statusNotIn = statusNotIn


    PROPERTY_LOADERS = {
        'formatEqual': (KalturaEnumsFactory.createString, "KalturaAttachmentType"), 
        'formatIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaAttachmentAssetStatus"), 
        'statusIn': getXmlNodeText, 
        'statusNotIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAttachmentAssetBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaAttachmentAssetBaseFilter")
        kparams.addStringEnumIfDefined("formatEqual", self.formatEqual)
        kparams.addStringIfDefined("formatIn", self.formatIn)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addStringIfDefined("statusNotIn", self.statusNotIn)
        return kparams

    def getFormatEqual(self):
        return self.formatEqual

    def setFormatEqual(self, newFormatEqual):
        self.formatEqual = newFormatEqual

    def getFormatIn(self):
        return self.formatIn

    def setFormatIn(self, newFormatIn):
        self.formatIn = newFormatIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getStatusNotIn(self):
        return self.statusNotIn

    def setStatusNotIn(self, newStatusNotIn):
        self.statusNotIn = newStatusNotIn


class KalturaAttachmentAssetFilter(KalturaAttachmentAssetBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            entryIdEqual=NotImplemented,
            entryIdIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            sizeGreaterThanOrEqual=NotImplemented,
            sizeLessThanOrEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            deletedAtGreaterThanOrEqual=NotImplemented,
            deletedAtLessThanOrEqual=NotImplemented,
            formatEqual=NotImplemented,
            formatIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented):
        KalturaAttachmentAssetBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            entryIdEqual,
            entryIdIn,
            partnerIdEqual,
            partnerIdIn,
            sizeGreaterThanOrEqual,
            sizeLessThanOrEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            deletedAtGreaterThanOrEqual,
            deletedAtLessThanOrEqual,
            formatEqual,
            formatIn,
            statusEqual,
            statusIn,
            statusNotIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAttachmentAssetBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAttachmentAssetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAttachmentAssetBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaAttachmentAssetFilter")
        return kparams


########## services ##########

class KalturaAttachmentAssetService(KalturaServiceBase):
    """Retrieve information and invoke actions on attachment Asset"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, entryId, attachmentAsset):
        """Add attachment asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("attachmentAsset", attachmentAsset)
        self.client.queueServiceActionCall("attachment_attachmentasset", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAttachmentAsset)

    def setContent(self, id, contentResource):
        """Update content of attachment asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addObjectIfDefined("contentResource", contentResource)
        self.client.queueServiceActionCall("attachment_attachmentasset", "setContent", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAttachmentAsset)

    def update(self, id, attachmentAsset):
        """Update attachment asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addObjectIfDefined("attachmentAsset", attachmentAsset)
        self.client.queueServiceActionCall("attachment_attachmentasset", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAttachmentAsset)

    def getUrl(self, id, storageId = NotImplemented):
        """Get download URL for the asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addIntIfDefined("storageId", storageId);
        self.client.queueServiceActionCall("attachment_attachmentasset", "getUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def getRemotePaths(self, id):
        """Get remote storage existing paths for the asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("attachment_attachmentasset", "getRemotePaths", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaRemotePathListResponse)

    def serve(self, attachmentAssetId):
        """Serves attachment by its id"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("attachmentAssetId", attachmentAssetId)
        self.client.queueServiceActionCall('attachment_attachmentasset', 'serve', kparams)
        return self.client.getServeUrl()

    def get(self, attachmentAssetId):
        kparams = KalturaParams()
        kparams.addStringIfDefined("attachmentAssetId", attachmentAssetId)
        self.client.queueServiceActionCall("attachment_attachmentasset", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAttachmentAsset)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List attachment Assets by filter and pager"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("attachment_attachmentasset", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAttachmentAssetListResponse)

    def delete(self, attachmentAssetId):
        kparams = KalturaParams()
        kparams.addStringIfDefined("attachmentAssetId", attachmentAssetId)
        self.client.queueServiceActionCall("attachment_attachmentasset", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

########## main ##########
class KalturaAttachmentClientPlugin(KalturaClientPlugin):
    # KalturaAttachmentClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaAttachmentClientPlugin
    @staticmethod
    def get(client):
        if KalturaAttachmentClientPlugin.instance == None:
            KalturaAttachmentClientPlugin.instance = KalturaAttachmentClientPlugin(client)
        return KalturaAttachmentClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'attachmentAsset': KalturaAttachmentAssetService,
        }

    def getEnums(self):
        return {
            'KalturaAttachmentAssetOrderBy': KalturaAttachmentAssetOrderBy,
            'KalturaAttachmentAssetStatus': KalturaAttachmentAssetStatus,
            'KalturaAttachmentType': KalturaAttachmentType,
        }

    def getTypes(self):
        return {
            'KalturaAttachmentAsset': KalturaAttachmentAsset,
            'KalturaAttachmentAssetListResponse': KalturaAttachmentAssetListResponse,
            'KalturaAttachmentAssetBaseFilter': KalturaAttachmentAssetBaseFilter,
            'KalturaAttachmentAssetFilter': KalturaAttachmentAssetFilter,
        }

    # @return string
    def getName(self):
        return 'attachment'


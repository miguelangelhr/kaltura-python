import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
class KalturaShortLinkOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    EXPIRES_AT_ASC = "+expiresAt"
    EXPIRES_AT_DESC = "-expiresAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaShortLinkStatus:
    DISABLED = 1
    ENABLED = 2
    DELETED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaShortLinkBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            expiresAtGreaterThanOrEqual=NotImplemented,
            expiresAtLessThanOrEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            userIdIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual

        # @var int
        self.expiresAtGreaterThanOrEqual = expiresAtGreaterThanOrEqual

        # @var int
        self.expiresAtLessThanOrEqual = expiresAtLessThanOrEqual

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var string
        self.partnerIdIn = partnerIdIn

        # @var string
        self.userIdEqual = userIdEqual

        # @var string
        self.userIdIn = userIdIn

        # @var string
        self.systemNameEqual = systemNameEqual

        # @var string
        self.systemNameIn = systemNameIn

        # @var KalturaShortLinkStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'expiresAtGreaterThanOrEqual': getXmlNodeInt, 
        'expiresAtLessThanOrEqual': getXmlNodeInt, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'userIdEqual': getXmlNodeText, 
        'userIdIn': getXmlNodeText, 
        'systemNameEqual': getXmlNodeText, 
        'systemNameIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaShortLinkStatus"), 
        'statusIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaShortLinkBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaShortLinkBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntIfDefined("expiresAtGreaterThanOrEqual", self.expiresAtGreaterThanOrEqual)
        kparams.addIntIfDefined("expiresAtLessThanOrEqual", self.expiresAtLessThanOrEqual)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfDefined("userIdEqual", self.userIdEqual)
        kparams.addStringIfDefined("userIdIn", self.userIdIn)
        kparams.addStringIfDefined("systemNameEqual", self.systemNameEqual)
        kparams.addStringIfDefined("systemNameIn", self.systemNameIn)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

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

    def getExpiresAtGreaterThanOrEqual(self):
        return self.expiresAtGreaterThanOrEqual

    def setExpiresAtGreaterThanOrEqual(self, newExpiresAtGreaterThanOrEqual):
        self.expiresAtGreaterThanOrEqual = newExpiresAtGreaterThanOrEqual

    def getExpiresAtLessThanOrEqual(self):
        return self.expiresAtLessThanOrEqual

    def setExpiresAtLessThanOrEqual(self, newExpiresAtLessThanOrEqual):
        self.expiresAtLessThanOrEqual = newExpiresAtLessThanOrEqual

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getUserIdEqual(self):
        return self.userIdEqual

    def setUserIdEqual(self, newUserIdEqual):
        self.userIdEqual = newUserIdEqual

    def getUserIdIn(self):
        return self.userIdIn

    def setUserIdIn(self, newUserIdIn):
        self.userIdIn = newUserIdIn

    def getSystemNameEqual(self):
        return self.systemNameEqual

    def setSystemNameEqual(self, newSystemNameEqual):
        self.systemNameEqual = newSystemNameEqual

    def getSystemNameIn(self):
        return self.systemNameIn

    def setSystemNameIn(self, newSystemNameIn):
        self.systemNameIn = newSystemNameIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn


class KalturaShortLinkFilter(KalturaShortLinkBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            expiresAtGreaterThanOrEqual=NotImplemented,
            expiresAtLessThanOrEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            userIdIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented):
        KalturaShortLinkBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            expiresAtGreaterThanOrEqual,
            expiresAtLessThanOrEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            userIdIn,
            systemNameEqual,
            systemNameIn,
            statusEqual,
            statusIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaShortLinkBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaShortLinkFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaShortLinkBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaShortLinkFilter")
        return kparams


class KalturaShortLink(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            expiresAt=NotImplemented,
            partnerId=NotImplemented,
            userId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            fullUrl=NotImplemented,
            status=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var int
        # @readonly
        self.createdAt = createdAt

        # @var int
        # @readonly
        self.updatedAt = updatedAt

        # @var int
        self.expiresAt = expiresAt

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var string
        self.userId = userId

        # @var string
        self.name = name

        # @var string
        self.systemName = systemName

        # @var string
        self.fullUrl = fullUrl

        # @var KalturaShortLinkStatus
        self.status = status


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'expiresAt': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'name': getXmlNodeText, 
        'systemName': getXmlNodeText, 
        'fullUrl': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaShortLinkStatus"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaShortLink.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaShortLink")
        kparams.addIntIfDefined("expiresAt", self.expiresAt)
        kparams.addStringIfDefined("userId", self.userId)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("systemName", self.systemName)
        kparams.addStringIfDefined("fullUrl", self.fullUrl)
        kparams.addIntEnumIfDefined("status", self.status)
        return kparams

    def getId(self):
        return self.id

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getExpiresAt(self):
        return self.expiresAt

    def setExpiresAt(self, newExpiresAt):
        self.expiresAt = newExpiresAt

    def getPartnerId(self):
        return self.partnerId

    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getFullUrl(self):
        return self.fullUrl

    def setFullUrl(self, newFullUrl):
        self.fullUrl = newFullUrl

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus


class KalturaShortLinkListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaShortLink
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaShortLink), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaShortLinkListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaShortLinkListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


########## services ##########

class KalturaShortLinkService(KalturaServiceBase):
    """Short link service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List short link objects by filter and pager"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("shortlink_shortlink", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaShortLinkListResponse)

    def add(self, shortLink):
        """Allows you to add a short link object"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("shortLink", shortLink)
        self.client.queueServiceActionCall("shortlink_shortlink", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaShortLink)

    def get(self, id):
        """Retrieve an short link object by id"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("shortlink_shortlink", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaShortLink)

    def update(self, id, shortLink):
        """Update exisitng short link"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addObjectIfDefined("shortLink", shortLink)
        self.client.queueServiceActionCall("shortlink_shortlink", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaShortLink)

    def delete(self, id):
        """Mark the short link as deleted"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("shortlink_shortlink", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaShortLink)

    def goto(self, id, proxy = False):
        """Serves short link"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addBoolIfDefined("proxy", proxy);
        self.client.queueServiceActionCall('shortlink_shortlink', 'goto', kparams)
        return self.client.getServeUrl()

########## main ##########
class KalturaShortLinkClientPlugin(KalturaClientPlugin):
    # KalturaShortLinkClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaShortLinkClientPlugin
    @staticmethod
    def get(client):
        if KalturaShortLinkClientPlugin.instance == None:
            KalturaShortLinkClientPlugin.instance = KalturaShortLinkClientPlugin(client)
        return KalturaShortLinkClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'shortLink': KalturaShortLinkService,
        }

    def getEnums(self):
        return {
            'KalturaShortLinkOrderBy': KalturaShortLinkOrderBy,
            'KalturaShortLinkStatus': KalturaShortLinkStatus,
        }

    def getTypes(self):
        return {
            'KalturaShortLinkBaseFilter': KalturaShortLinkBaseFilter,
            'KalturaShortLinkFilter': KalturaShortLinkFilter,
            'KalturaShortLink': KalturaShortLink,
            'KalturaShortLinkListResponse': KalturaShortLinkListResponse,
        }

    # @return string
    def getName(self):
        return 'shortLink'


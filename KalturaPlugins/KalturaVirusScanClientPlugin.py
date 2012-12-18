import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
class KalturaVirusFoundAction:
    NONE = 0
    DELETE = 1
    CLEAN_NONE = 2
    CLEAN_DELETE = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaVirusScanEngineType:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaVirusScanProfileOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaVirusScanProfileStatus:
    DISABLED = 1
    ENABLED = 2
    DELETED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaVirusScanProfileBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            nameEqual=NotImplemented,
            nameLike=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            engineTypeEqual=NotImplemented,
            engineTypeIn=NotImplemented):
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
        self.partnerIdEqual = partnerIdEqual

        # @var string
        self.partnerIdIn = partnerIdIn

        # @var string
        self.nameEqual = nameEqual

        # @var string
        self.nameLike = nameLike

        # @var KalturaVirusScanProfileStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var KalturaVirusScanEngineType
        self.engineTypeEqual = engineTypeEqual

        # @var string
        self.engineTypeIn = engineTypeIn


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'nameEqual': getXmlNodeText, 
        'nameLike': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaVirusScanProfileStatus"), 
        'statusIn': getXmlNodeText, 
        'engineTypeEqual': (KalturaEnumsFactory.createString, "KalturaVirusScanEngineType"), 
        'engineTypeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVirusScanProfileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaVirusScanProfileBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfDefined("nameEqual", self.nameEqual)
        kparams.addStringIfDefined("nameLike", self.nameLike)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addStringEnumIfDefined("engineTypeEqual", self.engineTypeEqual)
        kparams.addStringIfDefined("engineTypeIn", self.engineTypeIn)
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

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getNameEqual(self):
        return self.nameEqual

    def setNameEqual(self, newNameEqual):
        self.nameEqual = newNameEqual

    def getNameLike(self):
        return self.nameLike

    def setNameLike(self, newNameLike):
        self.nameLike = newNameLike

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getEngineTypeEqual(self):
        return self.engineTypeEqual

    def setEngineTypeEqual(self, newEngineTypeEqual):
        self.engineTypeEqual = newEngineTypeEqual

    def getEngineTypeIn(self):
        return self.engineTypeIn

    def setEngineTypeIn(self, newEngineTypeIn):
        self.engineTypeIn = newEngineTypeIn


class KalturaVirusScanProfileFilter(KalturaVirusScanProfileBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            nameEqual=NotImplemented,
            nameLike=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            engineTypeEqual=NotImplemented,
            engineTypeIn=NotImplemented):
        KalturaVirusScanProfileBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            partnerIdEqual,
            partnerIdIn,
            nameEqual,
            nameLike,
            statusEqual,
            statusIn,
            engineTypeEqual,
            engineTypeIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVirusScanProfileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVirusScanProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVirusScanProfileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaVirusScanProfileFilter")
        return kparams


class KalturaVirusScanProfile(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            status=NotImplemented,
            engineType=NotImplemented,
            entryFilter=NotImplemented,
            actionIfInfected=NotImplemented):
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
        # @readonly
        self.partnerId = partnerId

        # @var string
        self.name = name

        # @var KalturaVirusScanProfileStatus
        self.status = status

        # @var KalturaVirusScanEngineType
        self.engineType = engineType

        # @var KalturaBaseEntryFilter
        self.entryFilter = entryFilter

        # @var KalturaVirusFoundAction
        self.actionIfInfected = actionIfInfected


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaVirusScanProfileStatus"), 
        'engineType': (KalturaEnumsFactory.createString, "KalturaVirusScanEngineType"), 
        'entryFilter': (KalturaObjectFactory.create, KalturaBaseEntryFilter), 
        'actionIfInfected': (KalturaEnumsFactory.createInt, "KalturaVirusFoundAction"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVirusScanProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaVirusScanProfile")
        kparams.addStringIfDefined("name", self.name)
        kparams.addIntEnumIfDefined("status", self.status)
        kparams.addStringEnumIfDefined("engineType", self.engineType)
        kparams.addObjectIfDefined("entryFilter", self.entryFilter)
        kparams.addIntEnumIfDefined("actionIfInfected", self.actionIfInfected)
        return kparams

    def getId(self):
        return self.id

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getPartnerId(self):
        return self.partnerId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getEngineType(self):
        return self.engineType

    def setEngineType(self, newEngineType):
        self.engineType = newEngineType

    def getEntryFilter(self):
        return self.entryFilter

    def setEntryFilter(self, newEntryFilter):
        self.entryFilter = newEntryFilter

    def getActionIfInfected(self):
        return self.actionIfInfected

    def setActionIfInfected(self, newActionIfInfected):
        self.actionIfInfected = newActionIfInfected


class KalturaVirusScanProfileListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaVirusScanProfile
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaVirusScanProfile), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVirusScanProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaVirusScanProfileListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


########## services ##########

class KalturaVirusScanProfileService(KalturaServiceBase):
    """Virus scan profile service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List virus scan profile objects by filter and pager"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("virusscan_virusscanprofile", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaVirusScanProfileListResponse)

    def add(self, virusScanProfile):
        """Allows you to add an virus scan profile object and virus scan profile content associated with Kaltura object"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("virusScanProfile", virusScanProfile)
        self.client.queueServiceActionCall("virusscan_virusscanprofile", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaVirusScanProfile)

    def get(self, virusScanProfileId):
        """Retrieve an virus scan profile object by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("virusScanProfileId", virusScanProfileId);
        self.client.queueServiceActionCall("virusscan_virusscanprofile", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaVirusScanProfile)

    def update(self, virusScanProfileId, virusScanProfile):
        """Update exisitng virus scan profile, it is possible to update the virus scan profile id too"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("virusScanProfileId", virusScanProfileId);
        kparams.addObjectIfDefined("virusScanProfile", virusScanProfile)
        self.client.queueServiceActionCall("virusscan_virusscanprofile", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaVirusScanProfile)

    def delete(self, virusScanProfileId):
        """Mark the virus scan profile as deleted"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("virusScanProfileId", virusScanProfileId);
        self.client.queueServiceActionCall("virusscan_virusscanprofile", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaVirusScanProfile)

    def scan(self, flavorAssetId, virusScanProfileId = NotImplemented):
        """Scan flavor asset according to virus scan profile"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("flavorAssetId", flavorAssetId)
        kparams.addIntIfDefined("virusScanProfileId", virusScanProfileId);
        self.client.queueServiceActionCall("virusscan_virusscanprofile", "scan", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

########## main ##########
class KalturaVirusScanClientPlugin(KalturaClientPlugin):
    # KalturaVirusScanClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaVirusScanClientPlugin
    @staticmethod
    def get(client):
        if KalturaVirusScanClientPlugin.instance == None:
            KalturaVirusScanClientPlugin.instance = KalturaVirusScanClientPlugin(client)
        return KalturaVirusScanClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'virusScanProfile': KalturaVirusScanProfileService,
        }

    def getEnums(self):
        return {
            'KalturaVirusFoundAction': KalturaVirusFoundAction,
            'KalturaVirusScanEngineType': KalturaVirusScanEngineType,
            'KalturaVirusScanProfileOrderBy': KalturaVirusScanProfileOrderBy,
            'KalturaVirusScanProfileStatus': KalturaVirusScanProfileStatus,
        }

    def getTypes(self):
        return {
            'KalturaVirusScanProfileBaseFilter': KalturaVirusScanProfileBaseFilter,
            'KalturaVirusScanProfileFilter': KalturaVirusScanProfileFilter,
            'KalturaVirusScanProfile': KalturaVirusScanProfile,
            'KalturaVirusScanProfileListResponse': KalturaVirusScanProfileListResponse,
        }

    # @return string
    def getName(self):
        return 'virusScan'


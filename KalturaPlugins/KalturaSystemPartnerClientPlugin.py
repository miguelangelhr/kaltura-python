import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
class KalturaSystemPartnerLimitType:
    ENTRIES = "ENTRIES"
    MONTHLY_STREAM_ENTRIES = "MONTHLY_STREAM_ENTRIES"
    MONTHLY_BANDWIDTH = "MONTHLY_BANDWIDTH"
    PUBLISHERS = "PUBLISHERS"
    ADMIN_LOGIN_USERS = "ADMIN_LOGIN_USERS"
    LOGIN_USERS = "LOGIN_USERS"
    USER_LOGIN_ATTEMPTS = "USER_LOGIN_ATTEMPTS"
    BULK_SIZE = "BULK_SIZE"
    MONTHLY_STORAGE = "MONTHLY_STORAGE"
    MONTHLY_STORAGE_AND_BANDWIDTH = "MONTHLY_STORAGE_AND_BANDWIDTH"
    END_USERS = "END_USERS"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaSystemPartnerUsageFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            fromDate=NotImplemented,
            toDate=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # Date range from
        # @var int
        self.fromDate = fromDate

        # Date range to
        # @var int
        self.toDate = toDate


    PROPERTY_LOADERS = {
        'fromDate': getXmlNodeInt, 
        'toDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerUsageFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerUsageFilter")
        kparams.addIntIfDefined("fromDate", self.fromDate)
        kparams.addIntIfDefined("toDate", self.toDate)
        return kparams

    def getFromDate(self):
        return self.fromDate

    def setFromDate(self, newFromDate):
        self.fromDate = newFromDate

    def getToDate(self):
        return self.toDate

    def setToDate(self, newToDate):
        self.toDate = newToDate


class KalturaSystemPartnerUsageItem(KalturaObjectBase):
    def __init__(self,
            partnerId=NotImplemented,
            partnerName=NotImplemented,
            partnerStatus=NotImplemented,
            partnerPackage=NotImplemented,
            partnerCreatedAt=NotImplemented,
            views=NotImplemented,
            plays=NotImplemented,
            entriesCount=NotImplemented,
            totalEntriesCount=NotImplemented,
            videoEntriesCount=NotImplemented,
            imageEntriesCount=NotImplemented,
            audioEntriesCount=NotImplemented,
            mixEntriesCount=NotImplemented,
            bandwidth=NotImplemented,
            totalStorage=NotImplemented,
            storage=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Partner ID
        # @var int
        self.partnerId = partnerId

        # Partner name
        # @var string
        self.partnerName = partnerName

        # Partner status
        # @var KalturaPartnerStatus
        self.partnerStatus = partnerStatus

        # Partner package
        # @var int
        self.partnerPackage = partnerPackage

        # Partner creation date (Unix timestamp)
        # @var int
        self.partnerCreatedAt = partnerCreatedAt

        # Number of player loads in the specific date range
        # @var int
        self.views = views

        # Number of plays in the specific date range
        # @var int
        self.plays = plays

        # Number of new entries created during specific date range
        # @var int
        self.entriesCount = entriesCount

        # Total number of entries
        # @var int
        self.totalEntriesCount = totalEntriesCount

        # Number of new video entries created during specific date range
        # @var int
        self.videoEntriesCount = videoEntriesCount

        # Number of new image entries created during specific date range
        # @var int
        self.imageEntriesCount = imageEntriesCount

        # Number of new audio entries created during specific date range
        # @var int
        self.audioEntriesCount = audioEntriesCount

        # Number of new mix entries created during specific date range
        # @var int
        self.mixEntriesCount = mixEntriesCount

        # The total bandwidth usage during the given date range (in MB)
        # @var float
        self.bandwidth = bandwidth

        # The total storage consumption (in MB)
        # @var float
        self.totalStorage = totalStorage

        # The change in storage consumption (new uploads) during the given date range (in MB)
        # @var float
        self.storage = storage


    PROPERTY_LOADERS = {
        'partnerId': getXmlNodeInt, 
        'partnerName': getXmlNodeText, 
        'partnerStatus': (KalturaEnumsFactory.createInt, "KalturaPartnerStatus"), 
        'partnerPackage': getXmlNodeInt, 
        'partnerCreatedAt': getXmlNodeInt, 
        'views': getXmlNodeInt, 
        'plays': getXmlNodeInt, 
        'entriesCount': getXmlNodeInt, 
        'totalEntriesCount': getXmlNodeInt, 
        'videoEntriesCount': getXmlNodeInt, 
        'imageEntriesCount': getXmlNodeInt, 
        'audioEntriesCount': getXmlNodeInt, 
        'mixEntriesCount': getXmlNodeInt, 
        'bandwidth': getXmlNodeFloat, 
        'totalStorage': getXmlNodeFloat, 
        'storage': getXmlNodeFloat, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerUsageItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerUsageItem")
        kparams.addIntIfDefined("partnerId", self.partnerId)
        kparams.addStringIfDefined("partnerName", self.partnerName)
        kparams.addIntEnumIfDefined("partnerStatus", self.partnerStatus)
        kparams.addIntIfDefined("partnerPackage", self.partnerPackage)
        kparams.addIntIfDefined("partnerCreatedAt", self.partnerCreatedAt)
        kparams.addIntIfDefined("views", self.views)
        kparams.addIntIfDefined("plays", self.plays)
        kparams.addIntIfDefined("entriesCount", self.entriesCount)
        kparams.addIntIfDefined("totalEntriesCount", self.totalEntriesCount)
        kparams.addIntIfDefined("videoEntriesCount", self.videoEntriesCount)
        kparams.addIntIfDefined("imageEntriesCount", self.imageEntriesCount)
        kparams.addIntIfDefined("audioEntriesCount", self.audioEntriesCount)
        kparams.addIntIfDefined("mixEntriesCount", self.mixEntriesCount)
        kparams.addFloatIfDefined("bandwidth", self.bandwidth)
        kparams.addFloatIfDefined("totalStorage", self.totalStorage)
        kparams.addFloatIfDefined("storage", self.storage)
        return kparams

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getPartnerName(self):
        return self.partnerName

    def setPartnerName(self, newPartnerName):
        self.partnerName = newPartnerName

    def getPartnerStatus(self):
        return self.partnerStatus

    def setPartnerStatus(self, newPartnerStatus):
        self.partnerStatus = newPartnerStatus

    def getPartnerPackage(self):
        return self.partnerPackage

    def setPartnerPackage(self, newPartnerPackage):
        self.partnerPackage = newPartnerPackage

    def getPartnerCreatedAt(self):
        return self.partnerCreatedAt

    def setPartnerCreatedAt(self, newPartnerCreatedAt):
        self.partnerCreatedAt = newPartnerCreatedAt

    def getViews(self):
        return self.views

    def setViews(self, newViews):
        self.views = newViews

    def getPlays(self):
        return self.plays

    def setPlays(self, newPlays):
        self.plays = newPlays

    def getEntriesCount(self):
        return self.entriesCount

    def setEntriesCount(self, newEntriesCount):
        self.entriesCount = newEntriesCount

    def getTotalEntriesCount(self):
        return self.totalEntriesCount

    def setTotalEntriesCount(self, newTotalEntriesCount):
        self.totalEntriesCount = newTotalEntriesCount

    def getVideoEntriesCount(self):
        return self.videoEntriesCount

    def setVideoEntriesCount(self, newVideoEntriesCount):
        self.videoEntriesCount = newVideoEntriesCount

    def getImageEntriesCount(self):
        return self.imageEntriesCount

    def setImageEntriesCount(self, newImageEntriesCount):
        self.imageEntriesCount = newImageEntriesCount

    def getAudioEntriesCount(self):
        return self.audioEntriesCount

    def setAudioEntriesCount(self, newAudioEntriesCount):
        self.audioEntriesCount = newAudioEntriesCount

    def getMixEntriesCount(self):
        return self.mixEntriesCount

    def setMixEntriesCount(self, newMixEntriesCount):
        self.mixEntriesCount = newMixEntriesCount

    def getBandwidth(self):
        return self.bandwidth

    def setBandwidth(self, newBandwidth):
        self.bandwidth = newBandwidth

    def getTotalStorage(self):
        return self.totalStorage

    def setTotalStorage(self, newTotalStorage):
        self.totalStorage = newTotalStorage

    def getStorage(self):
        return self.storage

    def setStorage(self, newStorage):
        self.storage = newStorage


class KalturaSystemPartnerUsageListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaSystemPartnerUsageItem
        self.objects = objects

        # @var int
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaSystemPartnerUsageItem), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerUsageListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerUsageListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        kparams.addIntIfDefined("totalCount", self.totalCount)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects

    def getTotalCount(self):
        return self.totalCount

    def setTotalCount(self, newTotalCount):
        self.totalCount = newTotalCount


class KalturaSystemPartnerLimit(KalturaObjectBase):
    def __init__(self,
            type=NotImplemented,
            max=NotImplemented,
            overagePrice=NotImplemented,
            overageUnit=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var KalturaSystemPartnerLimitType
        self.type = type

        # @var float
        self.max = max

        # @var float
        self.overagePrice = overagePrice

        # @var float
        self.overageUnit = overageUnit


    PROPERTY_LOADERS = {
        'type': (KalturaEnumsFactory.createString, "KalturaSystemPartnerLimitType"), 
        'max': getXmlNodeFloat, 
        'overagePrice': getXmlNodeFloat, 
        'overageUnit': getXmlNodeFloat, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerLimit.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerLimit")
        kparams.addStringEnumIfDefined("type", self.type)
        kparams.addFloatIfDefined("max", self.max)
        kparams.addFloatIfDefined("overagePrice", self.overagePrice)
        kparams.addFloatIfDefined("overageUnit", self.overageUnit)
        return kparams

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getMax(self):
        return self.max

    def setMax(self, newMax):
        self.max = newMax

    def getOveragePrice(self):
        return self.overagePrice

    def setOveragePrice(self, newOveragePrice):
        self.overagePrice = newOveragePrice

    def getOverageUnit(self):
        return self.overageUnit

    def setOverageUnit(self, newOverageUnit):
        self.overageUnit = newOverageUnit


class KalturaSystemPartnerConfiguration(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            partnerName=NotImplemented,
            description=NotImplemented,
            adminName=NotImplemented,
            adminEmail=NotImplemented,
            host=NotImplemented,
            cdnHost=NotImplemented,
            partnerPackage=NotImplemented,
            monitorUsage=NotImplemented,
            moderateContent=NotImplemented,
            rtmpUrl=NotImplemented,
            storageDeleteFromKaltura=NotImplemented,
            storageServePriority=NotImplemented,
            kmcVersion=NotImplemented,
            restrictThumbnailByKs=NotImplemented,
            defThumbOffset=NotImplemented,
            defThumbDensity=NotImplemented,
            userSessionRoleId=NotImplemented,
            adminSessionRoleId=NotImplemented,
            alwaysAllowedPermissionNames=NotImplemented,
            importRemoteSourceForConvert=NotImplemented,
            permissions=NotImplemented,
            notificationsConfig=NotImplemented,
            allowMultiNotification=NotImplemented,
            loginBlockPeriod=NotImplemented,
            numPrevPassToKeep=NotImplemented,
            passReplaceFreq=NotImplemented,
            isFirstLogin=NotImplemented,
            partnerGroupType=NotImplemented,
            partnerParentId=NotImplemented,
            limits=NotImplemented,
            streamerType=NotImplemented,
            mediaProtocol=NotImplemented,
            extendedFreeTrailExpiryReason=NotImplemented,
            extendedFreeTrailExpiryDate=NotImplemented,
            extendedFreeTrail=NotImplemented,
            crmId=NotImplemented,
            crmLink=NotImplemented,
            verticalClasiffication=NotImplemented,
            partnerPackageClassOfService=NotImplemented,
            enableBulkUploadNotificationsEmails=NotImplemented,
            deliveryRestrictions=NotImplemented,
            bulkUploadNotificationsEmail=NotImplemented,
            internalUse=NotImplemented,
            autoModerateEntryFilter=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var string
        self.partnerName = partnerName

        # @var string
        self.description = description

        # @var string
        self.adminName = adminName

        # @var string
        self.adminEmail = adminEmail

        # @var string
        self.host = host

        # @var string
        self.cdnHost = cdnHost

        # @var int
        self.partnerPackage = partnerPackage

        # @var int
        self.monitorUsage = monitorUsage

        # @var bool
        self.moderateContent = moderateContent

        # @var string
        self.rtmpUrl = rtmpUrl

        # @var bool
        self.storageDeleteFromKaltura = storageDeleteFromKaltura

        # @var KalturaStorageServePriority
        self.storageServePriority = storageServePriority

        # @var int
        self.kmcVersion = kmcVersion

        # @var int
        self.restrictThumbnailByKs = restrictThumbnailByKs

        # @var int
        self.defThumbOffset = defThumbOffset

        # @var int
        self.defThumbDensity = defThumbDensity

        # @var int
        self.userSessionRoleId = userSessionRoleId

        # @var int
        self.adminSessionRoleId = adminSessionRoleId

        # @var string
        self.alwaysAllowedPermissionNames = alwaysAllowedPermissionNames

        # @var bool
        self.importRemoteSourceForConvert = importRemoteSourceForConvert

        # @var array of KalturaPermission
        self.permissions = permissions

        # @var string
        self.notificationsConfig = notificationsConfig

        # @var bool
        self.allowMultiNotification = allowMultiNotification

        # @var int
        self.loginBlockPeriod = loginBlockPeriod

        # @var int
        self.numPrevPassToKeep = numPrevPassToKeep

        # @var int
        self.passReplaceFreq = passReplaceFreq

        # @var bool
        self.isFirstLogin = isFirstLogin

        # @var KalturaPartnerGroupType
        self.partnerGroupType = partnerGroupType

        # @var int
        self.partnerParentId = partnerParentId

        # @var array of KalturaSystemPartnerLimit
        self.limits = limits

        # http/rtmp/hdnetwork
        # @var string
        self.streamerType = streamerType

        # http/https, rtmp/rtmpe
        # @var string
        self.mediaProtocol = mediaProtocol

        # @var string
        self.extendedFreeTrailExpiryReason = extendedFreeTrailExpiryReason

        # Unix timestamp (In seconds)
        # @var int
        self.extendedFreeTrailExpiryDate = extendedFreeTrailExpiryDate

        # @var int
        self.extendedFreeTrail = extendedFreeTrail

        # @var string
        self.crmId = crmId

        # @var string
        self.crmLink = crmLink

        # @var string
        self.verticalClasiffication = verticalClasiffication

        # @var string
        self.partnerPackageClassOfService = partnerPackageClassOfService

        # @var bool
        self.enableBulkUploadNotificationsEmails = enableBulkUploadNotificationsEmails

        # @var string
        self.deliveryRestrictions = deliveryRestrictions

        # @var string
        self.bulkUploadNotificationsEmail = bulkUploadNotificationsEmail

        # @var bool
        self.internalUse = internalUse

        # @var KalturaBaseEntryFilter
        self.autoModerateEntryFilter = autoModerateEntryFilter


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerName': getXmlNodeText, 
        'description': getXmlNodeText, 
        'adminName': getXmlNodeText, 
        'adminEmail': getXmlNodeText, 
        'host': getXmlNodeText, 
        'cdnHost': getXmlNodeText, 
        'partnerPackage': getXmlNodeInt, 
        'monitorUsage': getXmlNodeInt, 
        'moderateContent': getXmlNodeBool, 
        'rtmpUrl': getXmlNodeText, 
        'storageDeleteFromKaltura': getXmlNodeBool, 
        'storageServePriority': (KalturaEnumsFactory.createInt, "KalturaStorageServePriority"), 
        'kmcVersion': getXmlNodeInt, 
        'restrictThumbnailByKs': getXmlNodeInt, 
        'defThumbOffset': getXmlNodeInt, 
        'defThumbDensity': getXmlNodeInt, 
        'userSessionRoleId': getXmlNodeInt, 
        'adminSessionRoleId': getXmlNodeInt, 
        'alwaysAllowedPermissionNames': getXmlNodeText, 
        'importRemoteSourceForConvert': getXmlNodeBool, 
        'permissions': (KalturaObjectFactory.createArray, KalturaPermission), 
        'notificationsConfig': getXmlNodeText, 
        'allowMultiNotification': getXmlNodeBool, 
        'loginBlockPeriod': getXmlNodeInt, 
        'numPrevPassToKeep': getXmlNodeInt, 
        'passReplaceFreq': getXmlNodeInt, 
        'isFirstLogin': getXmlNodeBool, 
        'partnerGroupType': (KalturaEnumsFactory.createInt, "KalturaPartnerGroupType"), 
        'partnerParentId': getXmlNodeInt, 
        'limits': (KalturaObjectFactory.createArray, KalturaSystemPartnerLimit), 
        'streamerType': getXmlNodeText, 
        'mediaProtocol': getXmlNodeText, 
        'extendedFreeTrailExpiryReason': getXmlNodeText, 
        'extendedFreeTrailExpiryDate': getXmlNodeInt, 
        'extendedFreeTrail': getXmlNodeInt, 
        'crmId': getXmlNodeText, 
        'crmLink': getXmlNodeText, 
        'verticalClasiffication': getXmlNodeText, 
        'partnerPackageClassOfService': getXmlNodeText, 
        'enableBulkUploadNotificationsEmails': getXmlNodeBool, 
        'deliveryRestrictions': getXmlNodeText, 
        'bulkUploadNotificationsEmail': getXmlNodeText, 
        'internalUse': getXmlNodeBool, 
        'autoModerateEntryFilter': (KalturaObjectFactory.create, KalturaBaseEntryFilter), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerConfiguration.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerConfiguration")
        kparams.addStringIfDefined("partnerName", self.partnerName)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringIfDefined("adminName", self.adminName)
        kparams.addStringIfDefined("adminEmail", self.adminEmail)
        kparams.addStringIfDefined("host", self.host)
        kparams.addStringIfDefined("cdnHost", self.cdnHost)
        kparams.addIntIfDefined("partnerPackage", self.partnerPackage)
        kparams.addIntIfDefined("monitorUsage", self.monitorUsage)
        kparams.addBoolIfDefined("moderateContent", self.moderateContent)
        kparams.addStringIfDefined("rtmpUrl", self.rtmpUrl)
        kparams.addBoolIfDefined("storageDeleteFromKaltura", self.storageDeleteFromKaltura)
        kparams.addIntEnumIfDefined("storageServePriority", self.storageServePriority)
        kparams.addIntIfDefined("kmcVersion", self.kmcVersion)
        kparams.addIntIfDefined("restrictThumbnailByKs", self.restrictThumbnailByKs)
        kparams.addIntIfDefined("defThumbOffset", self.defThumbOffset)
        kparams.addIntIfDefined("defThumbDensity", self.defThumbDensity)
        kparams.addIntIfDefined("userSessionRoleId", self.userSessionRoleId)
        kparams.addIntIfDefined("adminSessionRoleId", self.adminSessionRoleId)
        kparams.addStringIfDefined("alwaysAllowedPermissionNames", self.alwaysAllowedPermissionNames)
        kparams.addBoolIfDefined("importRemoteSourceForConvert", self.importRemoteSourceForConvert)
        kparams.addArrayIfDefined("permissions", self.permissions)
        kparams.addStringIfDefined("notificationsConfig", self.notificationsConfig)
        kparams.addBoolIfDefined("allowMultiNotification", self.allowMultiNotification)
        kparams.addIntIfDefined("loginBlockPeriod", self.loginBlockPeriod)
        kparams.addIntIfDefined("numPrevPassToKeep", self.numPrevPassToKeep)
        kparams.addIntIfDefined("passReplaceFreq", self.passReplaceFreq)
        kparams.addBoolIfDefined("isFirstLogin", self.isFirstLogin)
        kparams.addIntEnumIfDefined("partnerGroupType", self.partnerGroupType)
        kparams.addIntIfDefined("partnerParentId", self.partnerParentId)
        kparams.addArrayIfDefined("limits", self.limits)
        kparams.addStringIfDefined("streamerType", self.streamerType)
        kparams.addStringIfDefined("mediaProtocol", self.mediaProtocol)
        kparams.addStringIfDefined("extendedFreeTrailExpiryReason", self.extendedFreeTrailExpiryReason)
        kparams.addIntIfDefined("extendedFreeTrailExpiryDate", self.extendedFreeTrailExpiryDate)
        kparams.addIntIfDefined("extendedFreeTrail", self.extendedFreeTrail)
        kparams.addStringIfDefined("crmId", self.crmId)
        kparams.addStringIfDefined("crmLink", self.crmLink)
        kparams.addStringIfDefined("verticalClasiffication", self.verticalClasiffication)
        kparams.addStringIfDefined("partnerPackageClassOfService", self.partnerPackageClassOfService)
        kparams.addBoolIfDefined("enableBulkUploadNotificationsEmails", self.enableBulkUploadNotificationsEmails)
        kparams.addStringIfDefined("deliveryRestrictions", self.deliveryRestrictions)
        kparams.addStringIfDefined("bulkUploadNotificationsEmail", self.bulkUploadNotificationsEmail)
        kparams.addBoolIfDefined("internalUse", self.internalUse)
        kparams.addObjectIfDefined("autoModerateEntryFilter", self.autoModerateEntryFilter)
        return kparams

    def getId(self):
        return self.id

    def getPartnerName(self):
        return self.partnerName

    def setPartnerName(self, newPartnerName):
        self.partnerName = newPartnerName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getAdminName(self):
        return self.adminName

    def setAdminName(self, newAdminName):
        self.adminName = newAdminName

    def getAdminEmail(self):
        return self.adminEmail

    def setAdminEmail(self, newAdminEmail):
        self.adminEmail = newAdminEmail

    def getHost(self):
        return self.host

    def setHost(self, newHost):
        self.host = newHost

    def getCdnHost(self):
        return self.cdnHost

    def setCdnHost(self, newCdnHost):
        self.cdnHost = newCdnHost

    def getPartnerPackage(self):
        return self.partnerPackage

    def setPartnerPackage(self, newPartnerPackage):
        self.partnerPackage = newPartnerPackage

    def getMonitorUsage(self):
        return self.monitorUsage

    def setMonitorUsage(self, newMonitorUsage):
        self.monitorUsage = newMonitorUsage

    def getModerateContent(self):
        return self.moderateContent

    def setModerateContent(self, newModerateContent):
        self.moderateContent = newModerateContent

    def getRtmpUrl(self):
        return self.rtmpUrl

    def setRtmpUrl(self, newRtmpUrl):
        self.rtmpUrl = newRtmpUrl

    def getStorageDeleteFromKaltura(self):
        return self.storageDeleteFromKaltura

    def setStorageDeleteFromKaltura(self, newStorageDeleteFromKaltura):
        self.storageDeleteFromKaltura = newStorageDeleteFromKaltura

    def getStorageServePriority(self):
        return self.storageServePriority

    def setStorageServePriority(self, newStorageServePriority):
        self.storageServePriority = newStorageServePriority

    def getKmcVersion(self):
        return self.kmcVersion

    def setKmcVersion(self, newKmcVersion):
        self.kmcVersion = newKmcVersion

    def getRestrictThumbnailByKs(self):
        return self.restrictThumbnailByKs

    def setRestrictThumbnailByKs(self, newRestrictThumbnailByKs):
        self.restrictThumbnailByKs = newRestrictThumbnailByKs

    def getDefThumbOffset(self):
        return self.defThumbOffset

    def setDefThumbOffset(self, newDefThumbOffset):
        self.defThumbOffset = newDefThumbOffset

    def getDefThumbDensity(self):
        return self.defThumbDensity

    def setDefThumbDensity(self, newDefThumbDensity):
        self.defThumbDensity = newDefThumbDensity

    def getUserSessionRoleId(self):
        return self.userSessionRoleId

    def setUserSessionRoleId(self, newUserSessionRoleId):
        self.userSessionRoleId = newUserSessionRoleId

    def getAdminSessionRoleId(self):
        return self.adminSessionRoleId

    def setAdminSessionRoleId(self, newAdminSessionRoleId):
        self.adminSessionRoleId = newAdminSessionRoleId

    def getAlwaysAllowedPermissionNames(self):
        return self.alwaysAllowedPermissionNames

    def setAlwaysAllowedPermissionNames(self, newAlwaysAllowedPermissionNames):
        self.alwaysAllowedPermissionNames = newAlwaysAllowedPermissionNames

    def getImportRemoteSourceForConvert(self):
        return self.importRemoteSourceForConvert

    def setImportRemoteSourceForConvert(self, newImportRemoteSourceForConvert):
        self.importRemoteSourceForConvert = newImportRemoteSourceForConvert

    def getPermissions(self):
        return self.permissions

    def setPermissions(self, newPermissions):
        self.permissions = newPermissions

    def getNotificationsConfig(self):
        return self.notificationsConfig

    def setNotificationsConfig(self, newNotificationsConfig):
        self.notificationsConfig = newNotificationsConfig

    def getAllowMultiNotification(self):
        return self.allowMultiNotification

    def setAllowMultiNotification(self, newAllowMultiNotification):
        self.allowMultiNotification = newAllowMultiNotification

    def getLoginBlockPeriod(self):
        return self.loginBlockPeriod

    def setLoginBlockPeriod(self, newLoginBlockPeriod):
        self.loginBlockPeriod = newLoginBlockPeriod

    def getNumPrevPassToKeep(self):
        return self.numPrevPassToKeep

    def setNumPrevPassToKeep(self, newNumPrevPassToKeep):
        self.numPrevPassToKeep = newNumPrevPassToKeep

    def getPassReplaceFreq(self):
        return self.passReplaceFreq

    def setPassReplaceFreq(self, newPassReplaceFreq):
        self.passReplaceFreq = newPassReplaceFreq

    def getIsFirstLogin(self):
        return self.isFirstLogin

    def setIsFirstLogin(self, newIsFirstLogin):
        self.isFirstLogin = newIsFirstLogin

    def getPartnerGroupType(self):
        return self.partnerGroupType

    def setPartnerGroupType(self, newPartnerGroupType):
        self.partnerGroupType = newPartnerGroupType

    def getPartnerParentId(self):
        return self.partnerParentId

    def setPartnerParentId(self, newPartnerParentId):
        self.partnerParentId = newPartnerParentId

    def getLimits(self):
        return self.limits

    def setLimits(self, newLimits):
        self.limits = newLimits

    def getStreamerType(self):
        return self.streamerType

    def setStreamerType(self, newStreamerType):
        self.streamerType = newStreamerType

    def getMediaProtocol(self):
        return self.mediaProtocol

    def setMediaProtocol(self, newMediaProtocol):
        self.mediaProtocol = newMediaProtocol

    def getExtendedFreeTrailExpiryReason(self):
        return self.extendedFreeTrailExpiryReason

    def setExtendedFreeTrailExpiryReason(self, newExtendedFreeTrailExpiryReason):
        self.extendedFreeTrailExpiryReason = newExtendedFreeTrailExpiryReason

    def getExtendedFreeTrailExpiryDate(self):
        return self.extendedFreeTrailExpiryDate

    def setExtendedFreeTrailExpiryDate(self, newExtendedFreeTrailExpiryDate):
        self.extendedFreeTrailExpiryDate = newExtendedFreeTrailExpiryDate

    def getExtendedFreeTrail(self):
        return self.extendedFreeTrail

    def setExtendedFreeTrail(self, newExtendedFreeTrail):
        self.extendedFreeTrail = newExtendedFreeTrail

    def getCrmId(self):
        return self.crmId

    def setCrmId(self, newCrmId):
        self.crmId = newCrmId

    def getCrmLink(self):
        return self.crmLink

    def setCrmLink(self, newCrmLink):
        self.crmLink = newCrmLink

    def getVerticalClasiffication(self):
        return self.verticalClasiffication

    def setVerticalClasiffication(self, newVerticalClasiffication):
        self.verticalClasiffication = newVerticalClasiffication

    def getPartnerPackageClassOfService(self):
        return self.partnerPackageClassOfService

    def setPartnerPackageClassOfService(self, newPartnerPackageClassOfService):
        self.partnerPackageClassOfService = newPartnerPackageClassOfService

    def getEnableBulkUploadNotificationsEmails(self):
        return self.enableBulkUploadNotificationsEmails

    def setEnableBulkUploadNotificationsEmails(self, newEnableBulkUploadNotificationsEmails):
        self.enableBulkUploadNotificationsEmails = newEnableBulkUploadNotificationsEmails

    def getDeliveryRestrictions(self):
        return self.deliveryRestrictions

    def setDeliveryRestrictions(self, newDeliveryRestrictions):
        self.deliveryRestrictions = newDeliveryRestrictions

    def getBulkUploadNotificationsEmail(self):
        return self.bulkUploadNotificationsEmail

    def setBulkUploadNotificationsEmail(self, newBulkUploadNotificationsEmail):
        self.bulkUploadNotificationsEmail = newBulkUploadNotificationsEmail

    def getInternalUse(self):
        return self.internalUse

    def setInternalUse(self, newInternalUse):
        self.internalUse = newInternalUse

    def getAutoModerateEntryFilter(self):
        return self.autoModerateEntryFilter

    def setAutoModerateEntryFilter(self, newAutoModerateEntryFilter):
        self.autoModerateEntryFilter = newAutoModerateEntryFilter


class KalturaSystemPartnerPackage(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        self.id = id

        # @var string
        self.name = name


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerPackage.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerPackage")
        kparams.addIntIfDefined("id", self.id)
        kparams.addStringIfDefined("name", self.name)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName


########## services ##########

class KalturaSystemPartnerService(KalturaServiceBase):
    """System partner service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, partnerId):
        """Retrieve all info about partner
        This service gets partner id as parameter and accessable to the admin console partner only"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        self.client.queueServiceActionCall("systempartner_systempartner", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPartner)

    def getUsage(self, partnerFilter = NotImplemented, usageFilter = NotImplemented, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("partnerFilter", partnerFilter)
        kparams.addObjectIfDefined("usageFilter", usageFilter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("systempartner_systempartner", "getUsage", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSystemPartnerUsageListResponse)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("systempartner_systempartner", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPartnerListResponse)

    def updateStatus(self, partnerId, status):
        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addIntIfDefined("status", status);
        self.client.queueServiceActionCall("systempartner_systempartner", "updateStatus", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def getAdminSession(self, partnerId, userId = NotImplemented):
        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addStringIfDefined("userId", userId)
        self.client.queueServiceActionCall("systempartner_systempartner", "getAdminSession", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def updateConfiguration(self, partnerId, configuration):
        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addObjectIfDefined("configuration", configuration)
        self.client.queueServiceActionCall("systempartner_systempartner", "updateConfiguration", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def getConfiguration(self, partnerId):
        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        self.client.queueServiceActionCall("systempartner_systempartner", "getConfiguration", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSystemPartnerConfiguration)

    def getPackages(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("systempartner_systempartner", "getPackages", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaSystemPartnerPackage)

    def getPackagesClassOfService(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("systempartner_systempartner", "getPackagesClassOfService", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaSystemPartnerPackage)

    def getPackagesVertical(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("systempartner_systempartner", "getPackagesVertical", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaSystemPartnerPackage)

    def resetUserPassword(self, userId, partnerId, newPassword):
        kparams = KalturaParams()
        kparams.addStringIfDefined("userId", userId)
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addStringIfDefined("newPassword", newPassword)
        self.client.queueServiceActionCall("systempartner_systempartner", "resetUserPassword", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def listUserLoginData(self, filter = NotImplemented, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("systempartner_systempartner", "listUserLoginData", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserLoginDataListResponse)

########## main ##########
class KalturaSystemPartnerClientPlugin(KalturaClientPlugin):
    # KalturaSystemPartnerClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaSystemPartnerClientPlugin
    @staticmethod
    def get(client):
        if KalturaSystemPartnerClientPlugin.instance == None:
            KalturaSystemPartnerClientPlugin.instance = KalturaSystemPartnerClientPlugin(client)
        return KalturaSystemPartnerClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'systemPartner': KalturaSystemPartnerService,
        }

    def getEnums(self):
        return {
            'KalturaSystemPartnerLimitType': KalturaSystemPartnerLimitType,
        }

    def getTypes(self):
        return {
            'KalturaSystemPartnerUsageFilter': KalturaSystemPartnerUsageFilter,
            'KalturaSystemPartnerUsageItem': KalturaSystemPartnerUsageItem,
            'KalturaSystemPartnerUsageListResponse': KalturaSystemPartnerUsageListResponse,
            'KalturaSystemPartnerLimit': KalturaSystemPartnerLimit,
            'KalturaSystemPartnerConfiguration': KalturaSystemPartnerConfiguration,
            'KalturaSystemPartnerPackage': KalturaSystemPartnerPackage,
        }

    # @return string
    def getName(self):
        return 'systemPartner'


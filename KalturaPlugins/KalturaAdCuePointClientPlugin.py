import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaCuePointClientPlugin import *
from KalturaClientBase import *

########## enums ##########
class KalturaAdCuePointOrderBy:
    END_TIME_ASC = "+endTime"
    END_TIME_DESC = "-endTime"
    DURATION_ASC = "+duration"
    DURATION_DESC = "-duration"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    START_TIME_ASC = "+startTime"
    START_TIME_DESC = "-startTime"
    PARTNER_SORT_VALUE_ASC = "+partnerSortValue"
    PARTNER_SORT_VALUE_DESC = "-partnerSortValue"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAdProtocolType:
    CUSTOM = "0"
    VAST = "1"
    VAST_2_0 = "2"
    VPAID = "3"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAdType:
    VIDEO = "1"
    OVERLAY = "2"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaAdCuePointBaseFilter(KalturaCuePointFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            cuePointTypeEqual=NotImplemented,
            cuePointTypeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            entryIdEqual=NotImplemented,
            entryIdIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            startTimeGreaterThanOrEqual=NotImplemented,
            startTimeLessThanOrEqual=NotImplemented,
            userIdEqual=NotImplemented,
            userIdIn=NotImplemented,
            partnerSortValueEqual=NotImplemented,
            partnerSortValueIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            forceStopEqual=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            protocolTypeEqual=NotImplemented,
            protocolTypeIn=NotImplemented,
            titleLike=NotImplemented,
            titleMultiLikeOr=NotImplemented,
            titleMultiLikeAnd=NotImplemented,
            endTimeGreaterThanOrEqual=NotImplemented,
            endTimeLessThanOrEqual=NotImplemented,
            durationGreaterThanOrEqual=NotImplemented,
            durationLessThanOrEqual=NotImplemented):
        KalturaCuePointFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            cuePointTypeEqual,
            cuePointTypeIn,
            statusEqual,
            statusIn,
            entryIdEqual,
            entryIdIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            startTimeGreaterThanOrEqual,
            startTimeLessThanOrEqual,
            userIdEqual,
            userIdIn,
            partnerSortValueEqual,
            partnerSortValueIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            forceStopEqual,
            systemNameEqual,
            systemNameIn)

        # @var KalturaAdProtocolType
        self.protocolTypeEqual = protocolTypeEqual

        # @var string
        self.protocolTypeIn = protocolTypeIn

        # @var string
        self.titleLike = titleLike

        # @var string
        self.titleMultiLikeOr = titleMultiLikeOr

        # @var string
        self.titleMultiLikeAnd = titleMultiLikeAnd

        # @var int
        self.endTimeGreaterThanOrEqual = endTimeGreaterThanOrEqual

        # @var int
        self.endTimeLessThanOrEqual = endTimeLessThanOrEqual

        # @var int
        self.durationGreaterThanOrEqual = durationGreaterThanOrEqual

        # @var int
        self.durationLessThanOrEqual = durationLessThanOrEqual


    PROPERTY_LOADERS = {
        'protocolTypeEqual': (KalturaEnumsFactory.createString, "KalturaAdProtocolType"), 
        'protocolTypeIn': getXmlNodeText, 
        'titleLike': getXmlNodeText, 
        'titleMultiLikeOr': getXmlNodeText, 
        'titleMultiLikeAnd': getXmlNodeText, 
        'endTimeGreaterThanOrEqual': getXmlNodeInt, 
        'endTimeLessThanOrEqual': getXmlNodeInt, 
        'durationGreaterThanOrEqual': getXmlNodeInt, 
        'durationLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaCuePointFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAdCuePointBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCuePointFilter.toParams(self)
        kparams.put("objectType", "KalturaAdCuePointBaseFilter")
        kparams.addStringEnumIfDefined("protocolTypeEqual", self.protocolTypeEqual)
        kparams.addStringIfDefined("protocolTypeIn", self.protocolTypeIn)
        kparams.addStringIfDefined("titleLike", self.titleLike)
        kparams.addStringIfDefined("titleMultiLikeOr", self.titleMultiLikeOr)
        kparams.addStringIfDefined("titleMultiLikeAnd", self.titleMultiLikeAnd)
        kparams.addIntIfDefined("endTimeGreaterThanOrEqual", self.endTimeGreaterThanOrEqual)
        kparams.addIntIfDefined("endTimeLessThanOrEqual", self.endTimeLessThanOrEqual)
        kparams.addIntIfDefined("durationGreaterThanOrEqual", self.durationGreaterThanOrEqual)
        kparams.addIntIfDefined("durationLessThanOrEqual", self.durationLessThanOrEqual)
        return kparams

    def getProtocolTypeEqual(self):
        return self.protocolTypeEqual

    def setProtocolTypeEqual(self, newProtocolTypeEqual):
        self.protocolTypeEqual = newProtocolTypeEqual

    def getProtocolTypeIn(self):
        return self.protocolTypeIn

    def setProtocolTypeIn(self, newProtocolTypeIn):
        self.protocolTypeIn = newProtocolTypeIn

    def getTitleLike(self):
        return self.titleLike

    def setTitleLike(self, newTitleLike):
        self.titleLike = newTitleLike

    def getTitleMultiLikeOr(self):
        return self.titleMultiLikeOr

    def setTitleMultiLikeOr(self, newTitleMultiLikeOr):
        self.titleMultiLikeOr = newTitleMultiLikeOr

    def getTitleMultiLikeAnd(self):
        return self.titleMultiLikeAnd

    def setTitleMultiLikeAnd(self, newTitleMultiLikeAnd):
        self.titleMultiLikeAnd = newTitleMultiLikeAnd

    def getEndTimeGreaterThanOrEqual(self):
        return self.endTimeGreaterThanOrEqual

    def setEndTimeGreaterThanOrEqual(self, newEndTimeGreaterThanOrEqual):
        self.endTimeGreaterThanOrEqual = newEndTimeGreaterThanOrEqual

    def getEndTimeLessThanOrEqual(self):
        return self.endTimeLessThanOrEqual

    def setEndTimeLessThanOrEqual(self, newEndTimeLessThanOrEqual):
        self.endTimeLessThanOrEqual = newEndTimeLessThanOrEqual

    def getDurationGreaterThanOrEqual(self):
        return self.durationGreaterThanOrEqual

    def setDurationGreaterThanOrEqual(self, newDurationGreaterThanOrEqual):
        self.durationGreaterThanOrEqual = newDurationGreaterThanOrEqual

    def getDurationLessThanOrEqual(self):
        return self.durationLessThanOrEqual

    def setDurationLessThanOrEqual(self, newDurationLessThanOrEqual):
        self.durationLessThanOrEqual = newDurationLessThanOrEqual


class KalturaAdCuePointFilter(KalturaAdCuePointBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            cuePointTypeEqual=NotImplemented,
            cuePointTypeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            entryIdEqual=NotImplemented,
            entryIdIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            startTimeGreaterThanOrEqual=NotImplemented,
            startTimeLessThanOrEqual=NotImplemented,
            userIdEqual=NotImplemented,
            userIdIn=NotImplemented,
            partnerSortValueEqual=NotImplemented,
            partnerSortValueIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            forceStopEqual=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            protocolTypeEqual=NotImplemented,
            protocolTypeIn=NotImplemented,
            titleLike=NotImplemented,
            titleMultiLikeOr=NotImplemented,
            titleMultiLikeAnd=NotImplemented,
            endTimeGreaterThanOrEqual=NotImplemented,
            endTimeLessThanOrEqual=NotImplemented,
            durationGreaterThanOrEqual=NotImplemented,
            durationLessThanOrEqual=NotImplemented):
        KalturaAdCuePointBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            cuePointTypeEqual,
            cuePointTypeIn,
            statusEqual,
            statusIn,
            entryIdEqual,
            entryIdIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            startTimeGreaterThanOrEqual,
            startTimeLessThanOrEqual,
            userIdEqual,
            userIdIn,
            partnerSortValueEqual,
            partnerSortValueIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            forceStopEqual,
            systemNameEqual,
            systemNameIn,
            protocolTypeEqual,
            protocolTypeIn,
            titleLike,
            titleMultiLikeOr,
            titleMultiLikeAnd,
            endTimeGreaterThanOrEqual,
            endTimeLessThanOrEqual,
            durationGreaterThanOrEqual,
            durationLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAdCuePointBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAdCuePointFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAdCuePointBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaAdCuePointFilter")
        return kparams


class KalturaAdCuePoint(KalturaCuePoint):
    def __init__(self,
            id=NotImplemented,
            cuePointType=NotImplemented,
            status=NotImplemented,
            entryId=NotImplemented,
            partnerId=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            tags=NotImplemented,
            startTime=NotImplemented,
            userId=NotImplemented,
            partnerData=NotImplemented,
            partnerSortValue=NotImplemented,
            forceStop=NotImplemented,
            thumbOffset=NotImplemented,
            systemName=NotImplemented,
            protocolType=NotImplemented,
            sourceUrl=NotImplemented,
            adType=NotImplemented,
            title=NotImplemented,
            endTime=NotImplemented,
            duration=NotImplemented):
        KalturaCuePoint.__init__(self,
            id,
            cuePointType,
            status,
            entryId,
            partnerId,
            createdAt,
            updatedAt,
            tags,
            startTime,
            userId,
            partnerData,
            partnerSortValue,
            forceStop,
            thumbOffset,
            systemName)

        # @var KalturaAdProtocolType
        # @insertonly
        self.protocolType = protocolType

        # @var string
        self.sourceUrl = sourceUrl

        # @var KalturaAdType
        self.adType = adType

        # @var string
        self.title = title

        # @var int
        self.endTime = endTime

        # Duration in milliseconds
        # @var int
        # @readonly
        self.duration = duration


    PROPERTY_LOADERS = {
        'protocolType': (KalturaEnumsFactory.createString, "KalturaAdProtocolType"), 
        'sourceUrl': getXmlNodeText, 
        'adType': (KalturaEnumsFactory.createString, "KalturaAdType"), 
        'title': getXmlNodeText, 
        'endTime': getXmlNodeInt, 
        'duration': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaCuePoint.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAdCuePoint.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCuePoint.toParams(self)
        kparams.put("objectType", "KalturaAdCuePoint")
        kparams.addStringEnumIfDefined("protocolType", self.protocolType)
        kparams.addStringIfDefined("sourceUrl", self.sourceUrl)
        kparams.addStringEnumIfDefined("adType", self.adType)
        kparams.addStringIfDefined("title", self.title)
        kparams.addIntIfDefined("endTime", self.endTime)
        return kparams

    def getProtocolType(self):
        return self.protocolType

    def setProtocolType(self, newProtocolType):
        self.protocolType = newProtocolType

    def getSourceUrl(self):
        return self.sourceUrl

    def setSourceUrl(self, newSourceUrl):
        self.sourceUrl = newSourceUrl

    def getAdType(self):
        return self.adType

    def setAdType(self, newAdType):
        self.adType = newAdType

    def getTitle(self):
        return self.title

    def setTitle(self, newTitle):
        self.title = newTitle

    def getEndTime(self):
        return self.endTime

    def setEndTime(self, newEndTime):
        self.endTime = newEndTime

    def getDuration(self):
        return self.duration


########## services ##########
########## main ##########
class KalturaAdCuePointClientPlugin(KalturaClientPlugin):
    # KalturaAdCuePointClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaAdCuePointClientPlugin
    @staticmethod
    def get(client):
        if KalturaAdCuePointClientPlugin.instance == None:
            KalturaAdCuePointClientPlugin.instance = KalturaAdCuePointClientPlugin(client)
        return KalturaAdCuePointClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaAdCuePointOrderBy': KalturaAdCuePointOrderBy,
            'KalturaAdProtocolType': KalturaAdProtocolType,
            'KalturaAdType': KalturaAdType,
        }

    def getTypes(self):
        return {
            'KalturaAdCuePointBaseFilter': KalturaAdCuePointBaseFilter,
            'KalturaAdCuePointFilter': KalturaAdCuePointFilter,
            'KalturaAdCuePoint': KalturaAdCuePoint,
        }

    # @return string
    def getName(self):
        return 'adCuePoint'


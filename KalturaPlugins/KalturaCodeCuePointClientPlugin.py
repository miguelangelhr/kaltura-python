import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaCuePointClientPlugin import *
from KalturaClientBase import *

########## enums ##########
class KalturaCodeCuePointOrderBy:
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

########## classes ##########
class KalturaCodeCuePointBaseFilter(KalturaCuePointFilter):
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
            codeLike=NotImplemented,
            codeMultiLikeOr=NotImplemented,
            codeMultiLikeAnd=NotImplemented,
            codeEqual=NotImplemented,
            codeIn=NotImplemented,
            descriptionLike=NotImplemented,
            descriptionMultiLikeOr=NotImplemented,
            descriptionMultiLikeAnd=NotImplemented):
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

        # @var string
        self.codeLike = codeLike

        # @var string
        self.codeMultiLikeOr = codeMultiLikeOr

        # @var string
        self.codeMultiLikeAnd = codeMultiLikeAnd

        # @var string
        self.codeEqual = codeEqual

        # @var string
        self.codeIn = codeIn

        # @var string
        self.descriptionLike = descriptionLike

        # @var string
        self.descriptionMultiLikeOr = descriptionMultiLikeOr

        # @var string
        self.descriptionMultiLikeAnd = descriptionMultiLikeAnd


    PROPERTY_LOADERS = {
        'codeLike': getXmlNodeText, 
        'codeMultiLikeOr': getXmlNodeText, 
        'codeMultiLikeAnd': getXmlNodeText, 
        'codeEqual': getXmlNodeText, 
        'codeIn': getXmlNodeText, 
        'descriptionLike': getXmlNodeText, 
        'descriptionMultiLikeOr': getXmlNodeText, 
        'descriptionMultiLikeAnd': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaCuePointFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCodeCuePointBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCuePointFilter.toParams(self)
        kparams.put("objectType", "KalturaCodeCuePointBaseFilter")
        kparams.addStringIfDefined("codeLike", self.codeLike)
        kparams.addStringIfDefined("codeMultiLikeOr", self.codeMultiLikeOr)
        kparams.addStringIfDefined("codeMultiLikeAnd", self.codeMultiLikeAnd)
        kparams.addStringIfDefined("codeEqual", self.codeEqual)
        kparams.addStringIfDefined("codeIn", self.codeIn)
        kparams.addStringIfDefined("descriptionLike", self.descriptionLike)
        kparams.addStringIfDefined("descriptionMultiLikeOr", self.descriptionMultiLikeOr)
        kparams.addStringIfDefined("descriptionMultiLikeAnd", self.descriptionMultiLikeAnd)
        return kparams

    def getCodeLike(self):
        return self.codeLike

    def setCodeLike(self, newCodeLike):
        self.codeLike = newCodeLike

    def getCodeMultiLikeOr(self):
        return self.codeMultiLikeOr

    def setCodeMultiLikeOr(self, newCodeMultiLikeOr):
        self.codeMultiLikeOr = newCodeMultiLikeOr

    def getCodeMultiLikeAnd(self):
        return self.codeMultiLikeAnd

    def setCodeMultiLikeAnd(self, newCodeMultiLikeAnd):
        self.codeMultiLikeAnd = newCodeMultiLikeAnd

    def getCodeEqual(self):
        return self.codeEqual

    def setCodeEqual(self, newCodeEqual):
        self.codeEqual = newCodeEqual

    def getCodeIn(self):
        return self.codeIn

    def setCodeIn(self, newCodeIn):
        self.codeIn = newCodeIn

    def getDescriptionLike(self):
        return self.descriptionLike

    def setDescriptionLike(self, newDescriptionLike):
        self.descriptionLike = newDescriptionLike

    def getDescriptionMultiLikeOr(self):
        return self.descriptionMultiLikeOr

    def setDescriptionMultiLikeOr(self, newDescriptionMultiLikeOr):
        self.descriptionMultiLikeOr = newDescriptionMultiLikeOr

    def getDescriptionMultiLikeAnd(self):
        return self.descriptionMultiLikeAnd

    def setDescriptionMultiLikeAnd(self, newDescriptionMultiLikeAnd):
        self.descriptionMultiLikeAnd = newDescriptionMultiLikeAnd


class KalturaCodeCuePointFilter(KalturaCodeCuePointBaseFilter):
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
            codeLike=NotImplemented,
            codeMultiLikeOr=NotImplemented,
            codeMultiLikeAnd=NotImplemented,
            codeEqual=NotImplemented,
            codeIn=NotImplemented,
            descriptionLike=NotImplemented,
            descriptionMultiLikeOr=NotImplemented,
            descriptionMultiLikeAnd=NotImplemented):
        KalturaCodeCuePointBaseFilter.__init__(self,
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
            codeLike,
            codeMultiLikeOr,
            codeMultiLikeAnd,
            codeEqual,
            codeIn,
            descriptionLike,
            descriptionMultiLikeOr,
            descriptionMultiLikeAnd)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaCodeCuePointBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCodeCuePointFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCodeCuePointBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaCodeCuePointFilter")
        return kparams


class KalturaCodeCuePoint(KalturaCuePoint):
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
            code=NotImplemented,
            description=NotImplemented):
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

        # @var string
        self.code = code

        # @var string
        self.description = description


    PROPERTY_LOADERS = {
        'code': getXmlNodeText, 
        'description': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaCuePoint.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCodeCuePoint.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCuePoint.toParams(self)
        kparams.put("objectType", "KalturaCodeCuePoint")
        kparams.addStringIfDefined("code", self.code)
        kparams.addStringIfDefined("description", self.description)
        return kparams

    def getCode(self):
        return self.code

    def setCode(self, newCode):
        self.code = newCode

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription


########## services ##########
########## main ##########
class KalturaCodeCuePointClientPlugin(KalturaClientPlugin):
    # KalturaCodeCuePointClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaCodeCuePointClientPlugin
    @staticmethod
    def get(client):
        if KalturaCodeCuePointClientPlugin.instance == None:
            KalturaCodeCuePointClientPlugin.instance = KalturaCodeCuePointClientPlugin(client)
        return KalturaCodeCuePointClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaCodeCuePointOrderBy': KalturaCodeCuePointOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaCodeCuePointBaseFilter': KalturaCodeCuePointBaseFilter,
            'KalturaCodeCuePointFilter': KalturaCodeCuePointFilter,
            'KalturaCodeCuePoint': KalturaCodeCuePoint,
        }

    # @return string
    def getName(self):
        return 'codeCuePoint'


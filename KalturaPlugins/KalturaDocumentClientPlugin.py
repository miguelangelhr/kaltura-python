import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
class KalturaDocumentEntryOrderBy:
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    MODERATION_COUNT_ASC = "+moderationCount"
    MODERATION_COUNT_DESC = "-moderationCount"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    RANK_ASC = "+rank"
    RANK_DESC = "-rank"
    START_DATE_ASC = "+startDate"
    START_DATE_DESC = "-startDate"
    END_DATE_ASC = "+endDate"
    END_DATE_DESC = "-endDate"
    PARTNER_SORT_VALUE_ASC = "+partnerSortValue"
    PARTNER_SORT_VALUE_DESC = "-partnerSortValue"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDocumentFlavorParamsOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDocumentFlavorParamsOutputOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDocumentType:
    DOCUMENT = 11
    SWF = 12
    PDF = 13

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPdfFlavorParamsOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPdfFlavorParamsOutputOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSwfFlavorParamsOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSwfFlavorParamsOutputOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaDocumentEntry(KalturaBaseEntry):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            partnerId=NotImplemented,
            userId=NotImplemented,
            tags=NotImplemented,
            adminTags=NotImplemented,
            categories=NotImplemented,
            categoriesIds=NotImplemented,
            status=NotImplemented,
            moderationStatus=NotImplemented,
            moderationCount=NotImplemented,
            type=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            rank=NotImplemented,
            totalRank=NotImplemented,
            votes=NotImplemented,
            groupId=NotImplemented,
            partnerData=NotImplemented,
            downloadUrl=NotImplemented,
            searchText=NotImplemented,
            licenseType=NotImplemented,
            version=NotImplemented,
            thumbnailUrl=NotImplemented,
            accessControlId=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            referenceId=NotImplemented,
            replacingEntryId=NotImplemented,
            replacedEntryId=NotImplemented,
            replacementStatus=NotImplemented,
            partnerSortValue=NotImplemented,
            conversionProfileId=NotImplemented,
            rootEntryId=NotImplemented,
            operationAttributes=NotImplemented,
            documentType=NotImplemented,
            assetParamsIds=NotImplemented):
        KalturaBaseEntry.__init__(self,
            id,
            name,
            description,
            partnerId,
            userId,
            tags,
            adminTags,
            categories,
            categoriesIds,
            status,
            moderationStatus,
            moderationCount,
            type,
            createdAt,
            updatedAt,
            rank,
            totalRank,
            votes,
            groupId,
            partnerData,
            downloadUrl,
            searchText,
            licenseType,
            version,
            thumbnailUrl,
            accessControlId,
            startDate,
            endDate,
            referenceId,
            replacingEntryId,
            replacedEntryId,
            replacementStatus,
            partnerSortValue,
            conversionProfileId,
            rootEntryId,
            operationAttributes)

        # The type of the document
        # @var KalturaDocumentType
        # @insertonly
        self.documentType = documentType

        # Comma separated asset params ids that exists for this media entry
        # @var string
        # @readonly
        self.assetParamsIds = assetParamsIds


    PROPERTY_LOADERS = {
        'documentType': (KalturaEnumsFactory.createInt, "KalturaDocumentType"), 
        'assetParamsIds': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDocumentEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntry.toParams(self)
        kparams.put("objectType", "KalturaDocumentEntry")
        kparams.addIntEnumIfDefined("documentType", self.documentType)
        return kparams

    def getDocumentType(self):
        return self.documentType

    def setDocumentType(self, newDocumentType):
        self.documentType = newDocumentType

    def getAssetParamsIds(self):
        return self.assetParamsIds


class KalturaDocumentEntryBaseFilter(KalturaBaseEntryFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented,
            documentTypeEqual=NotImplemented,
            documentTypeIn=NotImplemented,
            assetParamsIdsMatchOr=NotImplemented,
            assetParamsIdsMatchAnd=NotImplemented):
        KalturaBaseEntryFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            freeText,
            isRoot)

        # @var KalturaDocumentType
        self.documentTypeEqual = documentTypeEqual

        # @var string
        self.documentTypeIn = documentTypeIn

        # @var string
        self.assetParamsIdsMatchOr = assetParamsIdsMatchOr

        # @var string
        self.assetParamsIdsMatchAnd = assetParamsIdsMatchAnd


    PROPERTY_LOADERS = {
        'documentTypeEqual': (KalturaEnumsFactory.createInt, "KalturaDocumentType"), 
        'documentTypeIn': getXmlNodeText, 
        'assetParamsIdsMatchOr': getXmlNodeText, 
        'assetParamsIdsMatchAnd': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDocumentEntryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaDocumentEntryBaseFilter")
        kparams.addIntEnumIfDefined("documentTypeEqual", self.documentTypeEqual)
        kparams.addStringIfDefined("documentTypeIn", self.documentTypeIn)
        kparams.addStringIfDefined("assetParamsIdsMatchOr", self.assetParamsIdsMatchOr)
        kparams.addStringIfDefined("assetParamsIdsMatchAnd", self.assetParamsIdsMatchAnd)
        return kparams

    def getDocumentTypeEqual(self):
        return self.documentTypeEqual

    def setDocumentTypeEqual(self, newDocumentTypeEqual):
        self.documentTypeEqual = newDocumentTypeEqual

    def getDocumentTypeIn(self):
        return self.documentTypeIn

    def setDocumentTypeIn(self, newDocumentTypeIn):
        self.documentTypeIn = newDocumentTypeIn

    def getAssetParamsIdsMatchOr(self):
        return self.assetParamsIdsMatchOr

    def setAssetParamsIdsMatchOr(self, newAssetParamsIdsMatchOr):
        self.assetParamsIdsMatchOr = newAssetParamsIdsMatchOr

    def getAssetParamsIdsMatchAnd(self):
        return self.assetParamsIdsMatchAnd

    def setAssetParamsIdsMatchAnd(self, newAssetParamsIdsMatchAnd):
        self.assetParamsIdsMatchAnd = newAssetParamsIdsMatchAnd


class KalturaDocumentEntryFilter(KalturaDocumentEntryBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented,
            documentTypeEqual=NotImplemented,
            documentTypeIn=NotImplemented,
            assetParamsIdsMatchOr=NotImplemented,
            assetParamsIdsMatchAnd=NotImplemented):
        KalturaDocumentEntryBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            freeText,
            isRoot,
            documentTypeEqual,
            documentTypeIn,
            assetParamsIdsMatchOr,
            assetParamsIdsMatchAnd)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDocumentEntryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDocumentEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDocumentEntryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaDocumentEntryFilter")
        return kparams


class KalturaDocumentListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaDocumentEntry
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaDocumentEntry), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDocumentListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDocumentListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaDocumentFlavorParamsBaseFilter(KalturaFlavorParamsFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented):
        KalturaFlavorParamsFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDocumentFlavorParamsBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsFilter.toParams(self)
        kparams.put("objectType", "KalturaDocumentFlavorParamsBaseFilter")
        return kparams


class KalturaDocumentFlavorParamsOutputBaseFilter(KalturaFlavorParamsOutputFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented,
            flavorParamsIdEqual=NotImplemented,
            flavorParamsVersionEqual=NotImplemented,
            flavorAssetIdEqual=NotImplemented,
            flavorAssetVersionEqual=NotImplemented):
        KalturaFlavorParamsOutputFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual,
            flavorParamsIdEqual,
            flavorParamsVersionEqual,
            flavorAssetIdEqual,
            flavorAssetVersionEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsOutputFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDocumentFlavorParamsOutputBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsOutputFilter.toParams(self)
        kparams.put("objectType", "KalturaDocumentFlavorParamsOutputBaseFilter")
        return kparams


class KalturaPdfFlavorParamsBaseFilter(KalturaFlavorParamsFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented):
        KalturaFlavorParamsFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPdfFlavorParamsBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsFilter.toParams(self)
        kparams.put("objectType", "KalturaPdfFlavorParamsBaseFilter")
        return kparams


class KalturaPdfFlavorParamsOutputBaseFilter(KalturaFlavorParamsOutputFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented,
            flavorParamsIdEqual=NotImplemented,
            flavorParamsVersionEqual=NotImplemented,
            flavorAssetIdEqual=NotImplemented,
            flavorAssetVersionEqual=NotImplemented):
        KalturaFlavorParamsOutputFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual,
            flavorParamsIdEqual,
            flavorParamsVersionEqual,
            flavorAssetIdEqual,
            flavorAssetVersionEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsOutputFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPdfFlavorParamsOutputBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsOutputFilter.toParams(self)
        kparams.put("objectType", "KalturaPdfFlavorParamsOutputBaseFilter")
        return kparams


class KalturaSwfFlavorParamsBaseFilter(KalturaFlavorParamsFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented):
        KalturaFlavorParamsFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSwfFlavorParamsBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsFilter.toParams(self)
        kparams.put("objectType", "KalturaSwfFlavorParamsBaseFilter")
        return kparams


class KalturaSwfFlavorParamsOutputBaseFilter(KalturaFlavorParamsOutputFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented,
            flavorParamsIdEqual=NotImplemented,
            flavorParamsVersionEqual=NotImplemented,
            flavorAssetIdEqual=NotImplemented,
            flavorAssetVersionEqual=NotImplemented):
        KalturaFlavorParamsOutputFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual,
            flavorParamsIdEqual,
            flavorParamsVersionEqual,
            flavorAssetIdEqual,
            flavorAssetVersionEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsOutputFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSwfFlavorParamsOutputBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsOutputFilter.toParams(self)
        kparams.put("objectType", "KalturaSwfFlavorParamsOutputBaseFilter")
        return kparams


class KalturaDocumentFlavorParamsFilter(KalturaDocumentFlavorParamsBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented):
        KalturaDocumentFlavorParamsBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDocumentFlavorParamsBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDocumentFlavorParamsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDocumentFlavorParamsBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaDocumentFlavorParamsFilter")
        return kparams


class KalturaDocumentFlavorParamsOutputFilter(KalturaDocumentFlavorParamsOutputBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented,
            flavorParamsIdEqual=NotImplemented,
            flavorParamsVersionEqual=NotImplemented,
            flavorAssetIdEqual=NotImplemented,
            flavorAssetVersionEqual=NotImplemented):
        KalturaDocumentFlavorParamsOutputBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual,
            flavorParamsIdEqual,
            flavorParamsVersionEqual,
            flavorAssetIdEqual,
            flavorAssetVersionEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDocumentFlavorParamsOutputBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDocumentFlavorParamsOutputFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDocumentFlavorParamsOutputBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaDocumentFlavorParamsOutputFilter")
        return kparams


class KalturaPdfFlavorParamsFilter(KalturaPdfFlavorParamsBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented):
        KalturaPdfFlavorParamsBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPdfFlavorParamsBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPdfFlavorParamsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPdfFlavorParamsBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaPdfFlavorParamsFilter")
        return kparams


class KalturaPdfFlavorParamsOutputFilter(KalturaPdfFlavorParamsOutputBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented,
            flavorParamsIdEqual=NotImplemented,
            flavorParamsVersionEqual=NotImplemented,
            flavorAssetIdEqual=NotImplemented,
            flavorAssetVersionEqual=NotImplemented):
        KalturaPdfFlavorParamsOutputBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual,
            flavorParamsIdEqual,
            flavorParamsVersionEqual,
            flavorAssetIdEqual,
            flavorAssetVersionEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPdfFlavorParamsOutputBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPdfFlavorParamsOutputFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPdfFlavorParamsOutputBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaPdfFlavorParamsOutputFilter")
        return kparams


class KalturaSwfFlavorParamsFilter(KalturaSwfFlavorParamsBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented):
        KalturaSwfFlavorParamsBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaSwfFlavorParamsBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSwfFlavorParamsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSwfFlavorParamsBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaSwfFlavorParamsFilter")
        return kparams


class KalturaSwfFlavorParamsOutputFilter(KalturaSwfFlavorParamsOutputBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented,
            flavorParamsIdEqual=NotImplemented,
            flavorParamsVersionEqual=NotImplemented,
            flavorAssetIdEqual=NotImplemented,
            flavorAssetVersionEqual=NotImplemented):
        KalturaSwfFlavorParamsOutputBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual,
            flavorParamsIdEqual,
            flavorParamsVersionEqual,
            flavorAssetIdEqual,
            flavorAssetVersionEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaSwfFlavorParamsOutputBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSwfFlavorParamsOutputFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSwfFlavorParamsOutputBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaSwfFlavorParamsOutputFilter")
        return kparams


class KalturaDocumentFlavorParamsOutput(KalturaFlavorParamsOutput):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isSystemDefault=NotImplemented,
            tags=NotImplemented,
            requiredPermissions=NotImplemented,
            videoCodec=NotImplemented,
            videoBitrate=NotImplemented,
            audioCodec=NotImplemented,
            audioBitrate=NotImplemented,
            audioChannels=NotImplemented,
            audioSampleRate=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            frameRate=NotImplemented,
            gopSize=NotImplemented,
            conversionEngines=NotImplemented,
            conversionEnginesExtraParams=NotImplemented,
            twoPass=NotImplemented,
            deinterlice=NotImplemented,
            rotate=NotImplemented,
            operators=NotImplemented,
            engineVersion=NotImplemented,
            format=NotImplemented,
            aspectRatioProcessingMode=NotImplemented,
            forceFrameToMultiplication16=NotImplemented,
            videoConstantBitrate=NotImplemented,
            videoBitrateTolerance=NotImplemented,
            flavorParamsId=NotImplemented,
            commandLinesStr=NotImplemented,
            flavorParamsVersion=NotImplemented,
            flavorAssetId=NotImplemented,
            flavorAssetVersion=NotImplemented,
            readyBehavior=NotImplemented):
        KalturaFlavorParamsOutput.__init__(self,
            id,
            partnerId,
            name,
            systemName,
            description,
            createdAt,
            isSystemDefault,
            tags,
            requiredPermissions,
            videoCodec,
            videoBitrate,
            audioCodec,
            audioBitrate,
            audioChannels,
            audioSampleRate,
            width,
            height,
            frameRate,
            gopSize,
            conversionEngines,
            conversionEnginesExtraParams,
            twoPass,
            deinterlice,
            rotate,
            operators,
            engineVersion,
            format,
            aspectRatioProcessingMode,
            forceFrameToMultiplication16,
            videoConstantBitrate,
            videoBitrateTolerance,
            flavorParamsId,
            commandLinesStr,
            flavorParamsVersion,
            flavorAssetId,
            flavorAssetVersion,
            readyBehavior)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsOutput.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDocumentFlavorParamsOutput.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsOutput.toParams(self)
        kparams.put("objectType", "KalturaDocumentFlavorParamsOutput")
        return kparams


class KalturaDocumentFlavorParams(KalturaFlavorParams):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isSystemDefault=NotImplemented,
            tags=NotImplemented,
            requiredPermissions=NotImplemented,
            videoCodec=NotImplemented,
            videoBitrate=NotImplemented,
            audioCodec=NotImplemented,
            audioBitrate=NotImplemented,
            audioChannels=NotImplemented,
            audioSampleRate=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            frameRate=NotImplemented,
            gopSize=NotImplemented,
            conversionEngines=NotImplemented,
            conversionEnginesExtraParams=NotImplemented,
            twoPass=NotImplemented,
            deinterlice=NotImplemented,
            rotate=NotImplemented,
            operators=NotImplemented,
            engineVersion=NotImplemented,
            format=NotImplemented,
            aspectRatioProcessingMode=NotImplemented,
            forceFrameToMultiplication16=NotImplemented,
            videoConstantBitrate=NotImplemented,
            videoBitrateTolerance=NotImplemented):
        KalturaFlavorParams.__init__(self,
            id,
            partnerId,
            name,
            systemName,
            description,
            createdAt,
            isSystemDefault,
            tags,
            requiredPermissions,
            videoCodec,
            videoBitrate,
            audioCodec,
            audioBitrate,
            audioChannels,
            audioSampleRate,
            width,
            height,
            frameRate,
            gopSize,
            conversionEngines,
            conversionEnginesExtraParams,
            twoPass,
            deinterlice,
            rotate,
            operators,
            engineVersion,
            format,
            aspectRatioProcessingMode,
            forceFrameToMultiplication16,
            videoConstantBitrate,
            videoBitrateTolerance)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDocumentFlavorParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParams.toParams(self)
        kparams.put("objectType", "KalturaDocumentFlavorParams")
        return kparams


class KalturaPdfFlavorParamsOutput(KalturaFlavorParamsOutput):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isSystemDefault=NotImplemented,
            tags=NotImplemented,
            requiredPermissions=NotImplemented,
            videoCodec=NotImplemented,
            videoBitrate=NotImplemented,
            audioCodec=NotImplemented,
            audioBitrate=NotImplemented,
            audioChannels=NotImplemented,
            audioSampleRate=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            frameRate=NotImplemented,
            gopSize=NotImplemented,
            conversionEngines=NotImplemented,
            conversionEnginesExtraParams=NotImplemented,
            twoPass=NotImplemented,
            deinterlice=NotImplemented,
            rotate=NotImplemented,
            operators=NotImplemented,
            engineVersion=NotImplemented,
            format=NotImplemented,
            aspectRatioProcessingMode=NotImplemented,
            forceFrameToMultiplication16=NotImplemented,
            videoConstantBitrate=NotImplemented,
            videoBitrateTolerance=NotImplemented,
            flavorParamsId=NotImplemented,
            commandLinesStr=NotImplemented,
            flavorParamsVersion=NotImplemented,
            flavorAssetId=NotImplemented,
            flavorAssetVersion=NotImplemented,
            readyBehavior=NotImplemented,
            readonly=NotImplemented):
        KalturaFlavorParamsOutput.__init__(self,
            id,
            partnerId,
            name,
            systemName,
            description,
            createdAt,
            isSystemDefault,
            tags,
            requiredPermissions,
            videoCodec,
            videoBitrate,
            audioCodec,
            audioBitrate,
            audioChannels,
            audioSampleRate,
            width,
            height,
            frameRate,
            gopSize,
            conversionEngines,
            conversionEnginesExtraParams,
            twoPass,
            deinterlice,
            rotate,
            operators,
            engineVersion,
            format,
            aspectRatioProcessingMode,
            forceFrameToMultiplication16,
            videoConstantBitrate,
            videoBitrateTolerance,
            flavorParamsId,
            commandLinesStr,
            flavorParamsVersion,
            flavorAssetId,
            flavorAssetVersion,
            readyBehavior)

        # @var bool
        self.readonly = readonly


    PROPERTY_LOADERS = {
        'readonly': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaFlavorParamsOutput.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPdfFlavorParamsOutput.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsOutput.toParams(self)
        kparams.put("objectType", "KalturaPdfFlavorParamsOutput")
        kparams.addBoolIfDefined("readonly", self.readonly)
        return kparams

    def getReadonly(self):
        return self.readonly

    def setReadonly(self, newReadonly):
        self.readonly = newReadonly


class KalturaPdfFlavorParams(KalturaFlavorParams):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isSystemDefault=NotImplemented,
            tags=NotImplemented,
            requiredPermissions=NotImplemented,
            videoCodec=NotImplemented,
            videoBitrate=NotImplemented,
            audioCodec=NotImplemented,
            audioBitrate=NotImplemented,
            audioChannels=NotImplemented,
            audioSampleRate=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            frameRate=NotImplemented,
            gopSize=NotImplemented,
            conversionEngines=NotImplemented,
            conversionEnginesExtraParams=NotImplemented,
            twoPass=NotImplemented,
            deinterlice=NotImplemented,
            rotate=NotImplemented,
            operators=NotImplemented,
            engineVersion=NotImplemented,
            format=NotImplemented,
            aspectRatioProcessingMode=NotImplemented,
            forceFrameToMultiplication16=NotImplemented,
            videoConstantBitrate=NotImplemented,
            videoBitrateTolerance=NotImplemented,
            readonly=NotImplemented):
        KalturaFlavorParams.__init__(self,
            id,
            partnerId,
            name,
            systemName,
            description,
            createdAt,
            isSystemDefault,
            tags,
            requiredPermissions,
            videoCodec,
            videoBitrate,
            audioCodec,
            audioBitrate,
            audioChannels,
            audioSampleRate,
            width,
            height,
            frameRate,
            gopSize,
            conversionEngines,
            conversionEnginesExtraParams,
            twoPass,
            deinterlice,
            rotate,
            operators,
            engineVersion,
            format,
            aspectRatioProcessingMode,
            forceFrameToMultiplication16,
            videoConstantBitrate,
            videoBitrateTolerance)

        # @var bool
        self.readonly = readonly


    PROPERTY_LOADERS = {
        'readonly': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaFlavorParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPdfFlavorParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParams.toParams(self)
        kparams.put("objectType", "KalturaPdfFlavorParams")
        kparams.addBoolIfDefined("readonly", self.readonly)
        return kparams

    def getReadonly(self):
        return self.readonly

    def setReadonly(self, newReadonly):
        self.readonly = newReadonly


class KalturaSwfFlavorParamsOutput(KalturaFlavorParamsOutput):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isSystemDefault=NotImplemented,
            tags=NotImplemented,
            requiredPermissions=NotImplemented,
            videoCodec=NotImplemented,
            videoBitrate=NotImplemented,
            audioCodec=NotImplemented,
            audioBitrate=NotImplemented,
            audioChannels=NotImplemented,
            audioSampleRate=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            frameRate=NotImplemented,
            gopSize=NotImplemented,
            conversionEngines=NotImplemented,
            conversionEnginesExtraParams=NotImplemented,
            twoPass=NotImplemented,
            deinterlice=NotImplemented,
            rotate=NotImplemented,
            operators=NotImplemented,
            engineVersion=NotImplemented,
            format=NotImplemented,
            aspectRatioProcessingMode=NotImplemented,
            forceFrameToMultiplication16=NotImplemented,
            videoConstantBitrate=NotImplemented,
            videoBitrateTolerance=NotImplemented,
            flavorParamsId=NotImplemented,
            commandLinesStr=NotImplemented,
            flavorParamsVersion=NotImplemented,
            flavorAssetId=NotImplemented,
            flavorAssetVersion=NotImplemented,
            readyBehavior=NotImplemented,
            flashVersion=NotImplemented,
            poly2Bitmap=NotImplemented):
        KalturaFlavorParamsOutput.__init__(self,
            id,
            partnerId,
            name,
            systemName,
            description,
            createdAt,
            isSystemDefault,
            tags,
            requiredPermissions,
            videoCodec,
            videoBitrate,
            audioCodec,
            audioBitrate,
            audioChannels,
            audioSampleRate,
            width,
            height,
            frameRate,
            gopSize,
            conversionEngines,
            conversionEnginesExtraParams,
            twoPass,
            deinterlice,
            rotate,
            operators,
            engineVersion,
            format,
            aspectRatioProcessingMode,
            forceFrameToMultiplication16,
            videoConstantBitrate,
            videoBitrateTolerance,
            flavorParamsId,
            commandLinesStr,
            flavorParamsVersion,
            flavorAssetId,
            flavorAssetVersion,
            readyBehavior)

        # @var int
        self.flashVersion = flashVersion

        # @var bool
        self.poly2Bitmap = poly2Bitmap


    PROPERTY_LOADERS = {
        'flashVersion': getXmlNodeInt, 
        'poly2Bitmap': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaFlavorParamsOutput.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSwfFlavorParamsOutput.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsOutput.toParams(self)
        kparams.put("objectType", "KalturaSwfFlavorParamsOutput")
        kparams.addIntIfDefined("flashVersion", self.flashVersion)
        kparams.addBoolIfDefined("poly2Bitmap", self.poly2Bitmap)
        return kparams

    def getFlashVersion(self):
        return self.flashVersion

    def setFlashVersion(self, newFlashVersion):
        self.flashVersion = newFlashVersion

    def getPoly2Bitmap(self):
        return self.poly2Bitmap

    def setPoly2Bitmap(self, newPoly2Bitmap):
        self.poly2Bitmap = newPoly2Bitmap


class KalturaSwfFlavorParams(KalturaFlavorParams):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isSystemDefault=NotImplemented,
            tags=NotImplemented,
            requiredPermissions=NotImplemented,
            videoCodec=NotImplemented,
            videoBitrate=NotImplemented,
            audioCodec=NotImplemented,
            audioBitrate=NotImplemented,
            audioChannels=NotImplemented,
            audioSampleRate=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            frameRate=NotImplemented,
            gopSize=NotImplemented,
            conversionEngines=NotImplemented,
            conversionEnginesExtraParams=NotImplemented,
            twoPass=NotImplemented,
            deinterlice=NotImplemented,
            rotate=NotImplemented,
            operators=NotImplemented,
            engineVersion=NotImplemented,
            format=NotImplemented,
            aspectRatioProcessingMode=NotImplemented,
            forceFrameToMultiplication16=NotImplemented,
            videoConstantBitrate=NotImplemented,
            videoBitrateTolerance=NotImplemented,
            flashVersion=NotImplemented,
            poly2Bitmap=NotImplemented):
        KalturaFlavorParams.__init__(self,
            id,
            partnerId,
            name,
            systemName,
            description,
            createdAt,
            isSystemDefault,
            tags,
            requiredPermissions,
            videoCodec,
            videoBitrate,
            audioCodec,
            audioBitrate,
            audioChannels,
            audioSampleRate,
            width,
            height,
            frameRate,
            gopSize,
            conversionEngines,
            conversionEnginesExtraParams,
            twoPass,
            deinterlice,
            rotate,
            operators,
            engineVersion,
            format,
            aspectRatioProcessingMode,
            forceFrameToMultiplication16,
            videoConstantBitrate,
            videoBitrateTolerance)

        # @var int
        self.flashVersion = flashVersion

        # @var bool
        self.poly2Bitmap = poly2Bitmap


    PROPERTY_LOADERS = {
        'flashVersion': getXmlNodeInt, 
        'poly2Bitmap': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaFlavorParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSwfFlavorParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParams.toParams(self)
        kparams.put("objectType", "KalturaSwfFlavorParams")
        kparams.addIntIfDefined("flashVersion", self.flashVersion)
        kparams.addBoolIfDefined("poly2Bitmap", self.poly2Bitmap)
        return kparams

    def getFlashVersion(self):
        return self.flashVersion

    def setFlashVersion(self, newFlashVersion):
        self.flashVersion = newFlashVersion

    def getPoly2Bitmap(self):
        return self.poly2Bitmap

    def setPoly2Bitmap(self, newPoly2Bitmap):
        self.poly2Bitmap = newPoly2Bitmap


########## services ##########

class KalturaDocumentsService(KalturaServiceBase):
    """Document service lets you upload and manage document files"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def addFromUploadedFile(self, documentEntry, uploadTokenId):
        """Add new document entry after the specific document file was uploaded and the upload token id exists"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("documentEntry", documentEntry)
        kparams.addStringIfDefined("uploadTokenId", uploadTokenId)
        self.client.queueServiceActionCall("document_documents", "addFromUploadedFile", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentEntry)

    def addFromEntry(self, sourceEntryId, documentEntry = NotImplemented, sourceFlavorParamsId = NotImplemented):
        """Copy entry into new entry"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("sourceEntryId", sourceEntryId)
        kparams.addObjectIfDefined("documentEntry", documentEntry)
        kparams.addIntIfDefined("sourceFlavorParamsId", sourceFlavorParamsId);
        self.client.queueServiceActionCall("document_documents", "addFromEntry", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentEntry)

    def addFromFlavorAsset(self, sourceFlavorAssetId, documentEntry = NotImplemented):
        """Copy flavor asset into new entry"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("sourceFlavorAssetId", sourceFlavorAssetId)
        kparams.addObjectIfDefined("documentEntry", documentEntry)
        self.client.queueServiceActionCall("document_documents", "addFromFlavorAsset", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentEntry)

    def convert(self, entryId, conversionProfileId = NotImplemented, dynamicConversionAttributes = NotImplemented):
        """Convert entry"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("conversionProfileId", conversionProfileId);
        kparams.addArrayIfDefined("dynamicConversionAttributes", dynamicConversionAttributes)
        self.client.queueServiceActionCall("document_documents", "convert", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def get(self, entryId, version = -1):
        """Get document entry by ID."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("version", version);
        self.client.queueServiceActionCall("document_documents", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentEntry)

    def update(self, entryId, documentEntry):
        """Update document entry. Only the properties that were set will be updated."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("documentEntry", documentEntry)
        self.client.queueServiceActionCall("document_documents", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentEntry)

    def delete(self, entryId):
        """Delete a document entry."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("document_documents", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List document entries by filter with paging support."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("document_documents", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentListResponse)

    def upload(self, fileData):
        """Upload a document file to Kaltura, then the file can be used to create a document entry.
        DEPRECATED - use upload.upload or uploadToken.add instead"""

        kparams = KalturaParams()
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData);
        self.client.queueServiceActionCall("document_documents", "upload", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def convertPptToSwf(self, entryId):
        """This will queue a batch job for converting the document file to swf
        Returns the URL where the new swf will be available"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("document_documents", "convertPptToSwf", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def serve(self, entryId, flavorAssetId = NotImplemented, forceProxy = False):
        """Serves the file content"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addStringIfDefined("flavorAssetId", flavorAssetId)
        kparams.addBoolIfDefined("forceProxy", forceProxy);
        self.client.queueServiceActionCall('document_documents', 'serve', kparams)
        return self.client.getServeUrl()

    def serveByFlavorParamsId(self, entryId, flavorParamsId = NotImplemented, forceProxy = False):
        """Serves the file content"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addStringIfDefined("flavorParamsId", flavorParamsId)
        kparams.addBoolIfDefined("forceProxy", forceProxy);
        self.client.queueServiceActionCall('document_documents', 'serveByFlavorParamsId', kparams)
        return self.client.getServeUrl()

########## main ##########
class KalturaDocumentClientPlugin(KalturaClientPlugin):
    # KalturaDocumentClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaDocumentClientPlugin
    @staticmethod
    def get(client):
        if KalturaDocumentClientPlugin.instance == None:
            KalturaDocumentClientPlugin.instance = KalturaDocumentClientPlugin(client)
        return KalturaDocumentClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'documents': KalturaDocumentsService,
        }

    def getEnums(self):
        return {
            'KalturaDocumentEntryOrderBy': KalturaDocumentEntryOrderBy,
            'KalturaDocumentFlavorParamsOrderBy': KalturaDocumentFlavorParamsOrderBy,
            'KalturaDocumentFlavorParamsOutputOrderBy': KalturaDocumentFlavorParamsOutputOrderBy,
            'KalturaDocumentType': KalturaDocumentType,
            'KalturaPdfFlavorParamsOrderBy': KalturaPdfFlavorParamsOrderBy,
            'KalturaPdfFlavorParamsOutputOrderBy': KalturaPdfFlavorParamsOutputOrderBy,
            'KalturaSwfFlavorParamsOrderBy': KalturaSwfFlavorParamsOrderBy,
            'KalturaSwfFlavorParamsOutputOrderBy': KalturaSwfFlavorParamsOutputOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaDocumentEntry': KalturaDocumentEntry,
            'KalturaDocumentEntryBaseFilter': KalturaDocumentEntryBaseFilter,
            'KalturaDocumentEntryFilter': KalturaDocumentEntryFilter,
            'KalturaDocumentListResponse': KalturaDocumentListResponse,
            'KalturaDocumentFlavorParamsBaseFilter': KalturaDocumentFlavorParamsBaseFilter,
            'KalturaDocumentFlavorParamsOutputBaseFilter': KalturaDocumentFlavorParamsOutputBaseFilter,
            'KalturaPdfFlavorParamsBaseFilter': KalturaPdfFlavorParamsBaseFilter,
            'KalturaPdfFlavorParamsOutputBaseFilter': KalturaPdfFlavorParamsOutputBaseFilter,
            'KalturaSwfFlavorParamsBaseFilter': KalturaSwfFlavorParamsBaseFilter,
            'KalturaSwfFlavorParamsOutputBaseFilter': KalturaSwfFlavorParamsOutputBaseFilter,
            'KalturaDocumentFlavorParamsFilter': KalturaDocumentFlavorParamsFilter,
            'KalturaDocumentFlavorParamsOutputFilter': KalturaDocumentFlavorParamsOutputFilter,
            'KalturaPdfFlavorParamsFilter': KalturaPdfFlavorParamsFilter,
            'KalturaPdfFlavorParamsOutputFilter': KalturaPdfFlavorParamsOutputFilter,
            'KalturaSwfFlavorParamsFilter': KalturaSwfFlavorParamsFilter,
            'KalturaSwfFlavorParamsOutputFilter': KalturaSwfFlavorParamsOutputFilter,
            'KalturaDocumentFlavorParamsOutput': KalturaDocumentFlavorParamsOutput,
            'KalturaDocumentFlavorParams': KalturaDocumentFlavorParams,
            'KalturaPdfFlavorParamsOutput': KalturaPdfFlavorParamsOutput,
            'KalturaPdfFlavorParams': KalturaPdfFlavorParams,
            'KalturaSwfFlavorParamsOutput': KalturaSwfFlavorParamsOutput,
            'KalturaSwfFlavorParams': KalturaSwfFlavorParams,
        }

    # @return string
    def getName(self):
        return 'document'


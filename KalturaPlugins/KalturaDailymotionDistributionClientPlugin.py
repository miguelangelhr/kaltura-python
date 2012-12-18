import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaContentDistributionClientPlugin import *
from KalturaClientBase import *

########## enums ##########
class KalturaDailymotionDistributionProfileOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDailymotionDistributionProviderOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaDailymotionDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented):
        KalturaConfigurableDistributionProfileFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaConfigurableDistributionProfileFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDailymotionDistributionProfileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionProfileFilter.toParams(self)
        kparams.put("objectType", "KalturaDailymotionDistributionProfileBaseFilter")
        return kparams


class KalturaDailymotionDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented):
        KalturaDistributionProviderFilter.__init__(self,
            orderBy,
            advancedSearch,
            typeEqual,
            typeIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDistributionProviderFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDailymotionDistributionProviderBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProviderFilter.toParams(self)
        kparams.put("objectType", "KalturaDailymotionDistributionProviderBaseFilter")
        return kparams


class KalturaDailymotionDistributionProfileFilter(KalturaDailymotionDistributionProfileBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented):
        KalturaDailymotionDistributionProfileBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDailymotionDistributionProfileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDailymotionDistributionProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDailymotionDistributionProfileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaDailymotionDistributionProfileFilter")
        return kparams


class KalturaDailymotionDistributionProviderFilter(KalturaDailymotionDistributionProviderBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented):
        KalturaDailymotionDistributionProviderBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            typeEqual,
            typeIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDailymotionDistributionProviderBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDailymotionDistributionProviderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDailymotionDistributionProviderBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaDailymotionDistributionProviderFilter")
        return kparams


class KalturaDailymotionDistributionProfile(KalturaConfigurableDistributionProfile):
    def __init__(self,
            id=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            partnerId=NotImplemented,
            providerType=NotImplemented,
            name=NotImplemented,
            status=NotImplemented,
            submitEnabled=NotImplemented,
            updateEnabled=NotImplemented,
            deleteEnabled=NotImplemented,
            reportEnabled=NotImplemented,
            autoCreateFlavors=NotImplemented,
            autoCreateThumb=NotImplemented,
            optionalFlavorParamsIds=NotImplemented,
            requiredFlavorParamsIds=NotImplemented,
            optionalThumbDimensions=NotImplemented,
            requiredThumbDimensions=NotImplemented,
            sunriseDefaultOffset=NotImplemented,
            sunsetDefaultOffset=NotImplemented,
            fieldConfigArray=NotImplemented,
            itemXpathsToExtend=NotImplemented,
            user=NotImplemented,
            password=NotImplemented):
        KalturaConfigurableDistributionProfile.__init__(self,
            id,
            createdAt,
            updatedAt,
            partnerId,
            providerType,
            name,
            status,
            submitEnabled,
            updateEnabled,
            deleteEnabled,
            reportEnabled,
            autoCreateFlavors,
            autoCreateThumb,
            optionalFlavorParamsIds,
            requiredFlavorParamsIds,
            optionalThumbDimensions,
            requiredThumbDimensions,
            sunriseDefaultOffset,
            sunsetDefaultOffset,
            fieldConfigArray,
            itemXpathsToExtend)

        # @var string
        self.user = user

        # @var string
        self.password = password


    PROPERTY_LOADERS = {
        'user': getXmlNodeText, 
        'password': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaConfigurableDistributionProfile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDailymotionDistributionProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionProfile.toParams(self)
        kparams.put("objectType", "KalturaDailymotionDistributionProfile")
        kparams.addStringIfDefined("user", self.user)
        kparams.addStringIfDefined("password", self.password)
        return kparams

    def getUser(self):
        return self.user

    def setUser(self, newUser):
        self.user = newUser

    def getPassword(self):
        return self.password

    def setPassword(self, newPassword):
        self.password = newPassword


class KalturaDailymotionDistributionProvider(KalturaDistributionProvider):
    def __init__(self,
            type=NotImplemented,
            name=NotImplemented,
            scheduleUpdateEnabled=NotImplemented,
            availabilityUpdateEnabled=NotImplemented,
            deleteInsteadUpdate=NotImplemented,
            intervalBeforeSunrise=NotImplemented,
            intervalBeforeSunset=NotImplemented,
            updateRequiredEntryFields=NotImplemented,
            updateRequiredMetadataXPaths=NotImplemented):
        KalturaDistributionProvider.__init__(self,
            type,
            name,
            scheduleUpdateEnabled,
            availabilityUpdateEnabled,
            deleteInsteadUpdate,
            intervalBeforeSunrise,
            intervalBeforeSunset,
            updateRequiredEntryFields,
            updateRequiredMetadataXPaths)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDistributionProvider.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDailymotionDistributionProvider.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProvider.toParams(self)
        kparams.put("objectType", "KalturaDailymotionDistributionProvider")
        return kparams


########## services ##########
########## main ##########
class KalturaDailymotionDistributionClientPlugin(KalturaClientPlugin):
    # KalturaDailymotionDistributionClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaDailymotionDistributionClientPlugin
    @staticmethod
    def get(client):
        if KalturaDailymotionDistributionClientPlugin.instance == None:
            KalturaDailymotionDistributionClientPlugin.instance = KalturaDailymotionDistributionClientPlugin(client)
        return KalturaDailymotionDistributionClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaDailymotionDistributionProfileOrderBy': KalturaDailymotionDistributionProfileOrderBy,
            'KalturaDailymotionDistributionProviderOrderBy': KalturaDailymotionDistributionProviderOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaDailymotionDistributionProfileBaseFilter': KalturaDailymotionDistributionProfileBaseFilter,
            'KalturaDailymotionDistributionProviderBaseFilter': KalturaDailymotionDistributionProviderBaseFilter,
            'KalturaDailymotionDistributionProfileFilter': KalturaDailymotionDistributionProfileFilter,
            'KalturaDailymotionDistributionProviderFilter': KalturaDailymotionDistributionProviderFilter,
            'KalturaDailymotionDistributionProfile': KalturaDailymotionDistributionProfile,
            'KalturaDailymotionDistributionProvider': KalturaDailymotionDistributionProvider,
        }

    # @return string
    def getName(self):
        return 'dailymotionDistribution'


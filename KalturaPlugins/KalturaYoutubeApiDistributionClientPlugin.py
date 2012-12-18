import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaContentDistributionClientPlugin import *
from KalturaClientBase import *

########## enums ##########
class KalturaYoutubeApiDistributionProfileOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaYoutubeApiDistributionProviderOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaYoutubeApiDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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
        self.fromXmlImpl(node, KalturaYoutubeApiDistributionProfileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionProfileFilter.toParams(self)
        kparams.put("objectType", "KalturaYoutubeApiDistributionProfileBaseFilter")
        return kparams


class KalturaYoutubeApiDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
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
        self.fromXmlImpl(node, KalturaYoutubeApiDistributionProviderBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProviderFilter.toParams(self)
        kparams.put("objectType", "KalturaYoutubeApiDistributionProviderBaseFilter")
        return kparams


class KalturaYoutubeApiDistributionProfileFilter(KalturaYoutubeApiDistributionProfileBaseFilter):
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
        KalturaYoutubeApiDistributionProfileBaseFilter.__init__(self,
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
        KalturaYoutubeApiDistributionProfileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaYoutubeApiDistributionProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaYoutubeApiDistributionProfileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaYoutubeApiDistributionProfileFilter")
        return kparams


class KalturaYoutubeApiDistributionProviderFilter(KalturaYoutubeApiDistributionProviderBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented):
        KalturaYoutubeApiDistributionProviderBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            typeEqual,
            typeIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaYoutubeApiDistributionProviderBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaYoutubeApiDistributionProviderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaYoutubeApiDistributionProviderBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaYoutubeApiDistributionProviderFilter")
        return kparams


class KalturaYoutubeApiDistributionProfile(KalturaConfigurableDistributionProfile):
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
            username=NotImplemented,
            password=NotImplemented,
            defaultCategory=NotImplemented,
            allowComments=NotImplemented,
            allowEmbedding=NotImplemented,
            allowRatings=NotImplemented,
            allowResponses=NotImplemented):
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
        self.username = username

        # @var string
        self.password = password

        # @var string
        self.defaultCategory = defaultCategory

        # @var string
        self.allowComments = allowComments

        # @var string
        self.allowEmbedding = allowEmbedding

        # @var string
        self.allowRatings = allowRatings

        # @var string
        self.allowResponses = allowResponses


    PROPERTY_LOADERS = {
        'username': getXmlNodeText, 
        'password': getXmlNodeText, 
        'defaultCategory': getXmlNodeText, 
        'allowComments': getXmlNodeText, 
        'allowEmbedding': getXmlNodeText, 
        'allowRatings': getXmlNodeText, 
        'allowResponses': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaConfigurableDistributionProfile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaYoutubeApiDistributionProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionProfile.toParams(self)
        kparams.put("objectType", "KalturaYoutubeApiDistributionProfile")
        kparams.addStringIfDefined("username", self.username)
        kparams.addStringIfDefined("password", self.password)
        kparams.addStringIfDefined("defaultCategory", self.defaultCategory)
        kparams.addStringIfDefined("allowComments", self.allowComments)
        kparams.addStringIfDefined("allowEmbedding", self.allowEmbedding)
        kparams.addStringIfDefined("allowRatings", self.allowRatings)
        kparams.addStringIfDefined("allowResponses", self.allowResponses)
        return kparams

    def getUsername(self):
        return self.username

    def setUsername(self, newUsername):
        self.username = newUsername

    def getPassword(self):
        return self.password

    def setPassword(self, newPassword):
        self.password = newPassword

    def getDefaultCategory(self):
        return self.defaultCategory

    def setDefaultCategory(self, newDefaultCategory):
        self.defaultCategory = newDefaultCategory

    def getAllowComments(self):
        return self.allowComments

    def setAllowComments(self, newAllowComments):
        self.allowComments = newAllowComments

    def getAllowEmbedding(self):
        return self.allowEmbedding

    def setAllowEmbedding(self, newAllowEmbedding):
        self.allowEmbedding = newAllowEmbedding

    def getAllowRatings(self):
        return self.allowRatings

    def setAllowRatings(self, newAllowRatings):
        self.allowRatings = newAllowRatings

    def getAllowResponses(self):
        return self.allowResponses

    def setAllowResponses(self, newAllowResponses):
        self.allowResponses = newAllowResponses


class KalturaYoutubeApiDistributionProvider(KalturaDistributionProvider):
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
        self.fromXmlImpl(node, KalturaYoutubeApiDistributionProvider.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProvider.toParams(self)
        kparams.put("objectType", "KalturaYoutubeApiDistributionProvider")
        return kparams


########## services ##########
########## main ##########
class KalturaYoutubeApiDistributionClientPlugin(KalturaClientPlugin):
    # KalturaYoutubeApiDistributionClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaYoutubeApiDistributionClientPlugin
    @staticmethod
    def get(client):
        if KalturaYoutubeApiDistributionClientPlugin.instance == None:
            KalturaYoutubeApiDistributionClientPlugin.instance = KalturaYoutubeApiDistributionClientPlugin(client)
        return KalturaYoutubeApiDistributionClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaYoutubeApiDistributionProfileOrderBy': KalturaYoutubeApiDistributionProfileOrderBy,
            'KalturaYoutubeApiDistributionProviderOrderBy': KalturaYoutubeApiDistributionProviderOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaYoutubeApiDistributionProfileBaseFilter': KalturaYoutubeApiDistributionProfileBaseFilter,
            'KalturaYoutubeApiDistributionProviderBaseFilter': KalturaYoutubeApiDistributionProviderBaseFilter,
            'KalturaYoutubeApiDistributionProfileFilter': KalturaYoutubeApiDistributionProfileFilter,
            'KalturaYoutubeApiDistributionProviderFilter': KalturaYoutubeApiDistributionProviderFilter,
            'KalturaYoutubeApiDistributionProfile': KalturaYoutubeApiDistributionProfile,
            'KalturaYoutubeApiDistributionProvider': KalturaYoutubeApiDistributionProvider,
        }

    # @return string
    def getName(self):
        return 'youtubeApiDistribution'


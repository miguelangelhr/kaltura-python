import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaContentDistributionClientPlugin import *
from KalturaClientBase import *

########## enums ##########
class KalturaYouTubeDistributionProfileOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaYouTubeDistributionProviderOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaYouTubeDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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
        self.fromXmlImpl(node, KalturaYouTubeDistributionProfileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionProfileFilter.toParams(self)
        kparams.put("objectType", "KalturaYouTubeDistributionProfileBaseFilter")
        return kparams


class KalturaYouTubeDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
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
        self.fromXmlImpl(node, KalturaYouTubeDistributionProviderBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProviderFilter.toParams(self)
        kparams.put("objectType", "KalturaYouTubeDistributionProviderBaseFilter")
        return kparams


class KalturaYouTubeDistributionProfileFilter(KalturaYouTubeDistributionProfileBaseFilter):
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
        KalturaYouTubeDistributionProfileBaseFilter.__init__(self,
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
        KalturaYouTubeDistributionProfileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaYouTubeDistributionProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaYouTubeDistributionProfileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaYouTubeDistributionProfileFilter")
        return kparams


class KalturaYouTubeDistributionProviderFilter(KalturaYouTubeDistributionProviderBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented):
        KalturaYouTubeDistributionProviderBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            typeEqual,
            typeIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaYouTubeDistributionProviderBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaYouTubeDistributionProviderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaYouTubeDistributionProviderBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaYouTubeDistributionProviderFilter")
        return kparams


class KalturaYouTubeDistributionProfile(KalturaConfigurableDistributionProfile):
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
            notificationEmail=NotImplemented,
            sftpHost=NotImplemented,
            sftpLogin=NotImplemented,
            sftpPublicKey=NotImplemented,
            sftpPrivateKey=NotImplemented,
            sftpBaseDir=NotImplemented,
            ownerName=NotImplemented,
            defaultCategory=NotImplemented,
            allowComments=NotImplemented,
            allowEmbedding=NotImplemented,
            allowRatings=NotImplemented,
            allowResponses=NotImplemented,
            commercialPolicy=NotImplemented,
            ugcPolicy=NotImplemented,
            target=NotImplemented,
            adServerPartnerId=NotImplemented,
            enableAdServer=NotImplemented,
            allowPreRollAds=NotImplemented,
            allowPostRollAds=NotImplemented):
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
        self.notificationEmail = notificationEmail

        # @var string
        self.sftpHost = sftpHost

        # @var string
        self.sftpLogin = sftpLogin

        # @var string
        self.sftpPublicKey = sftpPublicKey

        # @var string
        self.sftpPrivateKey = sftpPrivateKey

        # @var string
        self.sftpBaseDir = sftpBaseDir

        # @var string
        self.ownerName = ownerName

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

        # @var string
        self.commercialPolicy = commercialPolicy

        # @var string
        self.ugcPolicy = ugcPolicy

        # @var string
        self.target = target

        # @var string
        self.adServerPartnerId = adServerPartnerId

        # @var bool
        self.enableAdServer = enableAdServer

        # @var bool
        self.allowPreRollAds = allowPreRollAds

        # @var bool
        self.allowPostRollAds = allowPostRollAds


    PROPERTY_LOADERS = {
        'username': getXmlNodeText, 
        'notificationEmail': getXmlNodeText, 
        'sftpHost': getXmlNodeText, 
        'sftpLogin': getXmlNodeText, 
        'sftpPublicKey': getXmlNodeText, 
        'sftpPrivateKey': getXmlNodeText, 
        'sftpBaseDir': getXmlNodeText, 
        'ownerName': getXmlNodeText, 
        'defaultCategory': getXmlNodeText, 
        'allowComments': getXmlNodeText, 
        'allowEmbedding': getXmlNodeText, 
        'allowRatings': getXmlNodeText, 
        'allowResponses': getXmlNodeText, 
        'commercialPolicy': getXmlNodeText, 
        'ugcPolicy': getXmlNodeText, 
        'target': getXmlNodeText, 
        'adServerPartnerId': getXmlNodeText, 
        'enableAdServer': getXmlNodeBool, 
        'allowPreRollAds': getXmlNodeBool, 
        'allowPostRollAds': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaConfigurableDistributionProfile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaYouTubeDistributionProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionProfile.toParams(self)
        kparams.put("objectType", "KalturaYouTubeDistributionProfile")
        kparams.addStringIfDefined("username", self.username)
        kparams.addStringIfDefined("notificationEmail", self.notificationEmail)
        kparams.addStringIfDefined("sftpHost", self.sftpHost)
        kparams.addStringIfDefined("sftpLogin", self.sftpLogin)
        kparams.addStringIfDefined("sftpPublicKey", self.sftpPublicKey)
        kparams.addStringIfDefined("sftpPrivateKey", self.sftpPrivateKey)
        kparams.addStringIfDefined("sftpBaseDir", self.sftpBaseDir)
        kparams.addStringIfDefined("ownerName", self.ownerName)
        kparams.addStringIfDefined("defaultCategory", self.defaultCategory)
        kparams.addStringIfDefined("allowComments", self.allowComments)
        kparams.addStringIfDefined("allowEmbedding", self.allowEmbedding)
        kparams.addStringIfDefined("allowRatings", self.allowRatings)
        kparams.addStringIfDefined("allowResponses", self.allowResponses)
        kparams.addStringIfDefined("commercialPolicy", self.commercialPolicy)
        kparams.addStringIfDefined("ugcPolicy", self.ugcPolicy)
        kparams.addStringIfDefined("target", self.target)
        kparams.addStringIfDefined("adServerPartnerId", self.adServerPartnerId)
        kparams.addBoolIfDefined("enableAdServer", self.enableAdServer)
        kparams.addBoolIfDefined("allowPreRollAds", self.allowPreRollAds)
        kparams.addBoolIfDefined("allowPostRollAds", self.allowPostRollAds)
        return kparams

    def getUsername(self):
        return self.username

    def setUsername(self, newUsername):
        self.username = newUsername

    def getNotificationEmail(self):
        return self.notificationEmail

    def setNotificationEmail(self, newNotificationEmail):
        self.notificationEmail = newNotificationEmail

    def getSftpHost(self):
        return self.sftpHost

    def setSftpHost(self, newSftpHost):
        self.sftpHost = newSftpHost

    def getSftpLogin(self):
        return self.sftpLogin

    def setSftpLogin(self, newSftpLogin):
        self.sftpLogin = newSftpLogin

    def getSftpPublicKey(self):
        return self.sftpPublicKey

    def setSftpPublicKey(self, newSftpPublicKey):
        self.sftpPublicKey = newSftpPublicKey

    def getSftpPrivateKey(self):
        return self.sftpPrivateKey

    def setSftpPrivateKey(self, newSftpPrivateKey):
        self.sftpPrivateKey = newSftpPrivateKey

    def getSftpBaseDir(self):
        return self.sftpBaseDir

    def setSftpBaseDir(self, newSftpBaseDir):
        self.sftpBaseDir = newSftpBaseDir

    def getOwnerName(self):
        return self.ownerName

    def setOwnerName(self, newOwnerName):
        self.ownerName = newOwnerName

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

    def getCommercialPolicy(self):
        return self.commercialPolicy

    def setCommercialPolicy(self, newCommercialPolicy):
        self.commercialPolicy = newCommercialPolicy

    def getUgcPolicy(self):
        return self.ugcPolicy

    def setUgcPolicy(self, newUgcPolicy):
        self.ugcPolicy = newUgcPolicy

    def getTarget(self):
        return self.target

    def setTarget(self, newTarget):
        self.target = newTarget

    def getAdServerPartnerId(self):
        return self.adServerPartnerId

    def setAdServerPartnerId(self, newAdServerPartnerId):
        self.adServerPartnerId = newAdServerPartnerId

    def getEnableAdServer(self):
        return self.enableAdServer

    def setEnableAdServer(self, newEnableAdServer):
        self.enableAdServer = newEnableAdServer

    def getAllowPreRollAds(self):
        return self.allowPreRollAds

    def setAllowPreRollAds(self, newAllowPreRollAds):
        self.allowPreRollAds = newAllowPreRollAds

    def getAllowPostRollAds(self):
        return self.allowPostRollAds

    def setAllowPostRollAds(self, newAllowPostRollAds):
        self.allowPostRollAds = newAllowPostRollAds


class KalturaYouTubeDistributionProvider(KalturaDistributionProvider):
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
        self.fromXmlImpl(node, KalturaYouTubeDistributionProvider.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProvider.toParams(self)
        kparams.put("objectType", "KalturaYouTubeDistributionProvider")
        return kparams


########## services ##########
########## main ##########
class KalturaYouTubeDistributionClientPlugin(KalturaClientPlugin):
    # KalturaYouTubeDistributionClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaYouTubeDistributionClientPlugin
    @staticmethod
    def get(client):
        if KalturaYouTubeDistributionClientPlugin.instance == None:
            KalturaYouTubeDistributionClientPlugin.instance = KalturaYouTubeDistributionClientPlugin(client)
        return KalturaYouTubeDistributionClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaYouTubeDistributionProfileOrderBy': KalturaYouTubeDistributionProfileOrderBy,
            'KalturaYouTubeDistributionProviderOrderBy': KalturaYouTubeDistributionProviderOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaYouTubeDistributionProfileBaseFilter': KalturaYouTubeDistributionProfileBaseFilter,
            'KalturaYouTubeDistributionProviderBaseFilter': KalturaYouTubeDistributionProviderBaseFilter,
            'KalturaYouTubeDistributionProfileFilter': KalturaYouTubeDistributionProfileFilter,
            'KalturaYouTubeDistributionProviderFilter': KalturaYouTubeDistributionProviderFilter,
            'KalturaYouTubeDistributionProfile': KalturaYouTubeDistributionProfile,
            'KalturaYouTubeDistributionProvider': KalturaYouTubeDistributionProvider,
        }

    # @return string
    def getName(self):
        return 'youTubeDistribution'


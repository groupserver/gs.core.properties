from gs.option.converter import GSOptionConverterFactory
import zope.schema
import zope.interface
import pytz
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

class IGSCoreOptions(zope.interface.Interface):
    alwaysShowMemberPhotos = zope.schema.Bool(
                                  title=u"Always show photos of members?",
                                  required=True)
    
    supportEmail = zope.schema.TextLine(title=u"Email address for support",
                                  required=True)

    showEmailAddressTo = zope.schema.Choice(title=u"Who should email addresses be shown to?",
                                  required=True,
                                  default='request',
                                  vocabulary=SimpleVocabulary(
                                                (SimpleTerm('request','request',u'Must request'),
                                                 SimpleTerm('nobody','nobody',u'Show no-one'))
                                             ))
    
    tz = zope.schema.Choice(title=u'Timezone',
      description=u'The timezone you wish to use as the default across the site.',
      required=True,
      default='UTC',
      vocabulary=SimpleVocabulary.fromValues(pytz.common_timezones))

    profileInterface = zope.schema.TextLine(title=u"Profile Interface",
                                  required=True)

class GSCoreOptionFactory(GSOptionConverterFactory):
    interface = IGSCoreOptions
    descriminators = ()
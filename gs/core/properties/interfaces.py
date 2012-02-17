from gs.option.converter import GSOptionConverterFactory
import zope.schema
import zope.interface
import pytz
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

class IGSCoreOptions(zope.interface.Interface):
    app_id = zope.schema.TextLine(title=u"Application ID as supplied by Facebook",
                                  required=True)
    app_secret = zope.schema.TextLine(title=u"Application Secret as supplied by Facebook",
                                  required=True)
    
    alwaysShowMemberPhotos = zope.schema.Bool(
                                  title=u"Always show photos of members?",
                                  required=True)

    supportEmail = zope.schema.TextLine(title=u"Email address for support",
                                  required=True)

    showEmailAddressTo = zope.schema.Choice(title=u"Who should email addresses be shown to?",
                                  required=True,
                                  default='request',
                                  vocabulary=SimpleVocabulary(
                             ('request','request',u'Must request'),
                             ('nobody','nobody','Show no-one')))                 
    
    tz = zope.schema.Choice(title=u'Timezone',
      description=u'The timezone you wish to use as the default across the site.',
      required=True,
      default='UTC',
      vocabulary=SimpleVocabulary.fromValues(pytz.common_timezones))

    profileInterface = zope.schema.TextLine(title=u"Profile Interface",
                                  required=True)

class GSCoreOptionFactory(GSOptionConverterFactory):
    interface = IGSCoreOptions

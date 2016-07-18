from django.db import models
from django.utils.translation import ugettext as _
from wealthmap.models import Opportunity


class LongBeachOpportunity(Opportunity):
    description = models.TextField()
    value_prop = models.CharField(max_length=255,
                                  null=False,
                                  blank=False)
    application_link = models.TextField()

    class Meta:
        verbose_name = _('Opportunity')
        verbose_name_plural = _('Opportunities')

from django.db import models
from django.utils.translation import ugettext as _
from wealthmap.models import Opportunity

class LongBeachOpportunity(Opportunity):
    description = models.TextField()

    class Meta:
        verbose_name = _('Opportunity')
        verbose_name_plural = _('Opportunities')

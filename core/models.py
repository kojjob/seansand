from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

  """Tme Stamped Model"""

  created = models.DateTimeField(auto_now_add=True, null=True)
  updated = models.DateTimeField(auto_now=True, null=True)

  class Meta:
    abstract = True

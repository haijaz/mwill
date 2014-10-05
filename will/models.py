from django.db import models
from django.contrib.auth.models import User
from localflavor.us.us_states import STATE_CHOICES

class Testator(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 6)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, null=True, blank=True)
    def __unicode__(self):
        return self.name
        
class Relationships(models.Model):
    type = models.CharField(max_length = 12)    
    def __unicode__(self):
        return self.type
    
class Inheritors(models.Model):
    name = models.CharField(max_length = 30, blank=True, null=True)
    gender = models.CharField(max_length = 6, blank=True, null=True)
    relative = models.ForeignKey('self', blank=True, null=True)
    testator = models.ForeignKey(Testator, blank=True, null=True)
    relationType = models.ForeignKey(Relationships, blank=True, null=True)
    alive = models.NullBooleanField(null=True, default = True)
    def __unicode__(self):
        return self.name
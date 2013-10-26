from django.db import models

class Testator(models.Model):
    name = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 6)
    def __unicode__(self):
        return self.name
        
class Relationships(models.Model):
    type = models.CharField(max_length = 12)    
    def __unicode__(self):
        return self.type
    
class Inheritors(models.Model):
    name = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 6)
    relative = models.ForeignKey('self', blank=True, null=True)
    testator = models.ForeignKey(Testator)
    relationType = models.ForeignKey(Relationships)
    alive = models.NullBooleanField(null=True, default = True)
    def __unicode__(self):
        return self.name
        

    

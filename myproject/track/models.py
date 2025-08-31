from django.db import models

# Create your models here.
class Track(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    @classmethod
    def getalltracks(cls):
        return cls.objects.all()
    @classmethod
    def gettrackbyid(cls,id):
        return cls.objects.get(id=id)

def __str__(self):
    return self.name

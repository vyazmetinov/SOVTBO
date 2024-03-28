from django.db import models
class dumpster(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    percents = models.IntegerField()
    class Meta:
        db_table = 'dumpsters'
    def __str__(self):
        return '{0}, {1}, {2}'.format(self.lat, self.lon, self.percents)
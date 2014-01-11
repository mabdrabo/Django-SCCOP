from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=128)
    lon = models.FloatField()
    lat = models.FloatField()

    def __unicode__(self):
        return self.username

    def get_values(self, title):
        return [log.value for log in LogValue.objects.filter(user=self, title=title).order_by('-date')]

    def get_avg(self, title):
        values = self.get_values(title)
        if values:
            return sum(values) / len(values)
        else:
            return 0

    def get_max(self, title):
        values = self.get_values(title)
        if values:
            return max(values)
        else:
            return 0

    def get_min(self, title):
        values = self.get_values(title)
        if values:
            return min(values)
        else:
            return 0

    def get_location(self):
        return [self.lat, self.lon]

    def update_location(self, longitude, latitude):
        self.lon = longitude
        self.lat = latitude
        return [self.lat, self.lon]


class LogValue(models.Model):
    user = models.ForeignKey(User, related_name='owner')
    title = models.CharField(max_length=64)
    value = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title + " " + str(self.value)

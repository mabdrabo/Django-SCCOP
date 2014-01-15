from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=128)
    lon = models.FloatField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return self.username

    def get(self, title):
        return [log for log in LogValue.objects.filter(user=self, title=title).order_by('-date')]

    def get_values(self, title):
        return [log.value for log in LogValue.objects.filter(user=self, title=title).order_by('-date')]

    def get_locations(self):
        lons = self.get('lon')
        lats = self.get('lat')
        return [[lon, lat] for lon, lat in zip(lons, lats)]

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
    value = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title + " " + str(self.value)

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.title == 'lon':
                self.user.lon = self.value
                self.user.save()
            elif self.title == 'lat':
                self.user.lat = self.value
                self.user.save()
        super(LogValue, self).save(*args, **kwargs)

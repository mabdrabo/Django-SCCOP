from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=128)

	def __unicode__(self):
		return self.username

	def get_rpm_values(self):
		return [log.value for log in LogValue.objects.filter(user=self, title='rpm')]

	def get_temp_values(self):	# temprature values
		return [log.value for log in LogValue.objects.filter(user=self, title='temp')]

	def get_speed_values(self):
		return [log.value for log in LogValue.objects.filter(user=self, title='speed')]

	def get_avg_speed(self):
		values = get_speed_values()
		return sum(values) / len(values)

class LogValue(models.Model):
	user = models.ForeignKey(User, related_name='owner')
	title = models.CharField(max_length=64)
	value = models.IntegerField()

	def __unicode__(self):
		return self.value

from django.db import models

class Stock(models.Model):
	#company ticker( short name for companies)
	ticker = models.CharField(max_length=10)
	opens = models.FloatField()
	close = models.FloatField()
	volume = models.IntegerField()

	def __str__(self):
		return self.ticker

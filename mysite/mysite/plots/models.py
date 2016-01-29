from django.db import models

class PlotData(models.Model):
	name = models.CharField(max_length=30)

# Create your models here.
class Plotting(models.Model):
	url = models.CharField(max_length=30)
	plotdata = models.ForeignKey(PlotData, on_delete=models.CASCADE)
	def __str__(self):
		return  self.url

class Tagging(models.Model):
	plot = models.ForeignKey(Plotting, on_delete=models.CASCADE)
	tag = models.CharField(max_length=30)


#class SubPlotting(models.Model):
#	url = models.CharField(max_length=30)
#	plot = models.ForeignKey(Plotting, on_delete=models.CASCADE)
#	def __str__(self):
#		return  self.url
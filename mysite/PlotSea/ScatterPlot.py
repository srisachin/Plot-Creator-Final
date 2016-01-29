# Copyright Sachin Srivastava

import PlotSea.PlotObj;
import seaborn as sns;
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import settings
from mysite.plots.models import Plotting
from mysite.plots.models import Tagging
from mysite.plots.models import PlotData

class ScatterPlot(PlotSea.PlotObj.PlotObj):
	def plotExp(self,exp,myData,a):
		b = Plotting(url=str(settings.count),plotdata=a)
		b.save()
		d = Tagging(tag='Scatter', plot=b)
		d.save()
		d = Tagging(tag=exp[1]['xaxis'], plot=b)
		d.save()
		d = Tagging(tag=exp[1]['yaxis'], plot=b)
		d.save()
		plt.figure();
		sns.regplot(exp[1]['xaxis'],exp[1]['yaxis'],data=myData);
		plt.savefig("mysite/static/%d.png" %b.id);
		plt.clf()
		plt.close()

		settings.count=settings.count+1;

	def check(self,myStr):
		return myStr=="scatter"

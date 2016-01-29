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

class DensityPlot(PlotSea.PlotObj.PlotObj):
	def plotExp(self,exp,myData,a):
		b = Plotting(url=str(settings.count),plotdata=a)
		b.save()
		d = Tagging(tag='Density', plot=b)
		d.save()
		d = Tagging(tag=exp[1]['xaxis'], plot=b)
		d.save()
		d = Tagging(tag=exp[1]['yaxis'], plot=b)
		d.save()
		plt.figure();
		try:
			sns.kdeplot(myData[exp[1]['xaxis']]);
			plt.savefig("mysite/static/%d.png" %b.id);
		except:
			pass
		plt.clf()
		plt.close()

		settings.count=settings.count+1;

	def check(self,myStr):
		return myStr=="density"

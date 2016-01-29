import PlotSea.PlotObj;
import seaborn as sns;
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import settings
from mysite.plots.models import Plotting
from mysite.plots.models import Tagging
#from mysite.plots.models import SubPlotting
from mysite.plots.models import PlotData
from matplotlib import rcParams

class BarMean(PlotSea.PlotObj.PlotObj):
	def plotExp(self,exp,myData,a):
		rcParams.update({'figure.autolayout': True})
		cats=len(myData[exp[1]['xaxis']].unique())/45
		b = Plotting(url=str(settings.count),plotdata=a)
		b.save()
		d = Tagging(tag='Bar', plot=b)
		d.save()
		d = Tagging(tag=exp[1]['xaxis'], plot=b)
		d.save()
		d = Tagging(tag=exp[1]['yaxis'], plot=b)
		d.save()
		plt.figure();
		sns.barplot(x=exp[1]['xaxis'], y=exp[1]['yaxis'],data=myData,order=myData.groupby(exp[1]['xaxis']).mean().sort(exp[1]['yaxis'],ascending=False).reset_index()[exp[1]['xaxis']],ci=0)
		if (cats>1):
			plt.xticks([])
		else:
			locs, labels = plt.xticks()
			plt.setp(labels, rotation=90)
		plt.savefig("mysite/static/%d.png" %b.id);
		plt.clf()
		plt.close()
		settings.count=settings.count+1;
		'''if (not cats.is_integer()):
			cats=int(cats)+1
		else:
			cats=int(cats)
		if (cats>1):
			for i in range(0,cats):
				plt.figure();
				sns.barplot(x=exp[1]['xaxis'], y=exp[1]['yaxis'],data=myData,order=myData.groupby(exp[1]['xaxis']).mean().sort(exp[1]['yaxis'],ascending=False).reset_index().iloc[i*40:(i+1)*40][exp[1]['xaxis']])
				locs, labels = plt.xticks()
				plt.setp(labels, rotation=90)
				plt.savefig("mysite/static/%d.png" %settings.count);
				plt.clf()
				plt.close()
				g = SubPlotting(url=str(settings.count), plot =b)
				g.save()
				settings.count=settings.count+1;
				print(i)'''


	def check(self,myStr):
		return myStr=="barmean"

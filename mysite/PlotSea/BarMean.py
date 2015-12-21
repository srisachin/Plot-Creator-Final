import PlotSea.PlotObj;
import seaborn as sns;
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import settings


class BarMean(PlotSea.PlotObj.PlotObj):
	def plotExp(self,exp,myData):
		plt.figure();
		g=sns.barplot(x=exp[1]['xaxis'], y=exp[1]['yaxis'],data=myData.sort(exp[1]['xaxis']))
		plt.savefig("mysite/static/%d.png" %settings.count);
		plt.clf()
		plt.close()
		settings.count=settings.count+1;

	def check(self,myStr):
		return myStr=="barmean"

# Copyright Sachin Srivastava

import PlotSea.PlotObj;
import seaborn as sns;
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import settings


class BarPlot(PlotSea.PlotObj.PlotObj):
	def plotExp(self,exp,myData):
		plt.figure();
#		print (exp[1]['xaxis'])
		g=sns.countplot(myData[exp[1]['xaxis']]);
		plt.savefig("mysite/static/%d.png" %settings.count);
		plt.clf()
		plt.close()
		settings.count=settings.count+1;

	def check(self,myStr):
		return myStr=="barcount"

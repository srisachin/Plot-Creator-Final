# Copyright Sachin Srivastava

import PlotSea.PlotObj;
import seaborn as sns;
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import settings


class DensityPlot(PlotSea.PlotObj.PlotObj):
	def plotExp(self,exp,myData):
		plt.figure();
		try:
			sns.kdeplot(myData[exp[1]['xaxis']]);
			plt.savefig("mysite/static/%d.png" %settings.count);
		except:
			pass
		plt.clf()
		plt.close()
		settings.count=settings.count+1;

	def check(self,myStr):
		return myStr=="density"

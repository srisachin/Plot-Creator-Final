# Copyright Sachin Srivastava

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

class BarPlot(PlotSea.PlotObj.PlotObj):
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
        sns.countplot(myData[exp[1]['xaxis']],order=myData[exp[1]['xaxis']].value_counts().index)
        if (cats>1):
            plt.xticks([])
        else:
            locs, labels = plt.xticks()
            plt.setp(labels, rotation=90)
        plt.savefig("mysite/static/%d.png" %b.id);
        plt.clf()
        plt.close()
        settings.count=settings.count+1;
        print("reached here")
        '''if (cats>1):
            if (not cats.is_integer()):
                cats=int(cats)+1
            else:
                cats=int(cats)
            print(cats)
            for i in range(0,cats):
                print(i)
                plt.figure();
                sns.countplot(myData[exp[1]['xaxis']],order=myData[exp[1]['xaxis']].value_counts().iloc[i*45:(i+1)*45].index)
                locs, labels = plt.xticks()
                plt.setp(labels, rotation=90)
                plt.savefig("mysite/static/%d.png" %settings.count);
                plt.clf()
                plt.close()
                print(b)
                g = SubPlotting(url=str(settings.count), plot =b)
                print(b)
                print(g)
                try:
                    g.save()
                except:
                    print("breaking")
                settings.count=settings.count+1;'''


    def check(self,myStr):
        return myStr=="barcount"

'''rcParams.update({'figure.autolayout': True})
		cats=len(myData[exp[1]['xaxis']].unique())/40
		if (not cats.is_integer()):
			cats=int(cats)+1
		else:
			cats=int(cats)
		for i in range(0,cats):
		    plt.figure();
		    sns.countplot(myData[exp[1]['xaxis']],order=myData[exp[1]['xaxis']].value_counts().iloc[i*40:(i+1)*40].index);
		    locs, labels = plt.xticks()
		    plt.setp(labels, rotation=90)
		    plt.savefig("mysite/static/%d.png" %settings.count);
		    plt.clf()
		    plt.close()
		    b = Plotting(url=str(settings.count))
		    b.save()
		    d = Tagging(tag='Bar', plot=b)
		    d.save()
		    d = Tagging(tag=exp[1]['xaxis'], plot=b)
		    d.save()
		    d = Tagging(tag=exp[1]['yaxis'], plot=b)
		    d.save()
		    settings.count=settings.count+1;'''

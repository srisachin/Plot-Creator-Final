# Copyright Sachin Srivastava
# Usage : python Genplots.py <data-filename> <experiment-filename>

import sys
import PlotSea.PlotObj
import pandas as pd
import settings
from PlotSea import *


class Genplots:

	def __init__(self,myDataLoc,myExp,cat=None,val=None):
			self.experiments = pd.DataFrame.from_csv(myExp,index_col=False);
			self.myData = pd.DataFrame.from_csv(myDataLoc,index_col=False,encoding = "ISO-8859-1");
#			self.plotlist = []
			if(cat!=None):
				self.myData = self.myData[self.myData[cat]==val]
			
	
	def myFactory(self,myStr,exp):
		for cls in PlotSea.PlotObj.PlotObj.__subclasses__():
			#__import__(cls.__name__)			
			t = cls()
			if t.check(myStr):
				return t

	def generatePlots(self):		
		for exp in self.experiments.iterrows():
			myStr = exp[1]['plot']
			p=self.myFactory(myStr,exp)
			p.plotExp(exp,self.myData)


def main(argv1,argv2,argv3):	
	myDataLoc=argv1
	myExp=argv2
	settings.initData()
	gen = Genplots(myDataLoc,myExp)
	gen.generatePlots()
	
#	df=pd.DataFrame.from_csv(argv3,index_col=False);
#	for index, row in df.iterrows():
#		gen = Genplots(myDataLoc,myExp,row['col'],row['value'])
#		gen.generatePlots()
		

if __name__ == '__main__':	
	main(sys.argv[1],sys.argv[2],sys.argv[3])

# Input : data, experiments
# Output : list of plots


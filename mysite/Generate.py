# Copyright Sachin Srivastava
# Usage : python Generate.py <schema-filename> <prototype-filename>

import pandas as pd
import sys

class Generate:
	def __init__(self,mySchema,myPrototype):
		self.schema = pd.DataFrame.from_csv(mySchema,index_col=False);		
		self.prototype = pd.DataFrame.from_csv(myPrototype,index_col=False);
	def generateExperiments(self):
		exp1 = pd.merge(self.prototype, self.schema, left_on='xaxis', right_on='type', how='inner');
		exp1['xaxis']=exp1['name'];
		exp1 = exp1[['xaxis','yaxis', 'plot']]
		idx = exp1['yaxis'].isin(['cat', 'num'])
		
		exp2 = pd.merge(exp1[idx], self.schema, left_on='yaxis', right_on='type', how='inner')
		exp2['yaxis']=exp2['name']
		exp2 = exp2[['xaxis','yaxis', 'plot']]
		exp=pd.concat([exp1[~idx], exp2])
		exp.to_csv('experiment.csv')

def main(argv1,argv2):	
	mySchema=argv1
	myPrototype=argv2
	gen = Generate(mySchema,myPrototype)
	gen.generateExperiments()

if __name__ == '__main__':
	main(sys.argv[1],sys.argv[2])

# Input : Schema, Plot Prototype
# Output : Experiments
#Experiment 1
#x=variableName1
#y=variableName2
#plotFuction bar

#
#Experiment 2
#x=variableName3
#y=variableName4
#plotFunction correlation

#
#Experiment 3
#x=variableName2
#y=variableName4
#Groupby=variableName5
#plotFunction correlation


	

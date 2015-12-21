# Copyright Sachin Srivastava
# python3 Groupby.py ZENSUS.csv schemaZ.csv
import pandas as pd
import csv
import sys

class Groupby:
	def __init__(self,myDataLoc,mySchema):
		self.schema = pd.DataFrame.from_csv(mySchema,index_col=False);
		self.myData = pd.DataFrame.from_csv(myDataLoc,index_col=False,encoding = "ISO-8859-1");


	def create(self):
		idx = self.schema[self.schema.type=="cat"].index.tolist()
		z=[]
		for id in idx:
			u=[]
			x=pd.unique(self.myData.ix[:,id])
			v=[self.schema.ix[id,0]]*len(x)
			u = list(zip(v,x))
			z=z+u
		with open('groups.csv','w+') as out:
			csv_out=csv.writer(out)
			csv_out.writerow(['col','value'])
			for row in z:
				csv_out.writerow(row)
		#print (z)

def main(argv1,argv2):
	myDataLoc=argv1
	mySchema=argv2
	gb = Groupby(myDataLoc,mySchema)
	gb.create()

if __name__ == '__main__':
	main(sys.argv[1],sys.argv[2])

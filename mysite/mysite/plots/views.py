#from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
#import pickle
#from django.http import HttpResponse
#from django.template import RequestContext, loader
#import pandas as pd;
#from django.template.context_processors import csrf
#import re;
import Generate;
import Groupby;
import Genplots;
import settings;
import csv;
import codecs;
import ast;


def index(request):
#	plots = defaultdict(list);
#	with open('/home/sachin/mysite/plots/static/plots/plots.pickle', 'rb') as handle:
#		plots = pickle.load(handle)
#	with open('/home/sachin/mysite/plots/static/plots/scores.pickle', 'rb') as handle:
		#scores = pickle.load(handle)
	if (request.is_ajax()):
		print("reached here")
		schema = request.POST.get('schema', '')
		print (schema)
		sdict=ast.literal_eval(schema)
		print (type(sdict))
		for key,value in sdict.items():
			print(key)
			print(value)
		with open('schema.csv', 'w+') as destination:
			csvwriter = csv.writer(destination)
			csvwriter.writerow(["name", "type"])
			for key,value in sdict.items():
				csvwriter.writerow([key, value])
		#return HttpResponse(json.dumps(schema), content_type="application/json")
		return HttpResponse(schema)
	elif (request.method == 'POST'):
#		X = plots['all'];
#		T = [scores[i] for i in X];
#		T = [0 if np.isnan(x) else x for x in T];
#		Y= [x for (t,x) in sorted(zip(T,X),reverse=True)];
#		Y = map(str, Y)
#		T = sorted(T,reverse=True)
		if(not request.FILES):
			f='wine.csv';
		else:
			f=request.FILES['myfile']
		#fs=request.FILES['myschema']

		with open('file.csv', 'wb+') as destination:
		        for chunk in f.chunks():
		            destination.write(chunk)

		#with open('schema.csv', 'wb+') as destination:
		#        for chunk in fs.chunks():
		#            destination.write(chunk)

		#Generate.main("schema.csv", "prototype.csv")
		#Groupby.main("file.csv", "schema.csv")
		#Genplots.main("file.csv", "experiment.csv", "groups.csv")
		#p=list(range(settings.count))
		#p=map(str,p)
#		return render_to_response("plots/index.html", {'plots_scores': zip(Y,T), 'filename' : f})
		#return render_to_response("plots/index.html", { 'plots':p, 'filename' : f})
		with codecs.open('file.csv', 'r', encoding="utf-8") as f:
			d_reader = csv.DictReader(f)
			headers = d_reader.fieldnames
		return render_to_response("index.html", { 'names':headers})
	return render_to_response("index.html")


def analyse(request):
	if (request.method == 'GET'): # If the form is submitted
		print("reached here too")
		Generate.main("schema.csv", "prototype.csv")
		Groupby.main("file.csv", "schema.csv")
		Genplots.main("file.csv", "experiment.csv", "groups.csv")
#		f='';
#		search_query = request.GET.get('search_box', None)
#		X = plots[str(search_query).lower()];
#		T = [scores[i] for i in X];
#		T = [0 if np.isnan(x) else x for x in T];
#		Y= [x for (t,x) in sorted(zip(T,X),reverse=True)];
#		Y = map(str, Y)
#		T = sorted(T,reverse=True)
	return render_to_response("analyse.html", {'plots':map(str,list(range(settings.count)))})
#                              {'plots': plots[search_query]})
				#{'plots': '10'})

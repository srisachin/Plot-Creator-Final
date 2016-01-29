from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import Generate;
import Groupby;
import Genplots;
import settings;
import csv;
import codecs;
import ast;
from mysite.plots.models import Plotting;
from mysite.plots.models import Tagging;
#from mysite.plots.models import SubPlotting;
from mysite.plots.models import PlotData;

def index(request):
	if (request.is_ajax()):
		print("reached here")
		schema = request.POST.get('schema', '')
		print (schema)
		sdict=ast.literal_eval(schema)
		print (type(sdict))
		for key,value in sdict.items():
			print(key)
			print(value)
		with open('schema.csv', 'wt+') as destination:
			csvwriter = csv.writer(destination)
			csvwriter.writerow(["name", "type"])
			for key,value in sdict.items():
				csvwriter.writerow([key, value])
		with open('file.txt', 'r') as f:
			filename = f.readlines()
		Generate.main("schema.csv", "prototype.csv")
		Groupby.main(filename[0], "schema.csv")
		Genplots.main(filename[0], "experiment.csv", "groups.csv")
		return HttpResponse([])
	elif (request.method == 'POST'):
		settings.count=0
		if(not request.FILES):
		    plotdata=PlotData.objects.all()
		    return render_to_response("index.html",{'plotdata':plotdata})
		else:
			f=request.FILES['myfile']
		with open('file.txt', 'w') as dest:
			dest.write(f.name)
		with open(f.name, 'wb+') as destination:
		        for chunk in f.chunks():
		            destination.write(chunk)
		with codecs.open(f.name, 'r', encoding="utf-8") as f:
			d_reader = csv.DictReader(f)
			headers = d_reader.fieldnames
		plotdata=PlotData.objects.all()
		return render_to_response("index.html", { 'names':headers, 'plotdata':plotdata})
	plotdata=PlotData.objects.all()
	return render_to_response("index.html",{'plotdata':plotdata})


def analyse(request):
	if (request.method == 'GET'): # If the form is submitted
		print("reached here too")
		with open('file.txt', 'r') as f:
			filename = f.readlines()
		search_query = request.GET.get('search_box', None)
		plotlist=Plotting.objects.filter(plotdata__name=filename[0])
		if search_query:
			words=search_query.split()
			for i in range(0,len(words)):
				plotlist=plotlist&Plotting.objects.filter(plotdata__name=filename[0]).filter(tagging__tag__icontains=words[i])
		return render_to_response("analyse.html", {'plots':plotlist})

def plotdata(request, plotdata_id=None):
	print (plotdata_id)
	dataname=PlotData.objects.filter(id=plotdata_id).values('name')
	c=dataname[0]['name']
	with open('file.txt', 'w') as dest:
		dest.write(c)
	plotlist=Plotting.objects.filter(plotdata__name=c)
	search_query = request.GET.get('search_box', None)
	if search_query:
			words=search_query.split()
			for i in range(0,len(words)):
				plotlist=plotlist&Plotting.objects.filter(plotdata__name=c).filter(tagging__tag__icontains=words[i])
	return render_to_response("analyse.html", {'plots':plotlist})

def subplots(request, plot_id=None):
	#subplotlist=SubPlotting.objects.filter(plot_id=plot_id)
	#if (not subplotlist):
	tags=Tagging.objects.filter(plot_id=plot_id).exclude(tag="Bar").exclude(tag="prob").exclude(tag="Scatter").exclude(tag="Density").exclude(tag="count").exclude(tag="mean").values('tag')
	plotlist=Plotting.objects.none()
	for t in tags:
		plotlist=plotlist|Plotting.objects.filter(tagging__tag=t["tag"])
	plotlist=plotlist.distinct()
	return render_to_response("analyse.html", {'plots':plotlist})
	#return render_to_response("analyse.html", {'plots':subplotlist})
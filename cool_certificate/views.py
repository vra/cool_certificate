# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
#import request
import create_certificates
from forms import * 

def index(request):
	return render_to_response('index.html')

def feiji(request):
	if request.method == "POST":
		form = NameForm(request.POST)
		if form.is_valid():
			name = request.POST['name']
			create_certificates.feiji(name);
			return render_to_response('feiji.html', {'form':form, 'done':1}, context_instance=RequestContext(request))
 
	else:
		form = NameForm()
	return render_to_response('feiji.html', {'form':form, 'done':0}, context_instance=RequestContext(request))

def chaojishuaige(request):
	if request.method == "POST":
		form = NameForm(request.POST)
		if form.is_valid():
			name = request.POST['name']
			create_certificates.chaojishuaige(name);
			return render_to_response('chaojishuaige.html', {'form':form, 'done':1}, context_instance=RequestContext(request))
 
	else:
		form = NameForm()
	return render_to_response('chaojishuaige.html', {'form':form, 'done':0}, context_instance=RequestContext(request))


def qianshui(request):
	if request.method == "POST":
		form = NameForm(request.POST)
		if form.is_valid():
			name = request.POST['name']
			create_certificates.qianshui(name);
			return render_to_response('qianshui.html', {'form':form, 'done':1}, context_instance=RequestContext(request))
 
	else:
		form = NameForm()
	return render_to_response('qianshui.html', {'form':form, 'done':0}, context_instance=RequestContext(request))

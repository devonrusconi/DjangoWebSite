from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
    context = RequestContext(request)
    return render_to_response('devon/home.html',context)

def tutorials(request):
    context = RequestContext(request)
    return render_to_response('devon/tutorials.html', context)

def projects(request):
    context = RequestContext(request)
    return render_to_response('devon/projects.html', context)


def cs(request):
    context = RequestContext(request)
    return render_to_response('devon/cs.html', context)

def mh(request):
    context = RequestContext(request)
    return render_to_response('devon/mh.html', context)

def stories(request):
    context = RequestContext(request)
    return render_to_response('devon/stories.html', context)

def journal(request):
    context = RequestContext(request)
    return render_to_response('devon/journal.html', context)


from django.shortcuts import render,HttpResponse

# Create your views here.

def index (req):
    return HttpResponse('hello world!')
def create(req):
    return HttpResponse('create!')
def read(req, id):
    return HttpResponse('read! id:' + id)
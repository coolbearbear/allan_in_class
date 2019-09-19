#could be a function or a class

from django.http import HttpResponse

def index(request): #index in webterm is like /
    return HttpResponse('Hello world!')

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish(request):
    return HttpResponse("LIFE IS Beautifull with you  with out you its hard to live")
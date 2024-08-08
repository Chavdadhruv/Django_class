from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# same function path name and function name same
def home(request):
    searchTerm=request.GET.get('searchMovie')
    return render(request, 'home.html',{'name':'dhruv','searchTerm':searchTerm})
def about(request):
    return HttpResponse('<h1>welcome to about page </h1>')
    
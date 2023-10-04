from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def tables_view(request):
    return render(request, 'tables.html')


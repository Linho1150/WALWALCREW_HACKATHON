from django.shortcuts import render
from .forms import addFrom

# Create your views here.
def list(request):
    form= addFrom(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
    print(context)
    return render(request, 'index.html', context)
from django.shortcuts import render, redirect
from .forms import Userformchange
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = Userformchange(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main-home')
    else:
        form = Userformchange
    return render(request, 'users/signup.html', {'form': form})



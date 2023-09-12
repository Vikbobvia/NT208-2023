from django.shortcuts import render
from .forms import MyForm

# Create your views here.
import datetime

def form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            input_data = form.cleaned_data['input_field']
            # Process the input_data
        print("Success button")
    else:
        form = MyForm()


    context = {
        'form' : form,
        'sum' : 1,
        'current_date' : datetime.datetime.now(),
    }
    
    return render(request, 'date_app/current_date.html', context)


def intro (request) :
    return render (request, 'date_app/intro.html')

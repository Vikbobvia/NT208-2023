from django.shortcuts import render
from .forms import MyForm
from .models import Text_table
# Create your views here.
import datetime



def form_view(request):
    output_data = ""
    latest_text = " "
    
    print(request.method)
    
    if request.method == 'POST':
        
        form = MyForm(request.POST)

        if form.is_valid() :#and 'submit' in request.POST:
            action = request.POST.get('action')
            if action == 'delete_output':
                output_data = ""
            elif action == 'delete_all':
                form = MyForm()
                output_data = ""
            elif action == "get_output":
                output_data = form.cleaned_data['input_field']
            elif action == 'save_output':
                output_data = form.cleaned_data['input_field']
                post = Text_table(date = datetime.datetime.now(), description = output_data )
                post.save() 
                print("Save successful")
    
    elif request.method == 'GET':

        Blog_Database = Text_table.objects.all()

        form = MyForm(request.GET)

        print("Get successful !")
        get_data_action = request.GET.get('get_data')
        print(get_data_action)
        print(latest_text)

        if "latest" in get_data_action:  
            try:  
                latest_text = Blog_Database.last().description
            except AttributeError:
                pass
        elif "clear" in get_data_action:
            # print("False in latest text")
            latest_text = ""

        elif "delete" in get_data_action:
            Blog_Database.delete()
        print("Success button")


    else:
        form = MyForm()
    
    print("Result of latest text", latest_text)
    context = {
        'form' : form,
        'sum' : 1,
        'current_date' : datetime.datetime.now(),
        'output_data' : output_data,
        'latest_text' : latest_text
    }
    
    return render(request, 'date_app/current_date.html', context)


def intro (request) :
    return render (request, 'date_app/intro.html')

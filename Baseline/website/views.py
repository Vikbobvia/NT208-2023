from django.shortcuts import render
from .forms import MyForm
from .models import Text_table
from django.views.generic import ListView, DetailView
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
                description_data = ""

            elif action == 'delete_all':
                form = MyForm()
                description_data = ""

            elif action == "get_output":
                output_data = form.cleaned_data['title_input']

            elif action == 'save_output':
                try :
                    title_data = form.cleaned_data['title_input']
                    description_data = form.cleaned_data['description_input']
                    post = Text_table(  date = datetime.datetime.now(),
                                        description = description_data,
                                        title = title_data)
                    post.save() 
                    print("Save successful")
                except UnboundLocalError:
                    pass

    elif request.method == 'GET':
        print(Text_table.objects.count())
        Blog_Database = Text_table.objects.all()

        form = MyForm(request.GET)

        print("Get successful !")
        get_data_action = request.GET.get('get_data')
        print(get_data_action)
        print(latest_text)
        
        if get_data_action is not None:
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


    links = [
        {'url': '../..', 'text': 'This website'},
        {'url': '../blogs_list', 'text': 'List of blog'},
        # {'url': '../blogs_details/<int:pk>', 'text': 'Detail'},

    ]

    

    
    context = {
        'form' : form,
        'Current_blog_number' : Text_table.objects.count(),
        'current_date' : datetime.datetime.now(),
        'output_data' : output_data,
        'latest_text' : latest_text,
        'links' : links
    }
    
    return render(request, 'current_date.html', context)


def intro (request) :
    return render (request, 'intro.html')




class BlogListView(ListView):
    model = Text_table
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    ordering = ['date']



class BlogDetailView(DetailView):
    model = Text_table
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add extra variables to the context dictionary
        context['date'] = datetime.datetime.now()

        return context

  

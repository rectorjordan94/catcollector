from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Cat, Toy
from .forms import FeedingForm

# temporary cats for building templates
# cats = [
#     {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3 },
#     {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
# ]

# Create your views here.
# view functions match urls to code (like controllers in Express)
# define our home view function
def home(request):
    return render(request, 'home.html')

# about route
def about(request):
    return render(request, 'about.html')

# index route for cats
def cats_index(request):
    # just like we passed data to our templates in express
    # we pass data to our templates through our view functions
    # we can gather relations from SQL using our model methods
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', { 'cats': cats })

# detail route for cats
# cat_id is defined, expecting an integer, in our url
def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)

    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', { 'cat': cat, 'feeding_form': feeding_form })

class CatCreate(CreateView):
    model = Cat
    # the fields attribute is required for a createview
    fields = '__all__'
    # we could also have written our fields like this:
    # fields = ['name', 'breed', 'description', 'age']

    # we need to add redirects when we make a success
    # success_url = '/cats/{cat_id}'
    # or we could redirect to the index page if we want
    # success_url = '/cats/'

    # what django recommends is adding a get_absolute_url to the model

class CatUpdate(UpdateView):
    model = Cat
    # let's use custom fields to disallow renaming a cat
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'

def add_feeding(request, cat_id):
    # create a ModelForm instance from the data in request.POST
    form = FeedingForm(request.POST)

    # we need to validate the form, that means does it match our data?
    if form.is_valid():
        # we dont want to save the form to the db until it has the cat_id
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('detail', cat_id=cat_id)

# ToyList
class ToyList(ListView):
    model = Toy
    template = 'toys/index.html'

# ToyDetail
class ToyDetail(DetailView):
    model = Toy
    template = 'toys/detail.html'

# ToyCreate
class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']

    # define what the inherited method is_valid does(we'll update this later)
    def form_valid(self, form):
        # we'll use this later, but implement right now
        # we'll need this when we add auth
        # super allows for the original inherited CreateView function to work as it was intended
        return super().form_valid(form)

# ToyUpdate
class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

# ToyDelete
class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

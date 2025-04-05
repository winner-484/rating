from django.shortcuts import render

from django.http import HttpResponse

from django.views import View

# from .forms import SimpleForm

from django.http import HttpResponseRedirect

from django.views.generic import ListView
from .models import Rating

# Create your views here.

class RatingsListView(ListView):
    model = Rating
    context_object_name = 'GG_T'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['Foo'] = '7STAR'
        return context

class SimpleView(View):
    def get(self, request):
        return HttpResponse('Hello, world')

class SimpleFormView(View):
    # form_class = SimpleForm/
    initial = {'foo': 'initial value'}
    template_name = 'form_template.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})



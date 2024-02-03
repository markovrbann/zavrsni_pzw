from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import *
from django.views.generic import *
from main.models import *

from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

def landing_page(request):
    return render(request, 'home.html')

class PredavacView(ListView):
    model = Predavac
    
class PredavacListView(ListView):
    model = Predavac
    template_name = 'main/list_predavac.html'
    context_object_name = 'predavac'
    
class PredavacDeleteView(DeleteView):
    model = Predavac
    template_name = 'deletepr_predavac.html'
    success_url = reverse_lazy('main:predavaci')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['predavac'] = self.get_object()
        return context

class PredavacCreateView(CreateView):
    model = Predavac
    form_class = PredavacForm
    template_name = 'add_predavac.html'
    success_url = reverse_lazy('main:predavaci')    
    
class PredavacUpdateView(UpdateView):
    model = Predavac
    form_class = PredavacForm
    template_name = 'update_predavac.html'
    success_url = reverse_lazy('main:predavaci')    
    
class TecajView(ListView):
    model = Tecaj

class TecajCreateView(CreateView):
    model = Tecaj
    form_class = TecajForm
    template_name = 'add_tecaj.html'
    success_url = reverse_lazy('main:tecajevi')    
    
class TecajUpdateView(UpdateView):
    model = Tecaj
    form_class = TecajForm
    template_name = 'update_tecaj.html'
    success_url = reverse_lazy('main:tecajevi')    
    
class TecajDeleteView(DeleteView):
    model = Tecaj
    template_name = 'delete_tecaj.html'
    success_url = reverse_lazy('main:tecajevi')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tecaj'] = self.get_object()
        return context
    
class PrebivalisteView(ListView):
    model = Prebivaliste

class PrebivalisteCreateView(CreateView):
    model = Prebivaliste
    form_class = PrebivalisteForm
    template_name = 'add_prebivaliste.html'
    success_url = reverse_lazy('main:prebivaliste')    
    
class PrebivalisteUpdateView(UpdateView):
    model = Prebivaliste
    form_class = PrebivalisteForm
    template_name = 'update_prebivaliste.html'
    success_url = reverse_lazy('main:prebivaliste')    
    
class PrebivalisteDeleteView(DeleteView):
    model = Prebivaliste
    template_name = 'delete_prebivaliste.html'
    success_url = reverse_lazy('main:prebivaliste')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prebivaliste'] = self.get_object()
        return context
    
class PolaznikView(ListView):
    model = Polaznik

class PolaznikCreateView(CreateView):
    model = Polaznik
    form_class = PolaznikForm
    template_name = 'add_polaznik.html'
    success_url = reverse_lazy('main:polaznik')    
    
class PolaznikUpdateView(UpdateView):
    model = Polaznik
    form_class = PolaznikForm
    template_name = 'update_polaznik.html'
    success_url = reverse_lazy('main:polaznik')    
    
class PolaznikDeleteView(DeleteView):
    model = Polaznik
    template_name = 'delete_polaznik.html'
    success_url = reverse_lazy('main:polaznik')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['polaznik'] = self.get_object()
        return context
    
class TjedanradnovrijemeView(ListView):
    model = TjedanRadnoVrijeme
    
class RasporedView(ListView):
    model = Raspored

class RasporedCreateView(CreateView):
    model = Raspored
    form_class = RasporedForm
    template_name = 'add_raspored.html'
    success_url = reverse_lazy('main:raspored')    
    
class RasporedUpdateView(UpdateView):
    model = Raspored
    form_class = RasporedForm
    template_name = 'update_raspored.html'
    success_url = reverse_lazy('main:raspored')    
    
class RasporedDeleteView(DeleteView):
    model = Raspored
    template_name = 'delete_raspored.html'
    success_url = reverse_lazy('main:raspored')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['raspored'] = self.get_object()
        return context
    
class OcjenaView(ListView):
    model = Ocjena

class OcjenaCreateView(CreateView):
    model = Ocjena
    form_class = OcjenaForm
    template_name = 'add_ocjena.html'
    success_url = reverse_lazy('main:ocjena')    
    
class OcjenaUpdateView(UpdateView):
    model = Ocjena
    form_class = OcjenaForm
    template_name = 'update_ocjena.html'
    success_url = reverse_lazy('main:ocjena')    
    
class OcjenaDeleteView(DeleteView):
    model = Ocjena
    template_name = 'delete_ocjena.html'
    success_url = reverse_lazy('main:ocjena')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ocjena'] = self.get_object()
        return context
    

## Create your views here.
def index(request):
    return render(request, './home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main:index')

    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)
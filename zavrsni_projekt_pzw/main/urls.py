from django.urls import path
from . import views

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('predavaci/', views.PredavacView.as_view(), name='predavaci'),
    path('addpr/', views.PredavacCreateView.as_view(), name='addpr'),
    path('deletepr/<int:pk>', views.PredavacDeleteView.as_view(), name='deletepr'),
    path('updatepr/<int:pk>', views.PredavacUpdateView.as_view(), name='updatepr'),
    
    path('tecajevi/', views.TecajView.as_view(), name='tecajevi'),
    path('addte/', views.TecajCreateView.as_view(), name='addte'),
    path('updatete/<int:pk>', views.TecajUpdateView.as_view(), name='updatete'),
    path('deletete/<int:pk>', views.TecajDeleteView.as_view(), name='deletete'),

    path('prebivaliste/', views.PrebivalisteView.as_view(), name='prebivaliste'),
    path('addpre/', views.PrebivalisteCreateView.as_view(), name='addpre'),
    path('updatepre/<int:pk>', views.PrebivalisteUpdateView.as_view(), name='updatepre'),
    path('deletepre/<int:pk>', views.PrebivalisteDeleteView.as_view(), name='deletepre'),
    
    path('polaznik/', views.PolaznikView.as_view(), name='polaznik'),
    path('addpol/', views.PolaznikCreateView.as_view(), name='addpol'),
    path('updatepol/<int:pk>', views.PolaznikUpdateView.as_view(), name='updatepol'),
    path('deletepol/<int:pk>', views.PolaznikDeleteView.as_view(), name='deletepol'),
    
    path('tjedanradnovrijeme/', views.TjedanradnovrijemeView.as_view(), name='tjedanradnovrijeme'),
    
    path('raspored/', views.RasporedView.as_view(), name='raspored'),
    path('addras/', views.RasporedCreateView.as_view(), name='addras'),
    path('updateras/<int:pk>', views.RasporedUpdateView.as_view(), name='updateras'),
    path('deleteras/<int:pk>', views.RasporedDeleteView.as_view(), name='deleteras'),

    path('ocjena/', views.OcjenaView.as_view(), name='ocjena'),
    path('addocj/', views.OcjenaCreateView.as_view(), name='addocj'),
    path('updateocj/<int:pk>', views.OcjenaUpdateView.as_view(), name='updateocj'),
    path('deleteocj/<int:pk>', views.OcjenaDeleteView.as_view(), name='deleteocj'),
    
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    
    path('pretraga/', views.PredavacListView.as_view(), name='pretraga'),


]

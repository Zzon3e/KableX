from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # Medlem
    path('medlemmer/', views.MedlemListView.as_view(), name='medlem_list'),
    path('medlemmer/ny/', views.MedlemCreateView.as_view(), name='medlem_create'),
    path('medlemmer/<int:pk>/', views.MedlemDetailView.as_view(), name='medlem_detail'),
    path('medlemmer/<int:pk>/endre/', views.MedlemUpdateView.as_view(), name='medlem_update'),
    path('medlemmer/<int:pk>/slett/', views.MedlemDeleteView.as_view(), name='medlem_delete'),
    
    # Aktivitet
    path('aktiviteter/', views.AktivitetListView.as_view(), name='aktivitet_list'),
    path('aktiviteter/ny/', views.AktivitetCreateView.as_view(), name='aktivitet_create'),
    path('aktiviteter/<int:pk>/', views.AktivitetDetailView.as_view(), name='aktivitet_detail'),
    path('aktiviteter/<int:pk>/endre/', views.AktivitetUpdateView.as_view(), name='aktivitet_update'),
    path('aktiviteter/<int:pk>/slett/', views.AktivitetDeleteView.as_view(), name='aktivitet_delete'),
    
    # Påmelding
    path('pameldigninger/', views.PameldingListView.as_view(), name='pamelding_list'),
    path('pameldigninger/ny/', views.PameldingCreateView.as_view(), name='pamelding_create'),
    path('pameldigninger/<int:pk>/', views.PameldingDetailView.as_view(), name='pamelding_detail'),
    path('pameldigninger/<int:pk>/slett/', views.PameldingDeleteView.as_view(), name='pamelding_delete'),
    
    # Betaling
    path('betalinger/', views.BetalingListView.as_view(), name='betaling_list'),
    path('betalinger/ny/', views.BetalingCreateView.as_view(), name='betaling_create'),
    path('betalinger/<int:pk>/', views.BetalingDetailView.as_view(), name='betaling_detail'),
    path('betalinger/<int:pk>/endre/', views.BetalingUpdateView.as_view(), name='betaling_update'),
    path('betalinger/<int:pk>/slett/', views.BetalingDeleteView.as_view(), name='betaling_delete'),
]
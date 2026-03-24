from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Medlem, Aktivitet, Pamelding, Betaling
from .forms import MedlemForm, AktivitetForm, PameldingForm, BetalingForm


# ========== MEDLEM VIEWS ==========

class MedlemListView(ListView):
    """Viser liste over alle medlemmer"""
    model = Medlem
    template_name = 'products/medlem_list.html'
    context_object_name = 'medlemmer'
    paginate_by = 10


class MedlemCreateView(SuccessMessageMixin, CreateView):
    """Oppretter nytt medlem"""
    model = Medlem
    form_class = MedlemForm
    template_name = 'products/medlem_form.html'
    success_url = reverse_lazy('products:medlem_list')
    success_message = "Medlem opprettet!"


class MedlemDetailView(DetailView):
    """Viser detaljer om ett medlem"""
    model = Medlem
    template_name = 'products/medlem_detail.html'
    context_object_name = 'medlem'


class MedlemUpdateView(SuccessMessageMixin, UpdateView):
    """Endrer medlem"""
    model = Medlem
    form_class = MedlemForm
    template_name = 'products/medlem_form.html'
    success_url = reverse_lazy('products:medlem_list')
    success_message = "Medlem endret!"


class MedlemDeleteView(DeleteView):
    """Sletter medlem"""
    model = Medlem
    template_name = 'products/medlem_confirm_delete.html'
    success_url = reverse_lazy('products:medlem_list')


# ========== AKTIVITET VIEWS ==========

class AktivitetListView(ListView):
    """Viser liste over alle aktiviteter"""
    model = Aktivitet
    template_name = 'products/aktivitet_list.html'
    context_object_name = 'aktiviteter'
    paginate_by = 10


class AktivitetCreateView(SuccessMessageMixin, CreateView):
    """Oppretter ny aktivitet"""
    model = Aktivitet
    form_class = AktivitetForm
    template_name = 'products/aktivitet_form.html'
    success_url = reverse_lazy('products:aktivitet_list')
    success_message = "Aktivitet opprettet!"


class AktivitetDetailView(DetailView):
    """Viser detaljer om en aktivitet"""
    model = Aktivitet
    template_name = 'products/aktivitet_detail.html'
    context_object_name = 'aktivitet'


class AktivitetUpdateView(SuccessMessageMixin, UpdateView):
    """Endrer aktivitet"""
    model = Aktivitet
    form_class = AktivitetForm
    template_name = 'products/aktivitet_form.html'
    success_url = reverse_lazy('products:aktivitet_list')
    success_message = "Aktivitet endret!"


class AktivitetDeleteView(DeleteView):
    """Sletter aktivitet"""
    model = Aktivitet
    template_name = 'products/aktivitet_confirm_delete.html'
    success_url = reverse_lazy('products:aktivitet_list')


# ========== PÅMELDING VIEWS ==========

class PameldingListView(ListView):
    """Viser liste over alle påmeldinger"""
    model = Pamelding
    template_name = 'products/pamelding_list.html'
    context_object_name = 'pameldigninger'
    paginate_by = 15


class PameldingCreateView(SuccessMessageMixin, CreateView):
    """Oppretter ny påmelding"""
    model = Pamelding
    form_class = PameldingForm
    template_name = 'products/pamelding_form.html'
    success_url = reverse_lazy('products:pamelding_list')
    success_message = "Påmelding opprettet!"


class PameldingDetailView(DetailView):
    """Viser detaljer om en påmelding"""
    model = Pamelding
    template_name = 'products/pamelding_detail.html'
    context_object_name = 'pamelding'


class PameldingDeleteView(DeleteView):
    """Sletter påmelding"""
    model = Pamelding
    template_name = 'products/pamelding_confirm_delete.html'
    success_url = reverse_lazy('products:pamelding_list')


# ========== BETALING VIEWS ==========

class BetalingListView(ListView):
    """Viser liste over alle betalinger"""
    model = Betaling
    template_name = 'products/betaling_list.html'
    context_object_name = 'betalinger'
    paginate_by = 15


class BetalingCreateView(SuccessMessageMixin, CreateView):
    """Oppretter ny betaling"""
    model = Betaling
    form_class = BetalingForm
    template_name = 'products/betaling_form.html'
    success_url = reverse_lazy('products:betaling_list')
    success_message = "Betaling registrert!"


class BetalingDetailView(DetailView):
    """Viser detaljer om en betaling"""
    model = Betaling
    template_name = 'products/betaling_detail.html'
    context_object_name = 'betaling'


class BetalingUpdateView(SuccessMessageMixin, UpdateView):
    """Endrer betaling"""
    model = Betaling
    form_class = BetalingForm
    template_name = 'products/betaling_form.html'
    success_url = reverse_lazy('products:betaling_list')
    success_message = "Betaling endret!"


class BetalingDeleteView(DeleteView):
    """Sletter betaling"""
    model = Betaling
    template_name = 'products/betaling_confirm_delete.html'
    success_url = reverse_lazy('products:betaling_list')
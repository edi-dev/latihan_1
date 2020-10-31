from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import KontakForm, ContactForm
from .models import Kontak

# Create your views here.
def KontakView(request):
    contact_form = KontakForm(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid():
            simpan_data = Kontak.objects.create(
                nama_lengkap = contact_form.cleaned_data.get('nama_lengkap'),
                jenis_kelamin = contact_form.cleaned_data.get('jenis_kelamin'),
                tanggal_lahir = contact_form.cleaned_data.get('tanggal_lahir'),
                alamat = contact_form.cleaned_data.get('alamat'),
                agree = contact_form.cleaned_data.get('agree')
            )
            return redirect('Contact:kontakList')
    context = {
        'title': 'Belajar Django',
        'kontak_saya': contact_form,
        'formulir': 'Class Form'
    }
    return render(request, 'contact/contact_form.html', context)

class KontakList(ListView):
    queryset = Kontak.objects.all()

class ContactCreate(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    model = Kontak
    success_url = reverse_lazy('Contact:kontakList')
    success_message = 'Kontak berhasil disimpan'
    template_name = 'contact/contact_form.html'
    extra_context = {
        'kontak_saya': form_class,
        'formulir': 'Model Form'
    }
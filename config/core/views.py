from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Box, Material, Appointment
from config.core.forms import AppointmentFormScan, AppointmentFormVoice


# Create your views here.

def core_page(request):
    return render(request, 'core/core.html')


def login(request):
    response = redirect('core_page')
    return response
    # return render(request, 'core/core.html')


def page_logout(request):
    if request.method == 'POST':
        logout(request)

    return redirect("/")


def appointment_scan(request):
    forms_scan = AppointmentFormScan(request.POST or None)
    if request.method == 'POST':
        if forms_scan.is_valid():
            new_appointment = forms_scan.save(commit=False)
            new_appointment.box = Box.objects.filter(code_box=forms_scan.cleaned_data['box']).first()
            new_appointment.material = Material.objects.filter(
                code_material=forms_scan.cleaned_data['material']).first()
            new_appointment.creator = request.user
            new_appointment.save()
            Box.objects.filter(code_box=forms_scan.cleaned_data['box']).update(is_empty=False)
            forms_scan = AppointmentFormScan()

    context = {'forms_scan': forms_scan}
    return render(request, 'core/appointment_scan.html', context)


def appointment_voice(request):
    forms_voice = AppointmentFormVoice(request.POST or None)
    if request.method == 'POST':
        if forms_voice.is_valid():
            pass

    context = {'forms_voice': forms_voice}
    return render(request, 'core/appointment_voice.html', context)

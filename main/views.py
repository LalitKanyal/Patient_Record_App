from django.shortcuts import render
from . models import Patient
from . forms import PatientForm
from django.contrib import messages


def home(request):
    data=Patient.objects.all()
    return render(request, 'home.html',{'data':data})

# Add Patient
def addPatient(request):
    form = PatientForm
    if request.method == 'POST':
        saveForm = PatientForm(request.POST)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request, 'Data has been added successfully.')
        return render(request, 'add-patient.html', {'form': form})
    else:
        return render(request, 'add-patient.html', {'form': form})


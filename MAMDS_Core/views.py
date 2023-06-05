"""

    Application Views

"""


from django.shortcuts import render, redirect
from .forms import ContactForm, OperationsTypeModelForm, ActivitiesModelForm, OperationsModelForm
from .models import OperationsType, Activities, Operations
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        'tipo_operacoes': OperationsType.objects.all(), 'atividades': Activities.objects.all(),
        'operacoes': Operations.objects.all(),
    }
    return render(request, "index.html", context)


def contact(request):
    o_form = ContactForm(request.POST or None)  # receive the data form filled or blank (None)

    if str(request.method) == "POST":
        if o_form.is_valid():
            o_form.send_mail()

            messages.success(request, "E-mail enviado com sucesso!")
            o_form = ContactForm()
        else:
            messages.error(request, "Erro ao enviarr email!")

    o_context = {
        "form": o_form
    }
    return render(request, "contact.html", o_context)


def operations_type_form(request):
    if str(request.user) != "AnonymousUser":
        if str(request.method) == "POST":
            # POST -> receive data - FILES -: receive image file
            o_form = OperationsTypeModelForm(request.POST, request.FILES)
            if o_form.is_valid():

                o_form.save()

                messages.success(request, "Tipo de Operaçao salva com sucesso!")
                o_form = OperationsTypeModelForm()
            else:
                messages.error(request, "Erro ao salvar Tipo de Operaçao")
        else:
            o_form = OperationsTypeModelForm()

        o_context = {
            "form": o_form
        }
        return render(request, "operations_type_form.html", o_context)
    else:
        return redirect("index")



def activities_form(request):
    if str(request.method) == "POST":
        # POST -> receive data - FILES -: receive image file
        o_form = ActivitiesModelForm(request.POST, request.FILES)
        if o_form.is_valid():
            o_form.save()

            messages.success(request, "Atividade salva com sucesso!")
            o_form = ActivitiesModelForm()
        else:
            messages.error(request, "Erro ao salvar Atividade!")
    else:
        o_form = ActivitiesModelForm()

    o_context = {
        "form": o_form
    }
    return render(request, "activities_form.html", o_context)


def operations_form(request):
    if str(request.method) == "POST":
        # POST -> receive data - FILES -: receive image file
        o_form = OperationsModelForm(request.POST)
        if o_form.is_valid():
            o_form.save()

            messages.success(request, "Operaçao salva com sucesso!")
            o_form = OperationsModelForm()
        else:
            messages.error(request, "Erro ao salvar Operaçao")
    else:
        o_form = OperationsModelForm()

    o_context = {
        "form": o_form
    }
    return render(request, "operations_form.html", o_context)


def form_clothes(request):
    return render(request, "form_clothes.html")

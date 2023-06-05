"""

    - Forms file - file where is all application forms

"""


from django import forms
from django.core.mail.message import EmailMessage
from .models import OperationsType, Activities, Operations


class ContactForm(forms.Form):
    o_name = forms.CharField(label="Nome", max_length=350)
    o_email = forms.EmailField(label="e-mail", max_length=350)
    o_subject = forms.CharField(label="Assunto", max_length=350)
    o_message = forms.CharField(label="Mensagem", widget=forms.Textarea())

    def send_mail(self):
        o_name = self.cleaned_data["o_name"]
        o_email = self.cleaned_data["o_email"]
        o_subject = self.cleaned_data["o_subject"]
        o_message = self.cleaned_data["o_message"]

        s_content = f"Nome: {o_name}\nE-mail: {o_email}\nAssunto: {o_subject}\nMensagem: {o_message}"

        o_mail = EmailMessage(
            subject="Email enviado pello sistema Django 4",
            body=s_content,
            from_email="ypioca.mam@hotmail.com",
            to=["nautilus.mam@gmail.com",],
            headers={"Replay-To": o_email}
        )
        o_mail.send()


class OperationsTypeModelForm(forms.ModelForm):

    class Meta:
        model = OperationsType
        fields = ["operation_type_name"]


class ActivitiesModelForm(forms.ModelForm):

    class Meta:
        model = Activities
        fields = ["activity_name", "mechanical_efficiency", "activity_image"]


class OperationsModelForm(forms.ModelForm):

    class Meta:
        model = Operations
        fields = ["operation_type_id", "activity_id"]
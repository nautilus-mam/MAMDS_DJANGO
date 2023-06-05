"""

    - Application urls file

"""


from django.urls import path, include
from pictures.conf import get_settings
from .views import index, contact, form_clothes, operations_type_form, activities_form, operations_form


urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contato"),
    path("form_clothes/", form_clothes, name="vestuário"),
    path("operations_type_form/", operations_type_form, name="tipo operacao"),
    path("activities_form/", activities_form, name="atividade"),
    path("operations_form/", operations_form, name="operacao")
]

if get_settings().USE_PLACEHOLDERS:
    urlpatterns += [
        path("_pictures/", include("pictures.urls")),
    ]
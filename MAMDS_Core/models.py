"""

    - Database models
        - Library models.signal
            - in models has the class signal - indicate to database that should be run a trigger before or after
                insert data
    - template
        - defaultfilters
            - slugify - from the page title, create a valid url -- Ex: Clothes Form -> clothes-form (slugify)

"""

from django.db import models
from pictures.models import PictureField
from django.template.defaultfilters import slugify


# Create your models here.
class BaseModel(models.Model):
    create_date = models.DateField(verbose_name="Data Criação", auto_now_add=True)
    last_update = models.DateField(verbose_name="Última Atualização", auto_now=True)
    is_active = models.BooleanField(verbose_name="Ativo", default=True)

    class Meta:
        abstract = True  # indic an abstract class, ie, it does not create in database


class OperationsType(BaseModel):
    operation_type_id = models.AutoField(primary_key=True, verbose_name="ID")
    operation_type_name = models.CharField(max_length=250, unique=True, verbose_name="Tipo Operação")
    operation_type_slug = models.SlugField("Slug", max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.operation_type_name


class Activities(BaseModel):
    activity_id = models.AutoField(primary_key=True, verbose_name="ID")
    activity_name = models.CharField(max_length=250, unique=True, verbose_name="Atividade")
    mechanical_efficiency = models.DecimalField(max_digits=6, decimal_places=3, verbose_name="Eficiência Mecânia",
                                                default=0)
    activity_image = PictureField(upload_to="activity", verbose_name="Imagem",
                                  blank=True)  # does not support to 'variations={"thumb": (124, 124)}'
    activity_slug = models.SlugField("Slug", max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.activity_name


class Operations(BaseModel):
    operation_id = models.AutoField(primary_key=True, verbose_name="ID")
    operation_type_id = models.ForeignKey("OperationsType",verbose_name="Tipo Operaçao", on_delete=models.PROTECT)
    activity_id = models.ForeignKey("Activities", verbose_name="Atividades", on_delete=models.PROTECT)
    operation_slug = models.SlugField("Slug", max_length=100, blank=True, editable=False)
    s_operation = f"{operation_id} -- {activity_id}"

    def __str__(self):
        return self.s_operation


def operations_type_pre_save(signal, instance, sender, **kwargs):
    instance.operation_type_slug = slugify(instance.operation_type_name)


def activities_pre_save(signal, instance, sender, **kwargs):
    instance.activity_slug = slugify(instance.activity_name)


def operations_pre_save(signal, instance, sender, **kwargs):
    instance.operation_slug = slugify(instance.s_operation)


models.signals.pre_save.connect(operations_type_pre_save, sender=OperationsType)
models.signals.pre_save.connect(activities_pre_save, sender=Activities)
models.signals.pre_save.connect(operations_pre_save, sender=Operations)

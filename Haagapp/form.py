from django.forms import ModelForm

from Haagapp.models import Eventmaterials_model


class MaterialForm(ModelForm):
    class Meta:
        model=Eventmaterials_model
        fields=['Materialsname','imagematerial','Description','Amount','date']
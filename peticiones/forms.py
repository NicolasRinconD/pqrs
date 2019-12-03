from django import forms


class PeticionForm(forms.Form):
    asunto = forms.CharField(max_length=80)
    descripcion = forms.CharField(widget=forms.Textarea)
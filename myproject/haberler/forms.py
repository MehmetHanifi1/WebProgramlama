from django import forms

class HaberForm(forms.Form):
    haber_id = forms.IntegerField(label='haber_id', widget=forms.NumberInput(attrs={'placeholder': 'Haber ID girin'}))

# forms.py
from django import forms

class CropForm(forms.Form):
    nitrogen = forms.FloatField(
        label='Nitrogen (mineral ratio in the soil)',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=1.0,
        max_value=300.0,
    )
    phosphorous = forms.FloatField(
        label='Phosphorous (mineral ratio in the soil)',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=1.0,
        max_value=300.0,
    )
    pottassium = forms.FloatField(
        label='Pottassium (mineral ratio in the soil)',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=1.0,
        max_value=300.0,
    )
    temperature = forms.FloatField(
        label='Temperature',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )
    humidity = forms.FloatField(
        label='Humidity',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )
    ph = forms.FloatField(
        label='pH (1-14)',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=1.0,
        max_value=14.0,
    )
    rainfall = forms.FloatField(
        label='Rainfall (in cm)',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=50.0,
        max_value=250.0,
    )
    area = forms.FloatField(
        label='Area',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )

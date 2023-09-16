from django import forms

class MyForm(forms.Form):
    input_field = forms.CharField(label='Enter Something')
    # output_field = forms.CharField(label = 'Output', required=False)

from django import forms

class MyForm(forms.Form):
    title_input = forms.CharField(label='Title')
    # output_field = forms.CharField(label = 'Output', required=False)
    description_input = forms.CharField(
        label='Decription',
        max_length=30000000000000,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )


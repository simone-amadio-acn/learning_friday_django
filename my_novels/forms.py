from django import forms

class CreateForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=32)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=256)
    #body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=2048)
    genres = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-inline'})
    )

    def __init__(self, *args, **kwargs):
        genres = kwargs.pop('genres', None)
        super(CreateForm, self).__init__(*args, **kwargs)
        
        if genres is not None:
            self.fields['genres'].queryset = genres
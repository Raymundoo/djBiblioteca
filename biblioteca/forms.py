
class AutorSearchForm(forms.Form):
    """
    """
    q = forms.CharField(label="Buscador", max_length=50, required=False)
    
    def clean_q(self):
        min_words = 3
        data = self.cleaned_data["q"]
        if len(data.split()) < min_words:
            raise forms.ValidationError("Se requieren minimo {} palabras".format(min_words))
        return data
    
    

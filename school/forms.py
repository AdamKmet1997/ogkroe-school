from django.forms import ModelForm
from .models import Results

class ResultsForm(ModelForm):
    class Meta:
        model = Results
        fields = ['track_name','tier_number','date_raced','results_image']

    # track_name = forms.CharField(label='Track name', max_length=100)
    # tier_number = forms.IntegerField(label='Tier Number')
    # date_raced = forms.DateField(label='Date of the Race', widget=forms.SelectDateWidget)
    # results_image = forms.ImageField(label='Race Results')
from django.forms import ModelForm
from .models import Results


class ResultsForm(ModelForm):
    class Meta:
        model = Results
        fields = ["track_name", "tier_number", "date_raced", "results_image_url"]

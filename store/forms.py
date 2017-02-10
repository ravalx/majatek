from django import forms
from .models import NrStc


class AddStc(forms.ModelForm):
	#nr_stc = forms.CharField(max_length=9)
	#nazwa = froms.CharField(max_length=255)

	class Meta:
		model = NrStc
		fields = ['nr_stc','name', 'data_przyjecia']
		widgets = {
            'data_przyjecia': forms.DateInput(attrs={'id':'datepicker'}),
        }
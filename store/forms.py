from django import forms
from .models import NrStc, NrSt


class AddStc(forms.ModelForm):
	#nr_stc = forms.CharField(max_length=9)
	#nazwa = froms.CharField(max_length=255)

	class Meta:
		model = NrStc
		fields = ['nr_stc','name', 'data_przyjecia']
		widgets = {
            'data_przyjecia': forms.DateInput(attrs={'id':'datepicker'}),
            'uwagi': forms.CharField(widget=forms.Textarea),
        }

class AddSt(forms.ModelForm):
	class Meta:
		model = NrSt
		fields = ['nr_st', 'name', 'dzierzawca', 'place', 'price', 'data_przyjecia', 'uwagi']
		

		widgets = {
			'data_przyjecia': forms.DateInput(attrs={'id':'datepicker', 'class':'form-control'}),
			'price': forms.NumberInput(attrs={'type':'', 'class':'form-control'}),
			'nr_st': forms.TextInput(attrs={'class':'form-control'}),
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'place': forms.TextInput(attrs={'class':'form-control'}),
			'dzierzawca': forms.TextInput(attrs={'class':'form-control'}),
			'uwagi': forms.Textarea(attrs={'class':'form-control'}),
		}
	
	
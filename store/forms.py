from django import forms
from .models import NrStc, NrSt, Upload
import re


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

	def clean_price(self):
		price = self.cleaned_data['price']
		ok = re.match(r'^\d*\.\d{2}$', str(price))
		if not ok:
			raise forms.ValidationError('Podaj miejsca dziesiętne')
		return price

	def clean_nr_st(self):
		nr_st = self.cleaned_data['nr_st']
		if len(nr_st) < 9:
			raise forms.ValidationError('Numer ST jest za krótki!')
		ok = re.match(r'^\d+$', nr_st)
		if not ok:
			raise forms.ValidationError('Pole powinno zawierać tylko cyfry')
		return nr_st

class UploadFileForm(forms.ModelForm):
	class Meta:
		model = Upload
		fields = ['upload']
	#upload = forms.FileField()
	
	
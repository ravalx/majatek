from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import NrSt, NrStc
from django.urls import reverse_lazy
from .forms import AddStc, AddSt
from django.http import HttpResponse, HttpResponseRedirect

class CreateSt(CreateView):
	template_name = 'store/create-st.html'
	model = NrSt
	fields = ['owner', 'nr_st', 'name']
	success_url = '/'


class StListView(ListView):
	template_name = 'store/list-st.html'
	model = NrSt
	fields = ['owner', 'nr_st', 'name']


class ProductsListView(ListView):
	context_object_name = 'products-list'
	template_name = 'store/products-list.html'
	#queryset = NrSt.objects.
	def get_queryset(self):
		return NrSt.objects.filter(owner = self.request.user)

	def get_context_data(self, **kwargs):
		context = super(ProductsListView, self).get_context_data(**kwargs)
		context['numer_stc'] = NrStc.objects.all()
		return context
	

class StcListView(ListView):
	template_name = 'store/list-stc.html'
	model = NrStc
	fields = ['owner', 'nr_st', 'name', 'nr_stc', 'data_przyjecia']


class DelSt(DeleteView):
	template_name = 'store/delete-st.html'
	model = NrSt
	success_url = reverse_lazy('list-st')

'''class CreateStc(CreateView):
	model = NrStc
	template_name = 'store/create-stc.html'
	fields = ['nr_stc', 'name']
	'''
def add_stc(request, nr_st):

	if request.method == 'POST':
		form = AddStc(request.POST)
		if form.is_valid():
			stc = form.save(commit = False)
			stc.owner = request.user
			#stc.nr_st = request.NrSt.objects.filter(nr_st=pk)
			stc.nr_st = get_object_or_404(NrSt, nr_st = nr_st)
			stc.save()


	form = AddStc
	return render(request, 'store/create-stc.html', {'form':form})

def add_st(request):
	if request.method == 'POST':
		form = AddSt(request.POST)
		if form.is_valid():
			st = form.save(commit = False)
			st.owner = request.user
			st.save()
			return HttpResponseRedirect('/')
	form = AddSt
	return render(request, 'store/create-st.html', {'form':form})





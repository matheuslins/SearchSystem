from django.shortcuts import render
from django.views import generic
from .models import Box
import operator
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from functools import reduce
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import BoxForm

class ListBoxView(generic.ListView):
	template_name = 'core/index.html'
	queryset = Box.objects.all()
	context_object_name = 'boxes'
	paginate_by = 4

	def get_queryset(self):

		result = super(ListBoxView, self).get_queryset()
		box_search = self.request.GET.get('search', None)
		if box_search:
			query_list = box_search.split()
			result = result.filter(
			reduce(operator.and_,
				(Q(name__icontains=search) for search in query_list))
			)
		return result.order_by('create_date')

	def get_context_data(self, **kwargs):
		context = super(ListBoxView, self).get_context_data(**kwargs)
		list_box = Box.objects.all().order_by('create_date')

		paginator = Paginator(list_box, self.paginate_by)
		page = self.request.GET.get('page')

		try:
		    list_box = paginator.page(page)
		except PageNotAnInteger:
		    list_box = paginator.page(1)
		except EmptyPage:
		    list_box = paginator.page(paginator.num_pages)

		context['list_box'] = list_box

		return context

class CreateBoxView(generic.edit.CreateView):

	template_name = 'category/create.html'
	form_class = BoxForm
	success_url = reverse_lazy('core:list_box')

	def get_success_url(self):
		messages.success(self.request, 'Box created successfully!')
		return reverse_lazy('core:list_box')

class UpdateBoxView(generic.UpdateView):

	template_name = 'core/update.html'
	model = Box
	form_class = BoxForm

	def get_success_url(self):
		messages.success(self.request, 'Box updated successfully!')
		return reverse_lazy('core:update_box', kwargs={'slug' : self.object.slug})

class DeleteBoxView(generic.DeleteView):

	model = Box
	template_name = 'core/delete.html'

	def get_context_data(self, **kwargs):
		context = super(DeleteBoxView, self).get_context_data(**kwargs)
		context['box'] = self.object
		return context

	def get_success_url(self):
		messages.success(self.request,'Box deleted successfully!')
		return reverse_lazy('core:list_box')

from django.shortcuts import render
from django.views import generic
from .models import Box
import operator
from django.db.models import Q
from functools import reduce
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class IndexView(generic.ListView):
	template_name = 'core/index.html'
	queryset = Box.objects.all()
	context_object_name = 'boxes'
	paginate_by = 4

	def get_queryset(self):

		result = super(IndexView, self).get_queryset()
		box_search = self.request.GET.get('search', None)
		if box_search:
			query_list = box_search.split()
			result = result.filter(
			reduce(operator.and_,
				(Q(name__icontains=search) for search in query_list))
			)
		return result

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		list_box = Box.objects.all().order_by('name')

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


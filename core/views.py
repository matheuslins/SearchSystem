from django.shortcuts import render
from django.views import generic
from .models import Box
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class IndexView(generic.ListView):
	template_name = 'core/index.html'
	queryset = Box.objects.all()
	context_object_name = 'boxes'
	paginate_by = 4

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


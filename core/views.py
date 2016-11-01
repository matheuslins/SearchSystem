from django.shortcuts import render
from django.views import generic
from .models import *
from django.contrib import messages
import operator
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from functools import reduce
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
from .tasks import *
from datetime import datetime
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class ListBoxView(generic.ListView):
	template_name = 'core/index.html'
	queryset = Box.objects.all()
	context_object_name = 'boxes'
	paginate_by = 500

	def get_queryset(self):

		result = super(ListBoxView, self).get_queryset()
		box_search = self.request.GET.get('search', None)
		if box_search:
			query_list = box_search.split()
			result = result.filter(
			reduce(operator.and_,
				(Q(name__icontains=search) for search in query_list))
			)
		return result.order_by('name')

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
		context['four_lasted'] = self.queryset.order_by('-id')[:4]

		return context

class CreateBoxView(generic.edit.CreateView):

	template_name = 'core/create.html'
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
		return reverse_lazy('core:update_box', kwargs={'pk' : self.object.pk})

	@receiver(post_save, sender=Box)
	def put(sender, instance, *args, **kwargs):
		register_update_box = BoxLog.objects.create(box=instance, datetime=datetime.now(), status=2)
		register_update_box.date_update=datetime.now()
		register_update_box.save()
		return register_update_box

class DeleteBoxView(generic.DeleteView):

	model = Box
	template_name = 'core/delete.html'

	def get_context_data(self, **kwargs):
		context = super(DeleteBoxView, self).get_context_data(**kwargs)
		context['box'] = self.object
		return context

	def get_success_url(self, *args, **kwargs):
		import json
		from django.forms.models import model_to_dict
		box = self.object
		box_dic = model_to_dict(box)
		create_log_delete_box.delay(json.dumps(box_dic), *args, **kwargs)
		return reverse_lazy('core:list_box')

class DetailBoxView(generic.DetailView):

	model = Box
	context_object_name = 'boxes'
	template_name = 'core/view.html'

	def get_context_data(self, **kwargs):
		context = super(DetailBoxView, self).get_context_data(**kwargs)
		context['box'] = self.object
		return context

class LogView(generic.ListView):

	template_name = 'core/log.html'
	queryset = BoxLog.objects.all()
	context_object_name = 'logs'
	paginate_by = 500

	def get_queryset(self):

		result = super(LogView, self).get_queryset()
		box_search = self.request.GET.get('search', None)
		if box_search:
			query_list = box_search.split()
			result = result.filter(
			reduce(operator.and_,
				(Q(box__name__icontains=search) for search in query_list))
			)
		return result.order_by('datetime')

	def get_context_data(self, **kwargs):
		context = super(LogView, self).get_context_data(**kwargs)
		list_box_log = BoxLog.objects.all().order_by('create_date')

		paginator = Paginator(list_box_log, self.paginate_by)
		page = self.request.GET.get('page')

		try:
		    list_box_log = paginator.page(page)
		except PageNotAnInteger:
		    list_box_log = paginator.page(1)
		except EmptyPage:
		    list_box_log = paginator.page(paginator.num_pages)

		context['list_box_log'] = list_box_log

		return context

@receiver(post_save, sender=Box)
def create_log_add_box(sender, **kwargs):
	box_log = BoxLog.objects.create(box=kwargs.get('instance'), datetime = datetime.now(), status=1)
	return box_log

from celery import shared_task, task


baixar_dados_api.delay()


# from django.shortcuts import render
# from .models import Box
# import operator
# from django.db.models import Q
# from django.core.urlresolvers import reverse_lazy
# from rest_framework.renderers import TemplateHTMLRenderer
# from functools import reduce
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from .serializers import BoxSerializer
# from rest_framework import generics

# class ListBox(generics.ListCreateAPIView):

# 	renderer_classes = [TemplateHTMLRenderer]
# 	template_name = 'core/index.html'
# 	queryset = Box.objects.all()
# 	serializer_class = BoxSerializer
# 	# paginator = 4

# 	def get_queryset(self):

# 		result = super(ListBox, self).get_queryset()
# 		box_search = self.request.GET.get('search', None)
# 		if box_search:
# 			query_list = box_search.split()
# 			result = result.filter(
# 			reduce(operator.and_,
# 			(Q(name__icontains=search) for search in query_list)))
# 		return result

# 	def get_serializer_context(self):
# 		context = super(ListBox, self).get_serializer_context()
# 		return context

	# def paginate_queryset(self, queryset):

	# 	paginator = Paginator(self.queryset, self.paginator)
	# 	page = self.request.GET.get('page')

	# 	try:
	# 		self.queryset = paginator.page(page)
	# 	except PageNotAnInteger:
	# 		self.queryset = paginator.page(1)
	# 	except EmptyPage:
	# 		self.queryset = paginator.page(paginator.num_pages)

	# 	return page


# class BoxDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Box.objects.all()
#     serializer_class = BoxSerializer

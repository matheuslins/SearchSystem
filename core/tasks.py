from __future__ import absolute_import

from celery import shared_task, task
from datetime import timedelta
from celery.task.schedules import crontab
from celery.decorators import periodic_task, task
from core.models import Box

# class BoxTask(Task):
# 	@task
# 	@shared_task
# 	@periodic_task(run_every=timedelta(seconds=2))
# 	def add_box(request, id, name):
# 		context = {}
# 		url = 'http://uinames.com/'
# 		template_name = 'core/create.html'
# 		if request.method == "POST":
# 			form = BoxForm(request.POST or None)
# 			form.name = 'Caixa'
# 			if form.is_valid():
# 				form.save()
# 			else:
# 				form = BoxForm()
# 		context['form'] = form
# 		return render(request, template_name, context)


@task(name="collect_perfis")
@task(ignore_result=True)
def collect_perfis(perfil_id):
	try:
		box = Box.objects.get(numero=perfil_id)
	except Box.DoesNotExist:
		item = 'http://uinames.com/api/'
		item_object = Box()
		item_object.name = 'Caixa'
		item_object.number = 11
		item_object.save()

	return

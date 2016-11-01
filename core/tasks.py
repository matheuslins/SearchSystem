from __future__ import absolute_import

from celery import shared_task, task
from datetime import timedelta
from celery.task.schedules import crontab
from celery.decorators import periodic_task, task
from core.models import Box

@shared_task
@periodic_task(run_every=(crontab()), name="baixar_dados_api", ignore_result=True)
def baixar_dados_api():
	import urllib.request
	import json

	r = urllib.request.urlopen('http://uinames.com/api/?amount=25').read().decode('utf8')
	r = json.loads(r)
	numero = 0
	new_box = None
	for value in r:
		new_box = Box.objects.create(name=value['name'], number=numero, content=value['region'])
		numero = numero + 1
	return new_box

@shared_task
def create_log_delete_box(sender, instance, *args, **kwargs):
	register_delete_box = BoxLog.objects.create(box=instance, datetime=datetime.now(), status=3)
	return register_delete_box
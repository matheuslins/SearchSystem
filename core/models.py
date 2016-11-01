from django.db import models

class Box(models.Model):
	name = models.CharField('Nome', max_length=100)
	number = models.IntegerField('Número', default=0)
	content = models.TextField('Content', blank = True)
	create_date = models.DateField('Creation Date', auto_now_add=True)
	date_update = models.DateTimeField(blank=True, null=True)

	class Meta:
		verbose_name = 'Box'
		verbose_name_plural = 'Boxes'

class BoxLog(models.Model):

	STATUS_CHOICES = (
		(0, 'Null'),
		(1, 'Criado'),
		(2, 'Atualizado'),
		(3, 'Deletado'),
		(4, 'Visualizado'),
	)

	box = models.ForeignKey(Box, verbose_name="Box Log", related_name='log_box')
	datetime = models.DateTimeField("Date and Time of action", auto_now_add=True)
	status = models.IntegerField('Status', choices=STATUS_CHOICES, default=0, blank=True)

	class Meta:
		verbose_name = 'Box Log'
		verbose_name_plural = 'Boxes Logs'
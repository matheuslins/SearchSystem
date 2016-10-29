from django.db import models
from autoslug.fields import AutoSlugField

class Box(models.Model):
	name = models.CharField('Nome', max_length=100)
	slug = AutoSlugField("Slug",populate_from='name',unique=True)
	create_date = models.DateField('Creation Date', auto_now_add=True)

	class Meta:
		verbose_name = 'Box'
		verbose_name_plural = 'Boxes'

	def __init__(self, arg):
		super(Box, self).__init__()
		self.name = arg
		

class BoxLog(models.Model):
	box = models.ForeignKey(Box, verbose_name="Box Log", related_name='log_box')
	datetime = models.DateTimeField("Date and Time of action", auto_now_add=True)

	class Meta:
		verbose_name = 'Box Log'
		verbose_name_plural = 'Boxes Logs'
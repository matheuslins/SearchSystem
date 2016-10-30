from .models import Box, BoxLog
from rest_framework import serializers


class BoxLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = BoxLog
		fields = ('datetime')

class BoxSerializer(serializers.ModelSerializer):
	log_box = BoxLogSerializer(many=True, required=False)

	class Meta:
		model = Box
		fields = ('name', 'number', 'content','log_box')

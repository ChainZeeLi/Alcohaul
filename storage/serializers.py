from rest_framework import serializers
from django.db import models
from .models import alcohol, store

class alcoholSerializer(serializers.ModelSerializer):

	class Meta:
		model = alcohol
		fields = '__all__'


class storeSerializer(serializers.ModelSerializer):

	class Meta:
		model = store
		fields = '__all__'



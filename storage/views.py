from django.shortcuts import get_object_or_404 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import alcohol
from .serializers import alcoholSerializer, storeSerializer
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
# List all booze or create a new one
# alcohol/
def index(request):
	all_alcohol = alcohol.objects.all()
	template = loader.get_template("storage/index.html")
	context = {'all_alcohol': all_alcohol}
	return render(request, "storage/index.html", context)



def detail(request, alcohol_name):
	return HttpResponse("<h2>Details for alcohol: " + str(alcohol_name)  + "</h2>")




class alcoholList(APIView):

	def get(self, request):
		Alcohol = alcohol.objects.all()
		serializers = alcoholSerializer(Alcohol, many=True)

		return Response(serializers.data)

	def post(self, request, alcohol):

		pass


class storeList(APIView):

	def get(self, request):
		Store = store.objects.all()
		serializers = storeSerializer(Store, many=True)

		return Response(serializers.data)

	def post(self):
		pass
"""
class alcoholSearch(APIView):


	def get(self, request):


	def post(self):
"""












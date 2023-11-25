from django.shortcuts import render
from django.http import JsonResponse
from .models import Technicians
from .serializers import TechnicainSerializer,UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET','POST'])
def TechnicainsList(request):
    if request.method=='GET':
        print("entered here")
        technicians=Technicians.objects.all()
        serailizer=TechnicainSerializer(technicians, many=True)
        return Response(serailizer.data)
    elif request.method=='POST':
        serailizer=TechnicainSerializer(data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data)
        else:
            return Response(serailizer.errors)
        
@api_view(['GET','PUT','DELETE'])
def TechnicainDetailView(request,pk):
    try:
        techinican=Technicians.objects.get(pk=pk)
    except Technicians.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method=='GET':
        tecnincan=Technicians.objects.get(pk=pk)
        print(tecnincan)
        serailizer=TechnicainSerializer(tecnincan)
        return Response(serailizer.data)
    
    elif request.method=='PUT':
        serailizer=TechnicainSerializer(techinican,data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data)
        else:
            return Response(serailizer.errors)
            
    elif request.method=='DELETE':
        techinican.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def Userslist(request):
    if request.method=='GET':
        user=User.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)
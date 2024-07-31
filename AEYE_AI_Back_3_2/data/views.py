from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import InitiateAI_Serializer, Image_Serializer
from colorama import Fore, Back, Style

SUCCESS = Fore.GREEN + "AI - [SUCCESS]" + Fore.RESET
ERROR = Fore.RED + "AI - [ERROR]" + Fore.RESET

class AI_Test_View(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def post (self, request, *args, **kwargs) :
        print(SUCCESS, "Received Data From Client _ Test")
        serializer = InitiateAI_Serializer(data = request.data)


        if serializer.is_valid() :

            serializer.save()

            print(SUCCESS, "Start AI Test")
            

            return Response("Reeived Well", status=200)
        else:
            print(ERROR, "Start AI Test")
            return Response("Received Wrong Data!", status=400)
        

class AI_Train_View(APIView):
    print(SUCCESS, "Received Data From Client _ Train")
    parser_classes = (MultiPartParser, FormParser)
    
    def post (self, request, *args, **kwargs) :
        serializer = InitiateAI_Serializer(data = request.data)


        if serializer.is_valid() :

            serializer.save()

            print(SUCCESS, "Start AI Train")
            

            return Response("Reeived Well", status=200)
        else:
            print(ERROR, "Start AI Train")
            return Response("Received Wrong Data!", status=400)


class AI_Inference_View(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post (self, request, *args, **kwargs) :
        print(SUCCESS, "Received Data From Client _ Inference")
        serializer = Image_Serializer(data = request.FILES)

        if serializer.is_valid() :

            serializer.save()

            print(SUCCESS, "Start AI Inference")
            

            return Response("Reeived Well", status=200)
        else:
            print(ERROR, "Start AI Inference")
            return Response("Received Invalid Data!", status=400)
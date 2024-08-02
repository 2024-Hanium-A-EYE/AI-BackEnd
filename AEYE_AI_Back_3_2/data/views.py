from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import InitiateAI_Serializer, Image_Serializer
from colorama import Fore, Back, Style
import os
import requests
import json
from .models import Initiate_AI_Model

SUCCESS = Fore.GREEN + "[AI Back - SUCCESS]" + Fore.RESET
ERROR   = Fore.RED   + "[AI Back - ERROR]"   + Fore.RESET

def print_log(status, message, method) :
    if status == 'SUCCESS' :
        print('-----------------------------------------')
        print(SUCCESS, message, Fore.BLUE + method + Fore.RESET)
        print('-----------------------------------------')
    elif status == "ERROR" :
        print('-----------------------------------------')
        print(ERROR, message, Fore.BLUE + method + Fore.RESET)
        print('-----------------------------------------')

def print_log_data(data) :
    print(f"Received: {data}")

##################################################################################
# AI

# /api/ai-test/
class AI_Test_View(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def post (self, request, *args, **kwargs) :
        print_log('SUCCESS', 'Received Data From Client', '[TEST]')

        serializer = InitiateAI_Serializer(data = request.data)

        if serializer.is_valid() :

            serializer.save()
            print_log('SUCCESS', "Start AI Test", '[TEST]')
            
            # AI Test 통신 #

            ###############

            return Response("Reeived Well", status=200)
        else:
            print_log('ERROR', "Start AI Test", '[TEST]')
            return Response("Received Wrong Data!", status=400)
        

# /api/ai-train/
class AI_Train_View(APIView):
    print_log('SUCCESS', "Received Data From Client", '[TRAIN]')
    parser_classes = (MultiPartParser, FormParser)
    
    def post (self, request, *args, **kwargs) :
        serializer = InitiateAI_Serializer(data = request.data)


        if serializer.is_valid() :

            serializer.save()

            print_log('SUCCESS', "Start AI Train", '[TRAIN]')
            
            # AI Train 통신 #

            #################

            return Response("Reeived Well", status=200)
        else:
            print_log('ERROR', "Start AI Train", '[TRAIN]')
            return Response("Received Wrong Data!", status=400)


# /api/ai-inference/
class AI_Inference_View(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post (self, request, *args, **kwargs) :
        print_log('SUCCESS', 'Received Data From Client', '[INFERENCE]')
        print_log_data(request.data)
        serializer = InitiateAI_Serializer(data = request.data) # doing Test #char
        print_log('SUCCESS', "RECEIVED WELL", '[INFERENCE]')

        if serializer.is_valid() :
            print_log('SUCCESS', "Start AI Inference", '[INFERENCE]')

            serializer.save()
            
            ################ AI Inference 통신 ####################
            server_url = 'http://127.0.0.1:3000/api/ai-inference'
            

            # 현재 디렉토리 경로
            current_dir = os.path.dirname(__file__)
            image_path = os.path.join(current_dir, '0.png')

            # 파일을 열고 POST 요청을 보냄.
            with open(image_path, 'rb') as image_file:
                files = {'file' : image_file}
                data = {'name': 'good'}

                response = requests.post(server_url, data=data, files=files)

            ######################################################

            return Response(response, status=200)
        else:
            print_log('ERROR', "Start AI Inference", '[INFERENCE]')
            return Response("Received Invalid Data!", status=400)
        


##################################################################################
# Developing

# /api/develop/
class Developing_View(APIView) :
    parser_classes = (MultiPartParser, FormParser)

    def post (self, request, *args, **kwargs) :
        print_log('SUCCESS', f"Received Data From Client", '[DEVELOP]')
        serializer = InitiateAI_Serializer(data = request.data) # doing Test #char
        print_log('SUCCESS', "RECEIVED WELL",'[DEVELOP]')

        if serializer.is_valid() :
            print_log('SUCCESS', "Start AI Inference", '[DEVELOP]')

            serializer.save()
            
            ################ AI Inference 통신 ####################
            server_url = 'http://127.0.0.1:3000/api/ai-inference'
            

            # 현재 디렉토리 경로
            current_dir = os.path.dirname(__file__)
            image_path = os.path.join(current_dir, '0.png')

            # 파일을 열고 POST 요청을 보냄.
            with open(image_path, 'rb') as image_file:
                files = {'file' : image_file}
                data = {'name': 'good'}

                response = requests.post(server_url, data=data, files=files)

            ######################################################

            return Response(response, status=200)
        else:
            print_log('ERROR', "Start AI Inference", '[DEVELOP]')
            return Response("Received Invalid Data!", status=400)
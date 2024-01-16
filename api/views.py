from django.shortcuts import render
from rest_framework import generics
from api.models import User
from api.serializers import UserSerializer
from api.utils.response import response
from rest_framework.parsers import JSONParser

class UserGeneralView(generics.GenericAPIView):
    def get(self, request):
        data = User.objects.all()
        user_serialize = UserSerializer(data, many=True).data
        return response(user_serialize)
    
    def post(self, request):
        body = JSONParser().parse(request)
        user_serialize = UserSerializer(data=body)
        if user_serialize.is_valid():
            user_serialize.save()
            return response("save success")
        return response("dont meet object requirements", 400)
    
    def patch(self, request):
        body = JSONParser().parse(request)
        try:
            selectedID = User.objects.get(id=body["id"])
        except User.DoesNotExist: return response("ids not found", 400)
        user_serialize = UserSerializer(selectedID, data=body)
        if user_serialize.is_valid():
            user_serialize.save()
            return response("update success")
        return response("update failed", 400)
    
class UserParamsView(generics.GenericAPIView):
    def get(self, request, pk):
        try: 
            data = User.objects.get(pk=pk)
        except User.DoesNotExist : response("ids not found", 400)  
        user_serialize = UserSerializer(data).data
        return response(user_serialize)
    def delete(self, request, pk):
        try: 
            data = User.objects.get(pk=pk)
        except User.DoesNotExist : response("ids not found", 400)
        data.delete()
        return response("delete success")
        









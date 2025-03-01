from django.shortcuts import render
from django.views.generic import View
from .models import Candidate
from .serializers import CandidateSerializer, CandidatePostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class CandidateView(APIView):
    """
    Candidate view class
    """
    
    def get(self, request):
        """
        Candidate get operation
        """
        
        candidate_id = request.GET.get('id')
        if candidate_id:
            candidate = Candidate.objects.get(id=candidate_id)
            serializer = CandidateSerializer(data=candidate)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            candidates = Candidate.objects.all()
            serializer = CandidateSerializer(candidates, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        """
        Candidate delete operation
        """
        
        candidate_id = request.GET.get('id')
        candidate = Candidate.objects.get(id=candidate_id)
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request):
        """
        Candidate put operation
        """
        
        serializer = CandidatePostSerializer(data=request.data)
        if serializer.is_valid():
            candidate = Candidate.objects.get(id=serializer.data['id'])
            candidate.name = serializer.data['name']
            candidate.age = serializer.data['age']
            candidate.gender = serializer.data['gender']
            candidate.email = serializer.data['email']
            candidate.phone = serializer.data['phone']
            candidate.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CandidateListView(APIView):
    """
    Candidate list view class
    """
    
    def post(self, request):
        """
        Candidate post operation
        """
        
        serializer = CandidatePostSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
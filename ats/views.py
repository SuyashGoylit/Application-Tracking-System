from django.shortcuts import render
from django.views.generic import View
from django.contrib.postgres.search import TrigramSimilarity
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Candidate
from .serializers import CandidateSerializer, CandidatePostSerializer

# Create your views here.

class CandidateView(APIView):
    """
    Candidate view class
    """
    
    def get(self, request, id):
        """
        Candidate get operation
        """
        
        try:
            candidate = Candidate.objects.get(id=id)
            serializer = CandidateSerializer(candidate)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"message": "Candidate ID not found in the database"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        """
        Candidate delete operation
        """
        
        try:
            candidate = Candidate.objects.get(id=id)
            candidate.delete()
            return Response({"message": "Candidate deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        
        except Exception as e:
            return Response({"message": "Candidate ID not found in the database"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        """
        Candidate put operation
        """
        
        try:
            candidate = Candidate.objects.get(id=id)
            
        except Exception as e:
            return Response({"message": "Candidate ID not found in the database"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CandidatePostSerializer(candidate, data=request.data)
        
        if serializer.is_valid():
            
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
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
            
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        """
        Candidates get operation
        """
        
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class CandidateSearchView(APIView):
    """
    Candidate search view class
    """
    
    def get(self, request):
        """
        Candidate search operation
        """
        
        query = request.GET.get("name", "").strip()
        
        if not query:
            return Response({"message": "Search query cannot be empty"}, status=status.HTTP_400_BAD_REQUEST)

        candidates = Candidate.objects.annotate(
            similarity=TrigramSimilarity('name', query)
        ).filter(similarity__gt=0.1).order_by('-similarity')
        
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
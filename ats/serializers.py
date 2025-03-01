from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    """
    Candidate serializer class
    """
    
    class Meta:
        model = Candidate
        fields = '__all__'
        
class CandidatePostSerializer(serializers.Serializer):
    """
    Candidate post serializer class
    """
    
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    gender = serializers.ChoiceField(choices=['male', 'female', 'other'])
    email = serializers.EmailField(max_length=100)
    phone = serializers.CharField(max_length=15)
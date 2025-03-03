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
    
    def create(self, validated_data):
        return Candidate.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance
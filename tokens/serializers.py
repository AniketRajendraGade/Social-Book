from rest_framework import serializers
from myapp.models import CustomUser,Books

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields = ['id', 'user_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['title', 'description', 'visibility', 'cost', 'year_publish', 'file']
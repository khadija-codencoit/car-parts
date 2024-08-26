from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        extra_kwargs = {
            'password' : {'write_only':True}
        }
        
        def create(self,validated_data):
            user=user.object.create_user(**validated_data)
            password = validated_data.get('password')
            user.set_password(password)
            user.save()
            return user
        
        
    
        
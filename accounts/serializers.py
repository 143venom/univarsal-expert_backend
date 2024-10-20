# from django.contrib.auth import get_user_model

# from rest_framework import serializers

# from .models import CustomUser

# User = get_user_model()


# class UserRegisterSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ('first_name', 'last_name', 'email', 'password', 'confirm_password')
#         extra_kwargs = {
#             'password': {'write_only': True},
#             'confirm_password': {'write_only': True},
#         }

#     def validate(self, data):
#         if data['password'] != data['confirm_password']:
#             raise serializers.ValidationError({"confirm_password": "Passwords must match."})
#         return data

#     def create(self, validated_data):
#         validated_data.pop('confirm_password')

#         user = CustomUser(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
    

# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         email = data.get('email')
#         password = data.get('password')

#         if not User.objects.filter(email=email).exists():
#             raise serializers.ValidationError({"email": "User with this email does not exist."})

#         user = User.objects.get(email=email)
#         if not user.check_password(password):
#             raise serializers.ValidationError({"password": "Incorrect password."})
        
#         return data
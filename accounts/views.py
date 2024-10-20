# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import UserRegisterSerializer, UserLoginSerializer
# from django.contrib.auth import get_user_model

# User = get_user_model()


# class UserViewSet(viewsets.ViewSet):
#     def create(self, request):
#         serializer = UserRegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def login(self, request):
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 user = User.objects.get(email=serializer.validated_data['email'])
#                 if user.check_password(serializer.validated_data['password']):
#                     refresh = RefreshToken.for_user(user)
#                     return Response({
#                         'refresh': str(refresh),
#                         'access': str(refresh.access_token),
#                     })
#                 return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#             except User.DoesNotExist:
#                 return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
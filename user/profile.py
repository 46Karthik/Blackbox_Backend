# from django.shortcuts import get_object_or_404,redirect
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .serializers import profileSerializer
# from .models import Profile
# from rest_framework import status

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def profile(request, username=None):
#     # stored_value = request.session.get('username')
#     # if stored_value:
#        if request.method == 'GET':
#         # print(stored_value,"profile")
#         if username:
#             # Retrieve data for a specific user by username
#             profile = get_object_or_404(Profile, username=username)
#             serializer = profileSerializer(profile)
#         else:
#             # Retrieve data for all profiles
#             profiles = Profile.objects.all()
#             serializer = profileSerializer(profiles, many=True)
#         return Response(serializer.data)

#        elif request.method == 'POST':
#         # Handle POST request to create new data
#         serializer = profileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()  # Save the data to the database
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#        elif request.method == 'PUT':
#         # Handle PUT request to update the profile
#         if username:
#             profile = get_object_or_404(Profile, username=username)
#             serializer = profileSerializer(profile, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({"error": "Username not provided."}, status=status.HTTP_400_BAD_REQUEST)

#        elif request.method == 'DELETE':
#         # Handle DELETE request to delete the profile
#         if username:
#             profile = get_object_or_404(Profile, username=username)
#             profile.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response({"error": "Username not provided."}, status=status.HTTP_400_BAD_REQUEST)
#     # else:
#     #     return redirect('login')
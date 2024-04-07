from django.shortcuts import get_object_or_404,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import storesongSerializer
from .models import Storesong
from rest_framework import status

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def storesong(request, id=None):
    # stored_value = request.session.get('username')
    # if stored_value:
       if request.method == 'GET':
        # print(stored_value,"profile")
        if id:
            # Retrieve data for a specific user by username
            profile = get_object_or_404(Storesong, id=id)
            serializer = storesongSerializer(profile)
        else:
            # Retrieve data for all profiles
            profiles = Storesong.objects.all()
            serializer = storesongSerializer(profiles, many=True)
        return Response(serializer.data)

       elif request.method == 'POST':
        # Handle POST request to create new data
        serializer = storesongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


       elif request.method == 'DELETE':
        # Handle DELETE request to delete the profile
        if id:
            profile = get_object_or_404(Storesong, id=id)
            profile.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "Username not provided."}, status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     return redirect('login')
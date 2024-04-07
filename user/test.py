from rest_framework.decorators  import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404 
from .data import file

@api_view(['GET'])
def test(request):
    if request.method == 'GET':
        print("found",file)
        return Response(file)

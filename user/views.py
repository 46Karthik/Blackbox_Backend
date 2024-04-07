# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import User,Profile
# from .serializers import UserSerializer,profileSerializer
# from rest_framework.decorators import api_view
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# from django.shortcuts import render,redirect
# # from .index.html improt finaldata
# import secrets
# @api_view(["GET"])
# def login(request):
#     if request.method =="GET":
#         # finaldata = "This is the data I want to pass to the template."
#         # context = {
#         # 'finaldata': finaldata,
#         #  }
#       return render(request, 'loginpage.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username,"found")
#         print(password,"found")
#         # Perform authentication or other processing with username and password here
#         if username:
#             getusername =get_object_or_404(Profile,username=username)
#             userinfo =profileSerializer(getusername).data
#             user_name_in_db =userinfo.get("username")
#             user_pass_in_db =userinfo.get("password")
#             # print(user_name_in_db,user_pass_in_db)
#         if username == user_name_in_db and password == user_pass_in_db:
#             request.session['username'] = 'auth01'
#             stored_value = request.session.get('username')
#             # Authentication successful, you can redirect the user to a different page
#             print(stored_value,"trueeeeeeeeeeeee")
#             return redirect('name/')
#         else:
#             # Authentication failed, you can set an error message
#             error_message = 'Invalid username or password'
#             return render(request, 'loginpage.html', {'error_message': error_message})
#     else:
#         # Handle GET request (display the login form)
#         return render(request, 'loginpage.html')

# def generate_api_key(length=32):
#     secrets_api_key = secrets.token_hex(length)
#     return secrets_api_key

# @api_view(['GET'])
# def example_view(request,userid):
#     api_key = request.GET.get('api_key', '')
#     if request.method == 'GET':
#         if userid:
#             found = get_object_or_404(User,userid=userid)
#             serializer = UserSerializer(found).data
#             keyfound = serializer.get("apikey")
#             # return Response(serializer, status=status.HTTP_200_OK)
#             if keyfound == api_key:
#                 profile = get_object_or_404(Profile, id=userid)
#                 finaldata = profileSerializer(profile).data
#                 return Response(finaldata, status=status.HTTP_200_OK)
#             else:
#                 response = HttpResponse(f"Error = api_key is Wrong")
#                 return response


#     # response = HttpResponse(f"API Key: {api_key},{id},{key}")
#     # return response
# @api_view(['GET'])
# def apidetails(request,userid=None):
#     print("data found")
#     if request.method == 'GET':
#         if userid:
#             # Retrieve data for a specific user by username
#             found = get_object_or_404(User,userid=userid)
#             serializer = UserSerializer(found).data
#             # print(serializer.data,"dataaaaaaaaaaaa")
#             return Response(serializer, status=status.HTTP_200_OK)
#             # return Response(serializer.data)
#             # print(userid)
#         # else:
#         #     # Retrieve data for all profiles
#         #     profiles = Profile.objects.all()
#         #     serializer = profileSerializer(profiles, many=True)
        

# class UserCreate(APIView):
#     def post(self, request):
#         data = request.data
#         userid = data.get('userid')
#         apikey  = data.get('apikey')
#         # 1st type to create data
#         # user = User.objects.create(name=name)

#         #2st type to create data
#         # user = User()
#         # user.name = name
#         # user.save()
#         #3st type to create data
#         user = User(userid=userid,apikey=apikey)
#         user.save()
    

#         output = {
#            "userid": user.userid,
#            "apikey": user.apikey
#         }
#         # print(name)
#         # Return a success response with the created user's data
#         # return Response({'message': 'User created successfully', 'user_id': user.id}, status=status.HTTP_201_CREATED)
#         return Response(data=output, status=status.HTTP_201_CREATED)
#     # def get(self, request):
#     #     userdata = User.objects.all()
#     #     data =UserSerializer(userdata,many=True).data
#     #     # serialized_data = data
#     #     return Response(data=data, status=status.HTTP_200_OK)

#     # def put(self, request):
#     # def post(self, request):
# Import necessary modules
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

# Define your Telegram Bot API settings
BOT_TOKEN = '6474858446:AAHElOYHNgdMzq5UZv7zq3wOrqzq9ZickBY'  # Replace with your Telegram Bot token
BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

# Define your Django view to handle file uploads
@api_view(['POST'])
def upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        print(uploaded_file,"got it")
        # Define the chat ID where you want to send the file
        chat_id = '1301942955' # Replace with your chat ID
        
        # Send the file using the Telegram Bot API
        result = send_file(chat_id, uploaded_file, caption="Uploaded File")
        if result:
            return Response({"message": "File sent successfully!"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to send file."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)

# Function to send a file using the Telegram Bot API
def send_file(chat_id, file_data, caption=None):
    url = BASE_URL + 'sendDocument'
    params = {'chat_id': chat_id, 'caption': caption}
    files = {'document': file_data}
    try:
        response = requests.post(url, params=params, files=files)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error sending file: {e}")
        return None

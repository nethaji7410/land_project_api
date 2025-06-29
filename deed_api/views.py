from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ExcelData
from rest_framework import status
from .models import FieldPosition
from .serializers import FieldPositionSerializer
from rest_framework.permissions import  IsAuthenticated

# Create your views here.

# Get distinct tag names from ExcelData table
class TagListView(APIView):

    # permission_classes = [AllowAny]

    def get(self, request):
        tags = ExcelData.objects.values_list('tag_name', flat=True).distinct()
        return Response({'tags': list(tags)})


# Get unique document names under a specific tag
class DocumentNameListView(APIView):
    

    # permission_classes = [AllowAny] 

    def get(self, request, tag_name):
        documents = ExcelData.objects.filter(tag_name=tag_name)\
                    .values_list('document_name', flat=True).distinct()
        
        # Return error if no documents found
        if not documents:
            return Response({'message': 'No documents found for this tag.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'documents': list(documents)})
    

class SavePositionView(APIView):

    # permission_classes = [AllowAny]

    def post(self, request):
        data = request.data

        # If only one object is sent, convert to list
        if isinstance(data, dict):
            data = [data]

        # Validate and save using serializer
        serializer = FieldPositionSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Field positions saved."}, status=status.HTTP_201_CREATED)
         # Return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ResetPositionView(APIView):
    # permission_classes = [AllowAny]

    def post(self, request):
        # Delete all saved field positions
        FieldPosition.objects.all().delete()
        return Response({"message": "All field positions have been reset to default."}, status=status.HTTP_200_OK)
    

class LogoutView(APIView):
    permission_classes = [IsAuthenticated] # Only logged-in users can logout

    def post(self, request):
        try:
            # Delete the current user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logout'}, status=status.HTTP_200_OK)
        except Exception as e:
            # Return error if something fails
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
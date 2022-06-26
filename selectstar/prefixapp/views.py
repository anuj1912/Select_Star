from .serializers import PrefixSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class PrefixList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def post(self, request):
        serializer = PrefixSerializer(data=request.data)
        prefix = ''
        di_prefix = {}
        list_data = request.data.get('data_li')
        if list_data == []:
            return Response({"error":"List cannot be empty"}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            for group in zip(*list_data):
                if not all(char == group[0] for char in group):
                    break
                prefix += group[0]
            if prefix not in di_prefix:
                di_prefix[prefix] = list_data
            return Response(di_prefix, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.response import Response
from rest_framework.views import APIView

class AdultStudentsView(APIView):
    def get(self, request):
        adults = Student.objects.filter(age.__gt=18)
        serializer = StudentSerializer(adults , many="True")
        return Response(serializer.data)

from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Testing API View"""

    def get(self, request, format=None):
        """Returns a list of features of APIView"""
        features = ["Effiecient", "Good and responsive", "Robust"]

        return Response({"message": "features of API", "features": features})

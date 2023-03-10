from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api.serializers import HelloSerializer


class HelloApiView(APIView):
    """Testing API View"""

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Returns a list of features of APIView"""
        features = ["Effiecient", "Good and responsive", "Robust"]

        return Response({"message": "features of API", "features": features})

    def post(self, request):
        """Create a serializer to valid the name of the user"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handling put request"""
        return Response({"method": "put"})

    def patch(self, request, pk=None):
        """Handling Patch request"""
        return Response({"method": "patch"})

    def delete(self, request, pk=None):
        """Deleting an object in the database"""
        return Response({"method": "Delete"})


class ViewSet(viewsets.ViewSet):
    """Create the CRUD using ViewSet class"""

    serializer_class = HelloSerializer

    def list(self, request):
        """Return a list of users"""
        users = ["Ahmad", "Essa", "Mohammad"]

        return Response({"message": "users", "names": users})

    def create(self, request):
        """Create a new user"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name} from ViewSet"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieving an object by the pk"""
        return Response({"message": "Retrieve an object"})

    def update(self, request, pk=None):
        """Updating an object"""
        return Response({"message": "Updating an object"})

    def partial_update(self, request, pk=None):
        """Updating a part of an object"""
        return Response({"message": "Updating a part of an object"})

    def destroy(self, request, pk=None):
        """Deleting an object"""
        return Response({"message": "Deleting an object"})

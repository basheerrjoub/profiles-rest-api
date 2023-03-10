from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """A serializer to serialize the helloAPI model"""

    name = serializers.CharField(max_length=10)

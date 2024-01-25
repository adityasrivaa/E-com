from rest_framework import serializers

from . models import *

# Serializers define the API representation.
class User_RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_Registration
        fields = '__all__'
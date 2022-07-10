
from rest_framework import serializers
from .models import *

class ProgramListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class PartnersListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'

class ConferenceListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = ("id","background", "title", "tagline")

class ConferenceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        exclude = ('draft',)
        
    speakers = serializers.SlugRelatedField(slug_field="name", read_only=True,many=True)
    program = ProgramListSerializers(many=True)
    partners = PartnersListSerializers(many=True)


class CreateRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = "__all__"

class CreateWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"
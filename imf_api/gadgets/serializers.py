from rest_framework import serializers
from .models import Gadget
from .utils import generate_success_probability

class GadgetSerializer(serializers.ModelSerializer):
    success_probability = serializers.SerializerMethodField()

    class Meta:
        model = Gadget
        fields = ['id', 'codename', 'name', 'status', 'decommissioned_at', 'success_probability']

    def get_success_probability(self, obj):
        return generate_success_probability()


class GadgetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gadget
        fields = ['name', 'status']

    def create(self, validated_data):
        from .utils import generate_codename
        validated_data['codename'] = generate_codename()
        return super().create(validated_data)

from rest_framework import serializers
from main.models import *


class WizardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wizard
        fields = ['name', 'code']


class OptionLocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionLocal
        fields = ['language', 'label']

class OptionSerializer(serializers.ModelSerializer):
    translations = OptionLocalSerializer(source='optionlocal_set', many=True, read_only=True)

    class Meta:
        model = Option
        fields = ['label', 'language', 'group', 'language', 'translations']

class StepLocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepLocal
        fields = ['language', 'label']


class StepSerializer(serializers.ModelSerializer):
    translations = StepLocalSerializer(source='steplocal_set', many=True, read_only=True)
    options = OptionSerializer(source='option_set', many=True, read_only=True)
    wizard = serializers.CharField(source='wizard.code', read_only=True)
    step = serializers.CharField(source='step_number', read_only=True)

    class Meta:
        model = Step
        fields = ['wizard', 'step', 'label', 'language', 'filter_name', 'translations', 'options']

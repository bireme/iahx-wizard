from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from main.serializers import WizardSerializer, StepSerializer, OptionSerializer

from main.models import Wizard, Step, Option


class WizardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows retrieve wizards information.
    """
    queryset = Wizard.objects.all()
    serializer_class = WizardSerializer
    http_method_names = ['get']


class StepViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows retrieve step information.
    """
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    http_method_names = ['get']


    def get_queryset(self):
        queryset = Step.objects.all()
        wizard = self.request.query_params.get('wizard', None)
        step = self.request.query_params.get('step', None)

        if wizard is not None:
            queryset = queryset.filter(wizard__code=wizard)

        if step is not None:
            queryset = queryset.filter(step_number=step)

        return queryset


class OptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows retrieve option information.
    """
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Option.objects.all()
        step = self.request.query_params.get('step', None)
        group = self.request.query_params.get('group', None)

        if step is not None:
            queryset = queryset.filter(step=step)

        if group is not None:
            queryset = queryset.filter(group=group)

        return queryset

from typing import OrderedDict, Type, Union

from rest_framework.generics import CreateAPIView
from rest_framework.serializers import Serializer, FileField, BaseSerializer
from django.core.files.uploadedfile import InMemoryUploadedFile


class GenericFileSerializer(Serializer):
    attachment = FileField()


class UploadFileView(CreateAPIView):
    def get_serializer_class(self) -> Type[BaseSerializer]:
        return GenericFileSerializer

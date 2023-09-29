from typing import OrderedDict, Type, Union

from rest_framework.generics import CreateAPIView
from rest_framework.serializers import Serializer, FileField, BaseSerializer
from django.core.files.uploadedfile import InMemoryUploadedFile


class GenericFileSerializer(Serializer):
    attachment = FileField()


class PhotoSerializer(GenericFileSerializer):
    def create(self, ctx: OrderedDict):
        ...


class UploadFileView(CreateAPIView):
    def get_serializer_class(self) -> Type[BaseSerializer]:
        attachment: Union[InMemoryUploadedFile, None] = self.request.data.get('attachment')
        if not attachment:
            return Serializer

        match attachment.content_type.split('/')[0]:
            case 'image':
                return PhotoSerializer
            case _:
                return GenericFileSerializer

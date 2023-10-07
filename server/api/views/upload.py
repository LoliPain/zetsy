from typing import OrderedDict, Type, Any

from rest_framework.generics import GenericAPIView
from rest_framework.serializers import ModelSerializer, BaseSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

from server.models.stored_file import FileModel


class GenericFileSerializer(ModelSerializer):
    class Meta:
        model = FileModel
        fields = ("attachment",)


class PhotoSerializer(GenericFileSerializer):
    def create(self, ctx: OrderedDict):
        return FileModel(**ctx)


class UploadFileView(GenericAPIView):
    parser_classes = (MultiPartParser,)

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        if not self.request.FILES.get('attachment'):
            return Response('No file provided')
        # TODO: Use serializer
        return Response()

    def get_serializer_class(self) -> Type[BaseSerializer]:
        _attachment = self.request.FILES.get('attachment')
        match _attachment.content_type.split('/')[0]:
            case 'image':
                return PhotoSerializer
            case _:
                return GenericFileSerializer

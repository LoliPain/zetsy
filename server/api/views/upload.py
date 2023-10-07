from typing import OrderedDict, Type, Any

from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
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

    def create(self, ctx: OrderedDict):
        return FileModel(**ctx)


class PhotoSerializer(GenericFileSerializer):
    def create(self, ctx: OrderedDict):
        return FileModel(**ctx)


class UploadFileView(GenericAPIView):
    parser_classes = (MultiPartParser,)

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def get_serializer_class(self) -> Type[BaseSerializer]:
        _attachment = self.request.FILES.get('attachment')
        match _attachment.content_type.split('/')[0] if _attachment else None:
            case 'image':
                return PhotoSerializer
            case _:
                return GenericFileSerializer

from typing import OrderedDict, Type, Any

from rest_framework.generics import CreateAPIView
from rest_framework.serializers import Serializer, FileField, BaseSerializer
from rest_framework.request import Request
from rest_framework.response import Response


class GenericFileSerializer(Serializer):
    attachment = FileField()


class PhotoSerializer(GenericFileSerializer):
    def create(self, ctx: OrderedDict):
        ...


class UploadFileView(CreateAPIView):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.attachment = None

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        self.attachment = self.request.data.get('attachment')
        if self.attachment:
            return Response('n')
        return super().post(request, *args, **kwargs)

    def get_serializer_class(self) -> Type[BaseSerializer]:
        match self.attachment.content_type.split('/')[0]:
            case 'image':
                return PhotoSerializer
            case _:
                return GenericFileSerializer

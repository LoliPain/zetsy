from typing import OrderedDict, Type, Any

from rest_framework.generics import CreateAPIView
from rest_framework.serializers import Serializer, FileField, BaseSerializer
from rest_framework.request import Request
from rest_framework.response import Response


class GenericFileSerializer(Serializer):
    attachment = FileField()


class PhotoSerializer(GenericFileSerializer):
    class ExampleModel:
        class File:
            def __init__(self, url):
                self.url = url

        def __init__(self, **kwargs):
            self.attachment = self.File(kwargs.get('_name'))

    def create(self, ctx: OrderedDict):
        return self.ExampleModel(**ctx['attachment'].__dict__)


class UploadFileView(CreateAPIView):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.attachment = None

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        self.attachment = self.request.data.get('attachment')
        if not self.attachment:
            return Response('No file provided')
        return super().post(request, *args, **kwargs)

    def get_serializer_class(self) -> Type[BaseSerializer]:
        if not self.attachment:
            return Serializer
        match self.attachment.content_type.split('/')[0]:
            case 'image':
                return PhotoSerializer
            case _:
                return GenericFileSerializer

from typing import Any

from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.generics import GenericAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

from server.models.stored_file import FileModel


class GenericFileSerializer(ModelSerializer):
    class Meta:
        model = FileModel
        fields = ("attachment",)


class UploadFileView(GenericAPIView):
    parser_classes = (MultiPartParser,)
    serializer_class = GenericFileSerializer

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

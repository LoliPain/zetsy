from django.db.models import Model, CharField, ForeignKey, CASCADE
from .uploader import UploadedByModel


class FileModel(Model):
    filename = CharField(max_length=8)
    uploader = ForeignKey(UploadedByModel, on_delete=CASCADE)

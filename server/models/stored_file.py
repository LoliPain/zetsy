from django.db.models import Model, FileField, CharField, ForeignKey, CASCADE
from .uploader import UploadedByModel


class FileModel(Model):
    attachment = FileField()
    uploader = ForeignKey(UploadedByModel, on_delete=CASCADE)

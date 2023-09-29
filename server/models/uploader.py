from django.db.models import Model, CharField, BooleanField


class UploaderModel(Model):
    uploader_token = CharField(max_length=64)
    is_valid = BooleanField()


class UploadedByModel(UploaderModel):
    uploader_ip = CharField(max_length=64)

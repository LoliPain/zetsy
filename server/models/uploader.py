from django.db.models import Model, CharField, BooleanField


class UploaderModel(Model):
    uploader_token = CharField()
    is_valid = BooleanField()


class UploadedByModel(UploaderModel):
    uploader_ip = CharField()

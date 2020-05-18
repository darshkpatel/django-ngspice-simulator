from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import uuid


class Task(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_time = models.DateTimeField(auto_now=True, db_index=True)
    task_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)


class spiceFile(models.Model):
    file_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(
        storage=FileSystemStorage(location=settings.MEDIA_ROOT))
    upload_date = models.DateTimeField(auto_now=True, db_index=True)
    # owner = models.ForeignKey('auth.User', related_name='uploaded_files')
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='files_set')

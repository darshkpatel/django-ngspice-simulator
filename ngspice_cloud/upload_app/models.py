from django.db import models
import uuid
# Create your models here.


class Task(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_time = models.DateTimeField(auto_now=True, db_index=True)
    task_id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)


class spiceFile(models.Model):
    file_id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    file = models.FileField()
    upload_date = models.DateTimeField(auto_now=True, db_index=True)
    # owner = models.ForeignKey('auth.User', related_name='uploaded_files')
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='files_set')

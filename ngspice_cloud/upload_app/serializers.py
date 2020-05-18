from rest_framework import serializers
from .models import spiceFile, Task


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = spiceFile
        fields = ('file', 'upload_date', 'file_id', 'task')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    files_set = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('task_id', 'task_time', 'files_set')

    def create(self, validated_data):
        files_data = self.context.get('view').request.FILES.getlist("file")
        print('reached here', self.context.get('view').request.FILES)
        task = Task.objects.create()
        print('task: ', task)
        for file_data in files_data:
            spiceFile.objects.create(task=task, file=file_data)
            print('Created Object for:', file_data.name)
        return task

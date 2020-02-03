import os
from rest_framework import serializers
from .models import spiceFile, Task


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = spiceFile
        fields = ('file', 'upload_date',)



class TaskSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    files_set = FileSerializer( many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'task_time','files_set',)

    def create(self, validated_data):
        files_data = self.context.get('view').request.FILES.getlist("file")
        print('reached here', self.context.get('view').request.FILES)
        task = Task.objects.create()
        print('task: ', task)
        for file_data in files_data:
            spiceFile.objects.create(task=task, file=file_data)
            print('Created Object for:', file_data.name)
        return task




# class FileSerializer ( serializers.Serializer ) :
#     image = serializers.ListField(
#                        child=serializers.FileField( max_length=100000,
#                                          allow_empty_file=False,
#                                          use_url=False )
#                                 )
#     def create(self, validated_data):
#         task = Task.objects.create(user_id=1)
#         files=validated_data.pop('file')
#         for file in files:
#             photo=Photo.objects.create(file=file,task=task,**validated_data)
#         return task

# class SingleFileSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = spiceFile
#         read_only_fields = ('name','version','owner','upload_date', 'size')
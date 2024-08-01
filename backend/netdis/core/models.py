from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from netdis import settings
import os

# Create your models here.
class UploadedFile(models.Model):
    file = models.FileField(upload_to="uploads/", max_length=300)
    hash = models.CharField(max_length=256)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.name))
        self.file = 'PROCESSED'
        self.save()
    
class Project(models.Model):
    file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    
class Function(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    addr = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    cfg = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Block(models.Model):
    function = models.ForeignKey(Function, on_delete=models.CASCADE)
    src = models.ManyToManyField('self', related_name="src_blocks", symmetrical=False, blank=True)
    dst = models.ManyToManyField('self', related_name="dst_blocks", symmetrical=False, blank=True)
    addr = models.CharField(max_length=64)
    

class Disasm(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE)   
    addr = models.CharField(max_length=64) 
    op = models.CharField(max_length=64)
    data = models.CharField(max_length=64)
    
class Task(models.Model):
    #file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=64, default="default")
    #project = models.ForeignKey(Project, default=None, null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=16)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    result = GenericForeignKey('content_type', 'object_id')
    
class FileUploadResult(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
class CFGAnalysisResult(models.Model):
    json_result = models.JSONField()
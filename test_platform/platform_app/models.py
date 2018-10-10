from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField("名称",max_length=100, blank=False,default="")
    description = models.TextField("描述",default="")
    status = models.BooleanField("状态", default=True)
    # modification_time = models.DateTimeField("时间")
    creationtime = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.name

class Module(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=100, blank=False, null=False)
    description = models.TextField("描述",default="")
    creationtime = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.name
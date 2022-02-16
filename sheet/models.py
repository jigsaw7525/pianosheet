from django.db import models
from user.models import Profile
from django.db.models.deletion import CASCADE, SET_NULL
# Create your models here.


class Type(models.Model):

    name = models.CharField(max_length=50, unique=True, null=False)
    createdon = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.id}-{self.name}-{self.createdon}"


class Tonality(models.Model):

    name = models.CharField(max_length=50, unique=True, null=False)
    createdon = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.id}-{self.name}-{self.createdon}"


class Style(models.Model):

    name = models.CharField(max_length=50, unique=True, null=False)
    createdon = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.id}-{self.name}-{self.createdon}"


class Sheet(models.Model):

    owner = models.ForeignKey(Profile, on_delete=CASCADE)
    # 標題
    title = models.CharField(max_length=200)
    # 譜檔
    pinture = models.FileField(upload_to='file')
    # 類型
    type = models.ForeignKey(Type, null=True, on_delete=SET_NULL)
    # 作曲家
    composer = models.CharField(null=True, blank=True, max_length=150)
    # 風格
    style = models.ManyToManyField(Style)
    # 調性
    tonality = models.ForeignKey(Tonality, null=True, on_delete=SET_NULL)
    # 說明
    introduction = models.TextField(null=True, blank=True)
    # 建立日期
    createdon = models.DateTimeField(auto_now_add=True)
    # 檢視次數
    view = models.IntegerField(default=0)

    class Meta:

        ordering = ['-createdon']

    def __str__(self):
        return self.title

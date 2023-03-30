from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Posts(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    slug=models.CharField(max_length=20)
    sug=models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    sno=models.AutoField(primary_key=True)
    comments=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Posts, on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comments+" "+"by"+" "+self.user.username
    


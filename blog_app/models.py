from django.contrib.auth.models import update_last_login
from django.db import models
from accounts.models import User

# Create your models here.

class Blogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    Blog_Title = models.CharField(max_length=120)
    Blog_Description = models.CharField(max_length=120)
    blog_image = models.ImageField(upload_to='blog_image')
    blog_content = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Blog_Title

    

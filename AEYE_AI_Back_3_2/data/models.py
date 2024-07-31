from django.db import models

# Create your models here.

class Request_Image_Model(models.Model):
    # 저장 경로: MEDIA_ROOT/uploaded_images/xxx.png
    image = models.ImageField(blank=True, upload_to='uploaded_images')


class Initiate_AI_Model(models.Model):
    name = models.CharField(max_length= 10)

    
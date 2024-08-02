from django.db import models

# Create your models here.

class Request_Image_Model(models.Model):
    # 저장 경로: MEDIA_ROOT/uploaded_images/xxx.png
    image = models.ImageField(blank=True, upload_to='uploaded_images')

# get JSON File
class Initiate_AI_Model(models.Model):
    name = models.CharField(max_length= 100)
    
    def __str__(self) :
        return self.name
    
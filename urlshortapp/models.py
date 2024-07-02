from django.db import models

# Create your models here.

class BaseModel(models.Model):
    STATUS_CHOICES = (
        ("Active", 'active'),
        ("In-Active", 'inactive'),
        )
    
    id           = models.AutoField(primary_key=True,db_index=True)                                               
    status       = models.CharField(choices=STATUS_CHOICES,default="Active",max_length=100)
    created_at   = models.DateTimeField(auto_now_add=True)                                                        
    updated_at   = models.DateTimeField(auto_now=True)                                                            


class URLModel(BaseModel):

    original_url = models.CharField(max_length=2000,verbose_name= 'small url')
    redirect_url = models.CharField(max_length=5000,verbose_name= 'long url')
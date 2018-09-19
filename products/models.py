from django.db import models
import os
import random
from django.db.models.signals import pre_save
from products.utils import unique_slug_generator
# Create your models here.
def upload_image_path(instance,filename):
    x=random.randint(1,100)
    ext=get_file_ext(filename)[-1]
    finalname= f'{x}{ext}'
    return f"products/{instance.title}/{finalname}"

def get_file_ext(filename):
    base=os.path.basename(filename)
    name,ext=os.path.splitext(base)
    return name,ext

class ProductManager(models.Manager):
    def get_by_id(self,id):
        qs=self.get_queryset().filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None

class Product(models.Model):
    title  =models.CharField(max_length=120)
    slug   =models.SlugField(unique=True ,blank=True)
    desc   =models.TextField()
    price  =models.DecimalField(decimal_places=2,max_digits=20)
    image  =models.ImageField(upload_to=upload_image_path ,null=True,blank=True) 

    objects=ProductManager()
    def __str__(self):
        return self.title
    #objects = models.Manager()
def pre_save_recevier(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(pre_save_recevier,sender=Product)
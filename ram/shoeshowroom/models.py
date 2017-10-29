from django.db import models
from django.utils import timezone
import PIL
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.
# python manage.py makemigrations blog
# python manage.py migrate blog
class product(models.Model):
	myid=models.AutoField(primary_key=True)

	CHOICES0 = (
        ('shoe_boot', 'shoe_boot'),
        ('shoe_oxford', 'shoe_oxford'),
        ('shoe_loafer', 'shoe_loafer'),
        ('shoe_sneaker', 'shoe_sneaker'),
        ('shoe_sport', 'shoe_sport'),
        ('slipper_beach', 'slipper_beach'),
        ('slipper_glider', 'slipper_glider'),
        ('slipper_printed', 'slipper_printed'),
        ('sandal_mules', 'sandal_mules'),
        ('sandal_glider', 'sandal_glider'),
        ('sandal_opentoe', 'sandal_opentoe'),
        ('sock_winter', 'sock_winter'),
        ('sock_sport', 'sock_sport'),

    )
	floater=models.CharField(max_length=200, choices=CHOICES0)


	company=models.CharField(max_length=200)
	modelname=models.CharField(max_length=200)

	price=models.PositiveIntegerField(null=True)

	img1=models.ImageField(upload_to='media/',blank=True, null=True, editable=True)
	img2=models.ImageField(upload_to='media/',blank=True, null=True, editable=True)
	img3=models.ImageField(upload_to='media/',blank=True, null=True, editable=True)
	image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
	image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")


	CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('K', 'Kids'),
    )
	category=models.CharField(max_length=1, choices=CHOICES)


	CHOICES2 = (
        (1, 'Available'),
        (0, 'Unavailable'),
    )
	size6=models.PositiveIntegerField(default=0,choices=CHOICES2)
	size7=models.PositiveIntegerField(default=0,choices=CHOICES2)
	size8=models.PositiveIntegerField(default=0,choices=CHOICES2)
	size9=models.PositiveIntegerField(default=0,choices=CHOICES2)
	size10=models.PositiveIntegerField(default=0,choices=CHOICES2)

	CHOICES3 = (
		('Zero', 'Zero'),
        ('Ankel', 'Ankel'),
        ('Calf', 'Calf'),
        ('Knee', 'Knee'),
        ('Thigh', 'Thigh'),
    )
	neck_height=models.CharField(max_length=200, choices=CHOICES3, default='Ankel')

	outer_material=models.CharField(max_length=200,null=True)
	occasion=models.CharField(max_length=200,null=True)
	weight=models.CharField(max_length=200,null=True)
	pack_of=models.PositiveIntegerField(default=1)

	def __unicode__(self):
		return "{0}".format(self.img1)

	def save(self):
		if not self.img1:
			return

		super(product, self).save()
		img1 = Image.open(self.img1)
		img2 = Image.open(self.img2)
		img3 = Image.open(self.img3)
		(width, height) = img1.size
		size = ( 150, 150)
		img1 = img1.resize(size, Image.ANTIALIAS)
		img2 = img2.resize(size, Image.ANTIALIAS)
		img3 = img3.resize(size, Image.ANTIALIAS)
		img1.save(self.img1.path)
		img2.save(self.img2.path)
		img3.save(self.img3.path)



class relation(models.Model):
	relid=models.AutoField(primary_key=True)
	userid=models.CharField(max_length=200)
	size=models.PositiveIntegerField(null=True)
	quantity=models.PositiveIntegerField()
	productid=models.PositiveIntegerField()

class querysub(models.Model):
	queryid=models.AutoField(primary_key=True)
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	query=models.CharField(max_length=1000)
	answer=models.CharField(max_length=1000,null=True)




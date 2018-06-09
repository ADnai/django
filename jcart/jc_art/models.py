#coding=utf-8

from django.db import models
from tinymce.models import HTMLField

class CourseTrain(models.Model):
   

	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		


class CreativeConsulting(object):
    cctitle    = models.CharField(max_length = 200)
    ccpic     = models.ImageField(upload_to = 'fs_pic')	
    
    cccontent = HTMLField()
    ccdate    = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.gtitle.encode('utf-8')
		


class SelectionOfWorks(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg


class ForeignSchools(object):
	fsname = models.CharField(max_length = 200)
    fspic = models.ImageField(upload_to = 'fs_pic')	
    fsjianjie = models.CharField(max_length =200)
    fscontent = HTMLField()
    def __str__(self):
        return self.fsname.encode('utf-8')


class StudentsStudyingAbroad(object):
	
		
# Create your models here.

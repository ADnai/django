from django.db import models


class BookInfo(models.Model):
    btitle = models.CharField(max_length =20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(null =False)
    isDelete = models.BooleanField(default =False)

    class Meta:
        db_table = 'bookinfo'

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book =models.ForeignKey(BookInfo)

# Create your models here.

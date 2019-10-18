from django.db import models

# Create your models here.
class AxfWheel(models.Model):
    img = models.CharField(max_length=256)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_wheel'


class AxfNav(models.Model):
    img = models.CharField(max_length=256)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_nav'


class AxfMustBuy(models.Model):
    img = models.CharField(max_length=256)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_mustbuy'


class AxfMainshow(models.Model):
    img = models.CharField(max_length=256)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()
    categoryid = models.IntegerField()
    brandname = models.CharField(max_length=32)

    img1 = models.CharField(max_length=256)
    childcid1 = models.IntegerField()
    productid1 = models.IntegerField()
    longname1 = models.CharField(max_length=32)
    price1 = models.CharField(max_length=32)
    marketprice1 = models.CharField(max_length=32)

    img2 = models.CharField(max_length=256)
    childcid2 = models.IntegerField()
    productid2 = models.IntegerField()
    longname2 = models.CharField(max_length=32)
    price2 = models.CharField(max_length=32)
    marketprice2 = models.CharField(max_length=32)

    img3 = models.CharField(max_length=256)
    childcid3 = models.IntegerField()
    productid3 = models.IntegerField()
    longname3 = models.CharField(max_length=32)
    price3 = models.CharField(max_length=32)
    marketprice3 = models.CharField(max_length=32)

    class Meta:
        db_table = 'axf_mainshow'
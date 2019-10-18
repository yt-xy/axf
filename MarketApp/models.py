from django.db import models

# Create your models here.
class AxfFoodType(models.Model):
    typeid = models.CharField(max_length=16)
    typename = models.CharField(max_length=32)
    childtypenames = models.CharField(max_length=128)
    typesort = models.CharField(max_length=16)

    class Meta:
        db_table = 'axf_foodtype'

# id, productid, productimg,                   productname, productlongname,   isxf, pmdesc, specifics, price, marketprice, categoryid, childcid, childcidname, dealerid, storenums, productnum)
# 1,  11951,     '/media/images/goods016.jpg', '',          '乐吧薯片鲜虾味50.0g', 0,     0,      '50g',     2,       2.5,        103541,   103543,    '膨化食品',    4858,     200,         4);
class AxfGoods(models.Model):
    productid = models.CharField(max_length=16)
    productimg = models.CharField(max_length=64)
    productname = models.CharField(max_length=128)
    productlongname = models.CharField(max_length=32)

    isxf = models.CharField(max_length=16)
    pmdesc = models.CharField(max_length=16)
    specifics = models.CharField(max_length=16)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.CharField(max_length=16)

    childcid = models.CharField(max_length=16)
    childcidname = models.CharField(max_length=32)
    dealerid = models.CharField(max_length=16)
    storenums = models.CharField(max_length=16)
    productnum = models.CharField(max_length=16)

    class Meta:
        db_table = 'axf_goods'

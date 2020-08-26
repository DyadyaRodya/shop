from django.db import models

#models for detail view
class SubsectionDetail(models.Model):
        Subid = models.IntegerField(primary_key=True)
        Sid = models.IntegerField()
        Subname = models.CharField(max_length=100)
        Sname = models.CharField(max_length=100)

class CategoryDetail(models.Model):
        Cid = models.IntegerField(primary_key=True)
        Subid = models.IntegerField()
        Sid = models.IntegerField()
        Cname = models.CharField(max_length=100)
        Subname = models.CharField(max_length=100)
        Sname = models.CharField(max_length=100)

class ProductDetail(models.Model):
        Pid = models.IntegerField(primary_key=True)
        Cid = models.IntegerField()
        Subid = models.IntegerField()
        Sid = models.IntegerField()
        Pname = models.CharField(max_length=100)
        description = models.TextField()
        price = models.DecimalField(max_digits=11, decimal_places=2)
        amount = models.IntegerField(default=0)
        Cname = models.CharField(max_length=100)
        Subname = models.CharField(max_length=100)
        Sname = models.CharField(max_length=100)

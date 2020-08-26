from django.db import models

class Section(models.Model):
        Sid = models.IntegerField(primary_key=True)
        Sname = models.CharField(max_length=100)

class Subsection(models.Model):
        Subid = models.IntegerField(primary_key=True)
        Subname = models.CharField(max_length=100)
        insection = models.ForeignKey(Section, on_delete=models.PROTECT)

class Category(models.Model):
        Cid = models.IntegerField(primary_key=True)
        Cname = models.CharField(max_length=100)
        insubsection = models.ForeignKey(Subsection, on_delete=models.PROTECT)

class Product(models.Model):
        Pid = models.IntegerField(primary_key=True)
        Pname = models.CharField(max_length=100)
        description = models.TextField()
        price = models.DecimalField(max_digits=11, decimal_places=2)
        amount = models.IntegerField(default=0)
        incategory = models.ForeignKey(Category, on_delete=models.PROTECT)

        class Meta:
                constraints = [
                        models.CheckConstraint(
                                check=models.Q(price__gte=0),
                                name="A valid price is non-negative",
                        )
                ]

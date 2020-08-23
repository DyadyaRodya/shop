from django.db import models

class Section(models.Model):
        name = models.CharField(max_length=100)

class Subsection(models.Model):
        name = models.CharField(max_length=100)
        section = models.ForeignKey(Section, on_delete=models.PROTECT)

class Category(models.Model):
        name = models.CharField(max_length=100)
        subsection = models.ForeignKey(Subsection, on_delete=models.PROTECT)

class Product(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()
        price = models.DecimalField(max_digits=11, decimal_places=2)
        amount = models.IntegerField(default=0)
        category = models.ForeignKey(Category, on_delete=models.PROTECT)

        class Meta:
                constraints = [
                        models.CheckConstraint(
                                check=models.Q(price__gte=0),
                                name="A valid price is non-negative",
                        )
                ]

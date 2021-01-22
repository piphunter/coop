from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=30)
    shares = models.IntegerField(default=1)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Payment(models.Model):
    CATEGORY = (
        ('Cash', 'Cash'),
        ('Previous', 'Previous'),
        ('Misc', 'Misc'),
    )
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    mode = models.CharField(max_length=10, choices=CATEGORY)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.mode

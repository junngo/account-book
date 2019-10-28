from django.db import models
from django.conf import settings

# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "{user}-{name}".format(user=self.user, name=self.name)


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    tr_date = models.DateTimeField('tr date published ')
    tr_amount = models.DecimalField(max_digits=8, decimal_places=2)
    memo = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return "{account}-{amount}".format(account=self.account, amount=self.tr_amount)

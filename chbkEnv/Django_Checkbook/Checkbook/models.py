from django.db import models


class Account(models.Model):
    first_name = models.CharField(max_length=50, blank=True, default="")
    last_name = models.CharField(max_length=50, blank=True, default= "")
    initial_deposits = models.DecimalField(default=0.00, max_digits=100000000, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.first_name + " " + self.last_name


trans_type = {

    ('Withdrawal', 'Withdrawal'), ('Deposit', 'Deposit')

}


class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=20, choices=trans_type)
    amount = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    description = models.CharField(max_length=150, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    Transactions = models.Manager()


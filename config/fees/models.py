from django.db import models

class StudentFee(models.Model):
    student_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    payment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.student_name
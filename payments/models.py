from django.db import models
from buildings.models import TimeStampedModel, Building, Penality
from houses.models import House, Resident

def bill_upload_path(instance, filename):
    building_name = instance.house.building.name
    return f'building/{building_name}/payments/bills/{filename}'

class Event(TimeStampedModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='events')
    creator = models.ForeignKey(Resident, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    commences = models.DateTimeField()
    penality = models.ForeignKey(Penality, on_delete=models.CASCADE, null=True, blank=True)
    attachment = models.FileField(upload_to=f'building/{building.name}/events/attachments/')

class BuildingExpense(TimeStampedModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2,  max_digits=10)
    description = models.TextField()

class Payment(TimeStampedModel):

    class PaymentTypes(models.TextChoices):
        Power = 'Power', 'POWER'
        Water = 'Water', 'WATER'
        Other = 'Other', 'OTHER'

    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='payments')
    collector = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='payments_to_collect')
    type = models.CharField(max_length=50, choices=PaymentTypes.choices, default=PaymentTypes.Other)
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=5 if type=='Water' else 525)
    isRecurring = models.BooleanField(default=False)
    recurrence_period = models.IntegerField(null=True, blank=True)
    penality = models.ForeignKey(Penality, on_delete=models.CASCADE, null=True, blank=True)
    attachment = models.FileField(upload_to=f'building/{building.name}/payments/attachments/', null=True, blank=True)

class HousePayment(TimeStampedModel):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="house_payments")
    paid_by = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name="completed_payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bill = models.FileField(upload_to=bill_upload_path, null=True, blank=True)
    verified = models.BooleanField(default=False)
    
    @property
    def total_paid(self):
        return HousePayment.objects.filter(
            house=self.house, 
            payment=self.payment
            ).aggregate(total=models.Sum('amount'))['total'] or 0

    @property
    def payment_progress(self):
        if self.payment.amount == 0:
            return 100
        return (self.total_paid / self.payment.amount) * 100

    def __str__(self):
        return f"Payment for {self.house} on {self.payment.deadline}: {'Paid' if self.payment_progress == 100 else 'Not Paid'}"
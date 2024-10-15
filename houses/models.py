from django.db import models
from accounts.models import UserAccount
from buildings.models import Building, Payment, Penality, TimeStampedModel

class House(TimeStampedModel):

    class StatusChoices(models.TextChoices):
        Unoccupied  = "Unoccupied", "UNOCCUPIED"
        Owner_Resided = "Owner Resided", "OWNER RESIDED"
        Rented = "Rented", "RENTED"
        For_Sale = "For Sale", "FOR SALE"
        For_Rent = "For Rent", "FOR RENT"

    owner = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="my_houses")
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="houses")
    description = models.TextField()
    floor = models.IntegerField()
    floorCode = models.CharField(max_length=10)
    bedrooms = models.IntegerField()
    squareMeter = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(choices=StatusChoices, default=StatusChoices.Unoccupied, max_length=50)

    class Meta:
        unique_together = ("building", "floor", "floorCode")
    def __str__(self):
        return str(self.floor)+self.floorCode
    
class HouseAttachment(TimeStampedModel):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house_attachments')
    file = models.FileField(upload_to=f'house/{house}/attachments/')

class HousePicture(TimeStampedModel):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="house_pictures")
    picture = models.ImageField(upload_to=f'house/{house}/pictures/')

class Resident(TimeStampedModel):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="residents")
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="residences")
    isHead = models.BooleanField(default=False)
    isOwner = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)

    class Meta:
        unique_together = ('house', 'user')
    def __str__(self):
        return str(self.user.phone)
    
class HousePenality(TimeStampedModel):
    penality = models.ForeignKey(Penality, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="penalities")
    is_paid = models.BooleanField(default=False)

class HousePayment(TimeStampedModel):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="payments")
    paid_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="completed_payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def total_paid(self):
        return self.aggregate(total=models.Sum('amount'))['total'] or 0

    @property
    def payment_progress(self):
        if self.payment.amount == 0:
            return 100
        return (self.total_paid / self.payment.amount) * 100

    def __str__(self):
        return f"Payment for {self.house} on {self.payment.deadline}: {'Paid' if self.payment_progress == 100 else 'Not Paid'}"
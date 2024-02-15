from django.db import models

class PhoneNumber(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

class User(models.Model):
    name = models.CharField(max_length=255)
    aadhar_id = models.IntegerField(unique=True)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class Admin(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

class VehicleType(models.Model):
    vehicle_type = models.CharField(max_length=255)



class GroundType(models.Model):
    ground_type = models.CharField(max_length=255)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)

class Slot(models.Model):
    ground_type = models.ForeignKey(GroundType, on_delete=models.CASCADE)
    slot_number = models.IntegerField()

class Ground(models.Model):
    ground_type = models.ForeignKey(GroundType, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    timeslot = models.TimeField

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ground = models.ForeignKey(Ground, on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length=20)
    no_of_adults = models.IntegerField()
    no_of_children = models.IntegerField()
    no_of_foreigners = models.IntegerField()
    no_of_stillcamera = models.IntegerField()
    no_of_videocamera = models.IntegerField()


class PeopleType(models.Model):
    people_type = models.CharField(max_length=255)
   

class AmountPeople(models.Model):
    people = models.ForeignKey(PeopleType, on_delete=models.CASCADE)
    
    amount = models.IntegerField()


class AdditionalCharge(models.Model):
    additional_charge = models.CharField(max_length=100)
    

class AdditionalChargeAmount(models.Model):

    additional_charge = models.ForeignKey(AdditionalCharge, on_delete=models.CASCADE)
    amount = models.IntegerField()
        
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE) 
    payment_datetime = models.DateTimeField(auto_now_add=True)
    total_amount = models.IntegerField()
    
class Refund(models.Model):
    request_date = models.DateField(auto_now_add=True)
    refund_date = models.DateTimeField(auto_now_add=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE) 
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE) 
    account_holder_name = models.CharField(blank=False, max_length=100) 
    account_no = models.IntegerField()
    ifsc_code = models.CharField(blank=False, max_length=100)

class Reschedule(models.Model):
    reschedule_date = models.DateField()
    reschedule_time = models.TimeField()
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
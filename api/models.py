from django.db import models, transaction
from model_utils import Choices


class Qualification(models.Model):
    STATUS_CHOICES = Choices(
        ('NW', 'New'),
        ('1', 'identification'),
        ('2', 'regulations'),
        ('CF', 'conformation'),
        ('DE', 'denial'),

    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES,
                              default=STATUS_CHOICES.NW)
    rule_one = models.BooleanField(default=False)
    rule_two = models.BooleanField(default=False)
    rule_three = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)


class Passport(models.Model):
    image_photo = models.ImageField(upload_to='passports/')
    image_registration = models.ImageField(upload_to='passports/')
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    serial_number = models.IntegerField()
    birth_date = models.DateField()
    place_of_birth = models.TextField()
    issue_date = models.DateField()
    department_code = models.IntegerField()
    issued_by = models.TextField()
    registration_adress = models.TextField(max_length=300)
    qualification = models.OneToOneField(Qualification,
                                         on_delete=models.CASCADE,
                                         related_name='passport')

    @transaction.atomic
    def save(self, *args, **kwargs):
        super(Passport, self).save(*args, **kwargs)
        qualification = Qualification.objects.get(id=self.qualification.id)
        qualification.status = '1'
        qualification.save()

    def __str__(self):
        return str(self.serial_number)


class Document(models.Model):
    title = models.TextField(max_length=100)
    image = models.ImageField(upload_to='documents/')
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE,
                                      related_name='document')

    def __str__(self):
        return self.title

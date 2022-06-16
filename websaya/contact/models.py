from django.db import models

# Create your models here.
class Kontak(models.Model):
    nama_lengkap = models.CharField(max_length=70)
    tanggal_lahir = models.DateField()
    GENDER = [
        ('p', 'Pria'),
        ('w', 'Wanita'),
    ]
    jenis_kelamin = models.CharField(choices=GENDER, max_length=50)
    alamat = models.TextField()
    agree = models.BooleanField()
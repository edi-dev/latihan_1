from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=25)
    slug_cat = models.SlugField(max_length=100, blank=True, unique=True)

    class Meta:
        ordering = ['-category']

    def save(self):
        self.slug_cat = slugify(self.category)
        super(Category, self).save()
    
    def __str__(self):
        return '{}'.format(self.category)

class Artikel(models.Model):
    from django.contrib.auth.models import User
    post_cat = models.ForeignKey(Category, to_field='slug_cat', on_delete=models.CASCADE)
    judul = models.CharField(max_length=75, unique=True)
    summary = models.TextField()
    body = models.TextField()
    date_create = models.DateField(auto_now_add=True)
    date_edit = models.DateField(auto_now=True)
    penulis = models.ForeignKey(User, to_field='username', null=True, blank=True, on_delete=models.CASCADE, related_name='author')
    publish = models.BooleanField(default=False)
    gambar = models.ImageField(upload_to='%Y/%m/%d', blank=True, null=True)
    slug = models.SlugField(max_length=175, unique=True, blank=True)

    class Meta:
        ordering = ['-date_create']
        permissions = {
            ('terbitkan', 'Terbikan Artikel')
        }
    
    def save(self):
        from django.utils import timezone
        self.slug = slugify(self.judul)
        super(Artikel, self).save()
    
    def __str__(self):
        return '{} | {} / {}'.format(self.id, self.judul, self.publish)
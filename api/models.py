from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Sorov(models.Model):
    fish = models.CharField(max_length=500)
    idpassport = models.CharField(max_length=500)
    Yashashmanzili = models.CharField(max_length=500)
    mfynomi = models.CharField(max_length=500)
    kochanomi = models.CharField(max_length=500)
    telefonraqami = models.CharField(max_length=500)
    rasmvavidio = models.FileField()
    matn = models.TextField()

    def __str__(self) -> str:
        return self.fish
    
    def get_absolute_url(self):
        return reverse('rahmat')
    
class Hokimiyat(models.Model):
    murajat = models.ForeignKey(Sorov,on_delete=models.CASCADE)
    orinbosar = models.CharField(max_length=500)
    tashkilot = models.CharField(max_length=500,default='none',blank=True)
    muddat = models.IntegerField(default=timezone.now()+timezone.timedelta(days=1))
    bajarildi = models.BooleanField(default=False)
    muddat_holati = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.orinbosar
        
    
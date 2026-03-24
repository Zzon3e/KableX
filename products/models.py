from django.db import models

# Tabell for medlemmer
class Medlem(models.Model):
    navn = models.CharField(max_length=100)
    epost = models.EmailField(unique=True)
    telefon = models.CharField(max_length=20)
    medlemsdato = models.DateField(auto_now_add=True)
    aktiv = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['navn']
    
    def __str__(self):
        return self.navn


# Tabell for aktiviteter
class Aktivitet(models.Model):
    navn = models.CharField(max_length=200)
    beskrivelse = models.TextField()
    dato = models.DateField()
    sted = models.CharField(max_length=200)
    opprettet = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-dato']
    
    def __str__(self):
        return self.navn


# Tabell for påmeldinger (kobler medlem og aktivitet)
class Pamelding(models.Model):
    medlem = models.ForeignKey(Medlem, on_delete=models.CASCADE)
    aktivitet = models.ForeignKey(Aktivitet, on_delete=models.CASCADE)
    dato_pameldt = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ('medlem', 'aktivitet')
    
    def __str__(self):
        return f"{self.medlem.navn} → {self.aktivitet.navn}"


# Tabell for betalinger
class Betaling(models.Model):
    STATUS_CHOICES = [
        ('betalt', 'Betalt'),
        ('ikke_betalt', 'Ikke betalt'),
    ]
    
    medlem = models.ForeignKey(Medlem, on_delete=models.CASCADE)
    belop = models.DecimalField(max_digits=8, decimal_places=2)
    betalingsdato = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ikke_betalt')
    
    class Meta:
        ordering = ['-betalingsdato']
    
    def __str__(self):
        return f"{self.medlem.navn} - {self.belop} kr"

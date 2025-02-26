from django.contrib.auth.models import AbstractUser
from django.db import models


class Pref(models.Model):
    # can be used to extend the fixtures for the Pref model
    class PrefChoices(models.TextChoices):
        HOKKAIDO = "Hokkaido", "Hokkaido"
        AOMORI = "Aomori", "Aomori"
        IWATE = "Iwate", "Iwate"
        MIYAGI = "Miyagi", "Miyagi"
        YAMAGATA = "Yamagata", "Yamagata"
        IBARAKI = "Ibaraki", "Ibaraki"
        TOCHIGI = "Tochigi", "Tochigi"
        GUNMA = "Gunma", "Gunma"
        SAITAMA = "Saitama", "Saitama"
        CHIBA = "Chiba", "Chiba"
        TOKYO = "Tokyo", "Tokyo"
        KANAGAWA = "Kanagawa", "Kanagawa"
        NIIGATA = "Niigata", "Niigata"
        NARA = "Nara", "Nara"
        OSAKA = "Osaka", "Osaka"
        KYOTO = "Kyoto", "Kyoto"
        HIROSHIMA = "Hiroshima", "Hiroshima"
        EHIME = "Ehime", "Ehime"
        KOBE = "Kobe", "Kobe"

    name = models.CharField(choices=PrefChoices.choices, max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name"], name="unique_pref_name")
        ]


class CustomUser(AbstractUser):
    tel = models.CharField(max_length=20, null=True, blank=True)
    pref = models.ForeignKey(
        Pref, db_column="pref_id", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.username

    # DB Constraint to ensure the email is unique
    class Meta:
        constraints = [models.UniqueConstraint(fields=["email"], name="unique_email")]

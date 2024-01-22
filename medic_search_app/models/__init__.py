from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

ROLE_CHOICES = (
    (1, 'Administrador'),
    (2, 'Médico'),
    (3, 'Paciente'),
)

from .Profile import Profile
from medic_search_app.models import *

class Speciality(models.Model):
    name = models.CharField(null=False, max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
from django.contrib.auth.models import User
from django.db import models
from encrypted_model_fields.fields import EncryptedTextField

class Passwords(models.Model):
    class Meta:
        verbose_name = "Saved Password"

    name = models.CharField(max_length=300)
    url = models.URLField(max_length=5000)
    password = EncryptedTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    shared_with = models.ManyToManyField(User, related_name='Passwords', blank=True)
    def __str__(self):
        return f"Name: {self.name}, Url: {str(self.url)[:20]}, Created at: {self.created_at}, Updated at: {self.updated_at}"
    
class Environment(models.Model):
    class Meta:
        verbose_name = "Saved Environment"

    name = models.CharField(max_length=300)
    url = models.URLField(max_length=5000)
    environment = EncryptedTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    shared_with = models.ManyToManyField(User, related_name='Environment', blank=True)
    def __str__(self):
        return f"Name: {self.name}, Url: {str(self.url)[:20]}, Created at: {self.created_at}, Updated at: {self.updated_at}"
    
    
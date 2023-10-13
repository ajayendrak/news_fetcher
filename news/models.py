from django.db import models
from user.models import User

class UserKeywords(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	keyword = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.user.firstname}---{self.id}'







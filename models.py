import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
	def _str_(self):
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'


	def was_published_recently(self):
		return self.pub_date>=timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
	question=models.ForeignKey(Question, on_delete=models.CASCADE)  #a relationship is defined, 
																	#using ForeignKey. That tells Django
																	#each Choice is related to a single Question. 
																	#Django supports all the common database relationships: 
																	#many-to-one, many-to-many, and one-to-one.
	def _str_(self):
		return self.choice_text
	choice_text=models.CharField(max_length=200)#max_length is a necessary argument for this Field class
	votes=models.IntegerField(default=0)#default value of vote=0

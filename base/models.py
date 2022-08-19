from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Room(models.Model):
	host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	participants = models.ManyToManyField(User, related_name='participants', blank=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

# Поле name имеет параметры макс. 200 символов
# Поле description имеет параметры != 0, т.е. ВАЖНО заполнить это поле;
# blank=True сохраняет форму в БД
# $$$$$$$

# Различия между auto_now и auto_now_add заключается, в том что
# первый изменяется постоянно с изменением данных(типо обновляется),
# а второй он сохраняет дату создания самого объекта

	class Meta:
		ordering = ['-updated', '-created']

	def __str__(self):
		return self.name



class Message(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	# Если удалиться основная моделька, т.е. статья то все объекты,
	# также удаляться (on_delete=models.SET_NULL)
	body = models.TextField()
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-updated', '-created']

	
	def __str__(self):
		return self.body[0:50]


# OneToMany - отношение одного объекта ко многим
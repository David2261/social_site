from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Topic
from .forms import RoomForm


# rooms = [
# 	{'id':1, 'name': 'First Step!'},
# 	{'id':2, 'name': 'Second Step!'},
# 	{'id':3, 'name': 'Third Step!'},
# ]

def loginPage(request):
	page = 'login'
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		username = request.POST.get('username').lower()
		password = request.POST.get('password')

		try:
			user = User.objects.get(username=username)
		except:
			messages.error(request, 'User does not exist')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Username or Password does not exist')

	context={'page':page}
	return render(request, 'base/login_register.html', context)


def logoutUser(request):
	logout(request)
	return redirect('home')


def registerPage(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.username = user.username.lower()
			user.save()
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'An error occured during registration')
	return render(request, 'base/login_register.html', {'form':form})


def home(request):
	q = request.GET.get('q') if request.GET.get('q') != None else ''

	rooms = Room.objects.filter(
		Q(topic__name__icontains=q) |
		Q(name__icontains=q) |
		Q(description__icontains=q)
		)
	# В функции filter(моделька__по параметру__icontains) - позволяет искать объекты,
	# даже если их писать не до конца.
	# Либо по топику, либо по имени объекта.

	topics = Topic.objects.all()
	room_count = rooms.count()

	context = {'rooms': rooms, 'topics':topics, 'room_count':room_count}
	return render(request, 'base/home.html', context)


def room(request, pk):
	room = Room.objects.get(id=pk)
	context = {'room': room}
	return render(request, 'base/room.html', context)


@login_required(login_url='login')
def createRoom(request):
	form = RoomForm()
	if request.method == 'POST':
		form = RoomForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'form':form}
	return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def updateRoom(request, pk):
	room = Room.objects.get(id=pk)
	form = RoomForm(instance=room)

	if request.user != room.host:
		return HttpResponse('Your are not allowed here!!!')

	if request.method == 'POST':
		form = RoomForm(request.POST, instance=room)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'form':form}
	return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def deleteRoom(request, pk):
	room = Room.objects.get(id=pk)

	if request.user != room.host:
		return HttpResponse('Your are not allowed here!!!')

	if request.method == 'POST':
		room.delete()
		return redirect('home')
	return render(request, 'base/delete.html', {'obj':room})
# Переменная = Название_Модельки.Атрибут_объект.метод({
# all - все
# get - брать объекты по id
# filter - выдает объект если они соответствует параметрам
# exclude -	выдает объекты если они не соответствует параметрам
# annotate - указанные с помощью аргументов ключевого слова,
# будут использовать ключевое слово в качестве псевдонима аннотации
# alias - сохраняет выражение для последующего повторного использования с другими QuerySet методами
# ~~~~
# order_by - По умолчанию результаты, возвращаемые a QuerySet, упорядочиваются по порядку кортежа,
# заданному orderingпараметром модели Meta. Вы можете переопределить это по отдельности QuerySet,
# используя order_byметод. Результат выше будет упорядочен по pub_dateубыванию,
# а затем по headlineвозрастанию. Отрицательный знак перед "-pub_date"указывает нисходящую заказ.
# Подразумевается возрастающий порядок. Для случайного заказа используйте "?"
# Чтобы упорядочить по полю в другой модели, используйте тот же синтаксис,
# что и при запросе по отношениям модели. То есть имя поля,
# за которым следует двойное подчеркивание ( __), за которым следует имя поля в новой модели и т.д.
# Для любого количества моделей, к которым вы хотите присоединиться.
# ~~~~
# reverse - Используйте этот reverse()метод, чтобы изменить порядок,
# в котором возвращаются элементы набора запросов.
# Повторный вызов reverse()восстанавливает порядок в нормальном направлении.
# Чтобы получить «последние» пять элементов в наборе запросов, вы можете сделать это:
# my_queryset.reverse()[:5]
# ~~~~
# distinct - Возвращает новый, QuerySetкоторый используется в своем SQL-запросе.
# Это исключает повторяющиеся строки из результатов запроса.SELECT DISTINCT
# ~~~
# values - Возвращает, QuerySetкоторый возвращает словари, а не экземпляры модели,
# при использовании в качестве итерации.
# Каждый из этих словарей представляет объект с ключами, соответствующими именам атрибутов объектов модели.
# This list contains a Blog object.
# Blog.objects.filter(name__startswith='Beatles')
# <QuerySet [<Blog: Beatles Blog>]>
# This list contains a dictionary.
# Blog.objects.filter(name__startswith='Beatles').values()
# <QuerySet [{'id': 1, 'name': 'Beatles Blog', 'tagline': 'All the latest Beatles news.'}]>
# ~~~
# })
from django.urls import path
from . import views

urlpatterns = [
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
	path('register/', views.registerPage, name="register"),

	path('', views.home, name="home"),
	path('room/<str:pk>/', views.room, name="room"),
	path('profile/<str:pk>/', views.userProfile, name="user-profile"),

	path('create-room/', views.createRoom, name="create-room"),
	path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
	path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
	path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

	path('update-user/', views.updateUser, name="update-user"),

	path('topics/', views.topicsPage, name="topics"),
	path('activity/', views.activityPage, name="activity"),
]

# str - соответствует любой непустой строке, за исключением разделителя пути, '/'. Это значение по умолчанию, если преобразователь не включен в выражение.
# int - соответствует нулю или любому положительному целому числу. Возвращает int.
# slug - соответствует любой строке заголовка, состоящей из букв или цифр ASCII, а также символов дефиса и подчеркивания. Например, build-your-1st-django-site.
# uuid - соответствует форматированному UUID. Чтобы предотвратить сопоставление нескольких URL-адресов с одной и той же страницей, необходимо использовать дефисы, а буквы должны быть строчными. Например, 075194d3-6885-417e-a8a8-6c931e272f00. Возвращает экземпляр UUID.
# path - соответствует любой непустой строке, включая разделитель пути, '/'. Это позволяет вам сопоставлять полный путь URL, а не сегмент пути URL, как в случае с str.
from django.urls import path

from .views import name, cricketer, color
app_name = 'new'
urlpatterns = [
	path('name/', name, name='name'),
	path('cricketer/', cricketer, name='cricketer'),
	path('color/', color, name='color'),
]

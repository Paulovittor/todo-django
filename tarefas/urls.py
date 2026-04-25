from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tarefas, name='listar_tarefas'),
    path('nova/', views.nova_tarefa, name='nova_tarefa'),
    path('editar/<int:tarefa_id>/', views.editar_tarefa, name='editar_tarefa'),
    path('deletar/<int:tarefa_id>/', views.deletar_tarefa, name='deletar_tarefa'),
]

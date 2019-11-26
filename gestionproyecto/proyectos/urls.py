from django.urls import path
from .views import (ProyectoList, CrearProyectoView,
                    ProyectoDetalle, ProyectoUpdate,
                    ProyectoDelete, FaseProyectoAdd,
                    FaseProyectoDetail, FaseProyectoUpdate,
                    FaseProyectoDelete)
app_name = 'proyecto'
urlpatterns = [
    path('', ProyectoList.as_view(), name='proyecto_list'),
    path('add-proyecto', CrearProyectoView.as_view(), name='add_proyecto'),
    path('proyecto/<int:pk>/', ProyectoDetalle.as_view(), name='detail_proyecto'),
    path('proyecto/edit/<int:pk>/', ProyectoUpdate.as_view(), name='edit_proyecto'),
    path('proyecto/delete/<int:pk>/', ProyectoDelete.as_view(), name='delete_proyecto'),
    path('fase-proyecto/add', FaseProyectoAdd.as_view(), name='add_fase'),
    path('fase-proyecto/<int:pk>/', FaseProyectoDetail.as_view(), name='detail_fase'),
    path('fase-proyecto/edit/<int:pk>/', FaseProyectoUpdate.as_view(), name='update_fase'),
    path('fase-proyecto/delete/<int:pk>/', FaseProyectoDelete.as_view(), name='delete_fase')

]

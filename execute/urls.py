from django.urls import path
from execute.controller.controller import ExecuteIde

urlpatterns = [
    path('executeidecode/', ExecuteIde.as_view())
]
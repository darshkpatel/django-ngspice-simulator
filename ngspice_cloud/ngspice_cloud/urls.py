from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from upload_app import views as upload_views
from simulator_app import views as simulator_views
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="nsgpice-simulator API",
        default_version='v1',
        description="Web Based ngSpice Simulator",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'uploads', upload_views.UploadViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Simulation API & Upload URLs
    path('api/task/<uuid:task_id>',
         simulator_views.TaskResultView.as_view(), name='task_status'),

    path('api/task', simulator_views.ViewTasks.as_view(), name='view_tasks'),

    path('api/task/<uuid:task_id>/start',
         simulator_views.TaskStartView.as_view(), name='task_start'),

    path('api/celery/<uuid:task_id>',
         simulator_views.CeleryResultView.as_view(), name='celery_status'),

    path('api/', include(router.urls)),

    # Docs URLs
    url(r'^api/docs(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(
            cache_timeout=0), name='schema-json'),

    url(r'^api/docs/$',
        schema_view.with_ui('swagger',
                            cache_timeout=0), name='schema-swagger-ui'),

]

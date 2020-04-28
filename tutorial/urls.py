from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'blog/', include('blog.urls', namespace='blog')),
    path(r'', TemplateView.as_view(template_name="home.html"),
        name='homepage'),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

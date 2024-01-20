from django.urls import include, path

from api.spectacular.urls import urlpatterns as doc_urls

appname = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.jwt'))
]

urlpatterns += doc_urls

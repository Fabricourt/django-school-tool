from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name="details"),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name="results"),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),
    url(r'^create_course$', views.create_course, name="create_course"),
    url(r'^courses/(?P<course_id>[0-9]+)/edit$', views.edit_course, name="edit_course"),
    url(r'^profile$', views.profile, name="profile")
]

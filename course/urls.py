from django.urls import path
from .views import CoursePageView


urlpatterns = [
    path("course/", CoursePageView.as_view(), name="course"),

]

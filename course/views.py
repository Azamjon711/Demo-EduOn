from django.shortcuts import render
from django.views import View


class CoursePageView(View):
    def get(self, request):
        return render(request, "main/course.html")

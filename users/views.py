from django.shortcuts import render
from django.views import View
from course.models import Course, Speciality


class LandingPageView(View):
    def get(self, request):
        specialities = Speciality.objects.all()
        courses = Course.objects.all()
        context = {
            "specialities": specialities,
            "courses": courses,
        }
        return render(request, "main/index.html")

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Project


# Create your views here.

def all_projects(request):
    projects = Project.objects.all()
    paginator = Paginator(projects, 9)
    page = request.GET.get('page')
    projects = paginator.get_page(page)
    return render(request, "project/allprojects.html", {"projects": projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "project/projectdetail.html", {"project": project})

from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView,
									CreateView, DeleteView, UpdateView)
from . import models

from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
	template_name = "index.html"

class SchoolList(ListView):
	model = models.School

class SchoolDetail(DetailView):

	model = models.School
	template_name = 'basicapp/school_detail.html'
	


class CreateSchool(CreateView):
	model = models.School
	fields = ('name','principal','location')


class UpdateSchool(UpdateView):
	model = models.School
	fields = ('name','principal')



class DeleteSchool(DeleteView):
	model = models.School
	success_url = reverse_lazy('basicapp:list')

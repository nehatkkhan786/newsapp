from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article

# Create your views here.
class ArticleListView(ListView):
	model = Article
	template_name = 'articles/article_list.html'

class ArticleDetailView(DetailView):
	model = Article
	template_name = 'articles/article_detail.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
	model = Article
	template_name = 'articles/article_create.html'
	fields = ('title', 'body',)
	login_url = 'login'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)



class ArticleEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Article
	fields = ('title', 'body',)
	template_name = 'articles/article_edit.html'
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
	model = Article
	template_name = 'articles/article_delete.html'
	success_url = reverse_lazy('article_list')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user






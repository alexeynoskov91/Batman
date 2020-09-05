from django.shortcuts import render
#from django.http import HttpResponse
from .models import Articles
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ArticleForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages

# def homepage(request):
    # return render (request, 'homepage/batman.html')
    
class Home(ListView):
    model = Articles
    template_name = 'index.html'
    context_object_name = 'list_articles'
    
class ArticlesDetailView(DetailView):
    model = Articles
    template_name = 'article_detail.html'
    context_object_name = 'get_article'

class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False
    def form_valid(self,form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)
    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


class ArticleCreateView(CustomSuccessMessageMixin, CreateView):
    model = Articles
    template_name = 'edit_page.html'
    form_class = ArticleForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись создана'
    def get_context_data(self,**kwargs):
        kwargs['list_articles'] = Articles.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)
        

class ArticleUpdateView(CustomSuccessMessageMixin, UpdateView):
    model = Articles
    template_name = 'edit_page.html'
    form_class = ArticleForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись успешно обновлена'
    def get_context_data(self,**kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = 'edit_page.html'
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись удалена'
    def post(self,request,*args,**kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)    
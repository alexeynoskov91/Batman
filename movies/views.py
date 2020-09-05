from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie
from .forms import ReviewForm

class MoviesView(ListView):
    """Список фильмов"""
    # template_name = 'movies.html' это тестил почему рвет templates. Зато выяснил. Из-за неявного задания шаблоны берутся из папки movie. Вьюха по статьям template_name задает явно, поэтому они ищутся сразу в корне templates
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name явно не указал, потому что джанго сам ищет файл "(имя_модели)_list.html" - название по умолчанию

class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = "url"
    # template_name не указал, потому что джаного сам ищет файл "(имя_модели)_detail.html" - название по умолчанию
    
class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
                
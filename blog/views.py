from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag
from django.db.models import F
# from .forms import PostsForm


# Этот класс предназначен для автоматического отображения постов, хранящихся в базе данных, на главной странице.
class Home(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context


def index(request):
    return render(request, 'blog/index.html')

def get_category(request, slug):
    return render(request, 'blog/category.html', {'slug': slug})

def text(request):
    return render(request, 'blog/Praktikum_2.html', {'title': 'lists'})

def list(request):
    return render(request, 'blog/Praktikum_3.html', {'title': 'lists'})

def web_4(request):
    return render(request, 'blog/Practicum_4.html', {'title': 'lists'})

def web_7(request):
    return render(request, 'blog/Practicum_7.html', {'title': 'lists'})

def web_8(request):
    return render(request, 'blog/Praktikum_8.html')

def web_91(request):
    return render(request, 'blog/Practicum9_1.html')

def web_92(request):
    return render(request, 'blog/Practicum9_2.html')

def web_93(request):
    return render(request, 'blog/Practicum9_3.html')

def web_94(request):
    return render(request, 'blog/Practicum9_4.html')

def blog_category(request, slug):
    return render(request, 'blog/category.html')

def blog_post(request, slug):
    return render(request, 'blog/post.html')


class PostsByCategory(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class PostsByTag(ListView):
    template_name = 'blog/index.html'  # Шаблон, который будет использоваться
    context_object_name = 'posts'  # Имя объекта в контексте шаблона
    paginate_by = 2  # Количество записей на странице
    allow_empty = False  # Если нет записей, вернуть 404

    def get_queryset(self):
        # Фильтрация постов по тегу
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # Передача текущего тега в контекст
        context['title'] = f"Записи с тегом: {Tag.objects.get(slug=self.kwargs['slug']).name}"
        return context


def add_news(request):
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = PostsForm()
    return render(request, 'blog/add_news.html', {'form': form})




from .forms import BasicForm

def signup(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            pass

    else:
        form = BasicForm()
    return render(request, 'signup.html', {'form': form})

# core/views.py
# ...
def crispy_signup(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = BasicForm()
    return render(request, 'crispy_signup.html', {'form': form})

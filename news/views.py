from time import timezone
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import Post


class PostsList(ListView):
    model = Post
    template_name = 'news/posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = timezone.localtime(timezone.now())  # добавим переменную текущей даты time_now
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'



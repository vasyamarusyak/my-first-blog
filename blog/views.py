from django.shortcuts import render
#from django.shortcuts import HttpResponse # імпорт для HttpResponse
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #відфільтровує дані побілкації статтей, де lts - менше або рівне, часовій зоні яка є тепер, а order by - упорядковує за датою публікації.
    return render(request, 'blog/post_list.html', {'posts': posts})
    #return HttpResponse("Hello world!") просто виеде "Hello world"

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'details.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        getDetailInfo = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = getDetailInfo.total_likes() #models.py function
        context['related_posts'] = Post.objects.all()
        context['total_likes'] = total_likes
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

def CategoryView(request, categories):
    category_posts = Post.objects.filter(category=categories.replace('-',' '))
    return render(request, 'categories.html', {'categories': categories.title().replace('-', ' '), 'category_posts': category_posts})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)] ))

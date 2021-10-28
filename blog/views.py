from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy,reverse 
from django.http import HttpResponseRedirect

# Create your views here.
class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	context_object_name = 'posts'
	ordering = ['-post_date']

class PostDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'

	# stuff = Post.objects.get(id = self.kwargs['pk'])
	# total_likes = stuff.total_likes()

	def get_context_data(self, *args, **kwargs):
		context = super(PostDetailView,self).get_context_data(*args, **kwargs)
		stuff =get_object_or_404(Post, id=self.kwargs['pk'])
		tl = stuff.total_likes()
		context['total_likes'] = tl
		return context

class CreatePostView(CreateView):
	model = Post
	template_name = 'new_post.html'
	fields = '__all__'

class PostEditView(UpdateView):
	model = Post
	template_name = 'edit_post.html'
	fields = ['title','body']

class PostDeleteView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')

def LikeView(request, pk):
	post = Post.objects.get(id=pk)
	post.likes.add(request.user)
	return HttpResponseRedirect(reverse('post-detail',args=[pk]))

from django import forms
from .models import Post, Comment

class PostForm(forms.MmodelForm):

	class Meta():
		model = Post
		fields = ('author','title','text')



class CommentForm(forms.MmodelForm):
	class Meta():
		model = Comment
		fields = ('author','text')

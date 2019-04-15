from django.shortcuts import render, get_object_or_404
from .models import Blogpost
from django.utils import timezone
# Create your views here.
def post_list(request):
	blogpost = Blogpost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'dummyapp/post_list.html', {'blogpost':blogpost})

def post_detail(request, pk):
    blogpost = get_object_or_404(Blogpost, pk=pk)
    return render(request, 'dummyapp/post_detail.html', {'blogpost': blogpost})

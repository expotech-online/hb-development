from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Category
from .forms import CommentForm
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib import messages

def archive(request):
    category_id = request.GET.get('category')
    if category_id:
        posts = Post.objects.filter(category_id=category_id)
    else:
        posts = Post.objects.all()
        
    paginator = Paginator(posts, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    return render(request, 'blogs/archives.html', {'page_obj': page_obj, 'categories': categories})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    
    # Fetch related posts based on the same category
    related_posts = Post.objects.filter(category=post.category).exclude(pk=pk)[:5]
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            if request.user.is_authenticated:
                comment.author = request.user
            comment.save()
            
            # Construct the post URL
            post_url = request.build_absolute_uri(reverse('post_detail', args=[post.pk]))
            
            # Construct the delete comment URL
            delete_url = request.build_absolute_uri(reverse('delete_comment', args=[comment.id]))
            
            # Send email notification to admin
            send_mail(
                subject=f'New Comment on Post: {post.title}',
                message=(
                    f'Name: {comment.name}\n'
                    f'Email: {comment.email}\n'
                    f'Comment: {comment.content}\n'
                    f'Post: {post.title}\n'
                    f'Link: {post_url}\n'
                    f'Site: LG Assurance\n\n'
                    f'To delete this comment, click the following link: {delete_url}'
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blogs/singlepost.html', {
        'post': post,
        'comments': comments,
        'form': form,
        'related_posts': related_posts
    })

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id  # Get the post ID before deleting the comment
    comment.delete()
    messages.success(request, 'Comment has been deleted.')
    return redirect('post_detail', pk=post_id)

def search_results(request):
    query = request.GET.get('q')
    results = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
    return render(request, 'pages/search_result.html', {'results': results, 'query': query})



def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category)
    paginator = Paginator(posts, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blogs/category_detail.html', {'category': category, 'page_obj': page_obj})

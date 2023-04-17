from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reviews.models import Review, Comment, Emote
from django.http import JsonResponse
from .forms import ReviewForm, CommentForm

# Create your views here.


def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/index.html', context)


EMOTIONS = [
    {'label': '👍', 'value': 1},
    {'label': '👎', 'value': 2},
    {'label': '😂', 'value': 3},
    {'label': '😡', 'value': 4},
]


def detail(request, pk):
    review = Review.objects.get(pk=pk)

    emotions = []
    for emotion in EMOTIONS:
        label = emotion['label']
        value = emotion['value']
        count = 0
        exist = False
        if request.user.is_authenticated:
            count = Emote.objects.filter(review=review, emotion=value).count()
            exist = Emote.objects.filter(
                review=review, emotion=value, user=request.user).exists()
        emotions.append(
            {
                'label': label,
                'value': value,
                'count': count,
                'exist': exist,
                'is_authenticated': request.user.is_authenticated,
            }
        )

    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        'emotions': emotions,
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'reviews/detail.html', context)


@login_required
def emotes(request, review_pk, emotion):
    review = Review.objects.get(pk=review_pk)
    filter_query = Emote.objects.filter(
        review=review,
        user=request.user,
        emotion=emotion,
    )
    if filter_query.exists():
        filter_query.delete()
    else:
        Emote.objects.create(review=review, user=request.user, emotion=emotion)
    return redirect('reviews:detail', review_pk)


@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            new_images = request.FILES.getlist('new_images')
            if new_images:
                review.image += new_images
            review.user = request.user
            review.save()
            form.save_m2m()
            return redirect('reviews:index')
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'reviews/create.html', context)


@login_required
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('reviews:index')


@login_required
def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user != review.user:
        return redirect('reviews:index')

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            new_images = request.FILES.getlist('new_images')
            if new_images:
                review.image.add(*new_images)
            return redirect('reviews:detail', review.pk)
    else:
        form = ReviewForm(instance=review)

    context = {
        'review': review,
        'form': form,
    }
    return render(request, 'reviews/update.html', context)


@login_required
def comment_create(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('reviews:detail', review.pk)
    context = {
        'review': review,
        'comment_form': comment_form,
    }
    return render(request, 'reviews/detail.html', context)


@login_required
def comment_delete(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('reviews:detail', review_pk)


@login_required
def like_comment(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        if request.user in comment.like_users.all():
            comment.like_users.remove(request.user)
        else:
            comment.like_users.add(request.user)
    return redirect('reviews:detail', pk=review_pk)

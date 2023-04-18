from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reviews.models import Review, Comment, Emote
from django.http import JsonResponse
from .forms import ReviewForm, CommentForm
from django.core.paginator import Paginator


# Create your views here.


def index(request):
    reviews = Review.objects.order_by('-pk')
    """
        [int] page
        현재 주소의 페이지 번호를 할당받는 변수
        주소에 page(키)에 대한 값이 없으면 1 할당
    """
    page = request.GET.get('page', '1')

    """
        [int] per_page
        페이지를 나누는 기준
        e.g. 10 -> 데이터를 10개를 기준으로 나눔.
    """
    per_page = 5

    """
        [Paginator 인스턴스] paginator
        첫 번째 인자 : 페이지네이션을 적용할 데이터(queryset)
        두 번째 인자 : per_page
    """
    paginator = Paginator(reviews, per_page)

    """
        [Page 인스턴스] page_obj
        출력할 데이터 및 페이지네이션을 구현을 위한 데이터가 저장된 변수
        반복문으로 순회하면 페이징 처리가 된 데이터가 요소가 됨.
    """
    page_obj = paginator.get_page(page)

    context = {
        'reviews': page_obj,
    }

    return render(request, 'reviews/index.html', context)


EMOTIONS = [
    {'label': '👎', 'value': 1},
    {'label': '😂', 'value': 2},
    {'label': '😡', 'value': 3},
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
def likes(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user in review.like_users.all():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('reviews:detail', pk=review_pk)


@login_required
def like_comment(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        if request.user in comment.like_users.all():
            comment.like_users.remove(request.user)
        else:
            comment.like_users.add(request.user)
    return redirect('reviews:detail', pk=review_pk)

from beer.models import Brewery, Beer, Review, ReviewComment
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext


def brewery(request, brewery_id):
    b = get_object_or_404(Brewery, pk=brewery_id)
    return render_to_response('beer/brewery.html', {'brewery': b})

def beer(request, beer_id):
    b = get_object_or_404(Beer, pk=beer_id)
    return render_to_response('beer/beer.html', {'beer': b})

def review(request, review_id):
    r = get_object_or_404(Review, pk=review_id)
    comments = ReviewComment.objects.filter(review=r)

    return render_to_response('beer/review.html',
                              {'review': r, 'comments': comments},
                              context_instance=RequestContext(request))

def review_comment(request, review_id):
    r = get_object_or_404(Review, pk=review_id)

    try:
        comment_author = request.POST['author']
        comment_text = request.POST['content']
    except (KeyError, e):
        return render_to_response('beer/review.html',
                                  {'review': r,
                                   'comments': comments,
                                   'error_message': 'Could not save comment'},
                                  context_instance=RequestContext(request))

    else:
        new_comment = ReviewComment()
        new_comment.review = r
        new_comment.author = comment_author
        new_comment.content = comment_text
        new_comment.save()

        return HttpResponseRedirect(reverse('beer.views.review', args=(r.id,)))

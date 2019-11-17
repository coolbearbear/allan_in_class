# tests/blog/views/test_home.py

from model_mommy import mommy
import pytest

from blog.models import Post

# Needed for database
pytestmark = pytest.mark.django_db

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_authors_included_in_context_data(client, django_user_model):
    """
    Checks that a list of unique published authors is included in the context
    and is ordered by first name.
    """
    # Make a published author called Cosmo
    cosmo = mommy.make(
        django_user_model,
        username='ckramer',
        first_name='Cosmo',
        last_name='Kramer',
    )
    mommy.make(
        'blog.Post',
        status=Post.PUBLISHED,
        author=cosmo,
        _quantity=2,
    )
    # make a published author called elaine
    elaine = mommy.make(
        django_user_model,
        username='ebenez',
        first_name='Elaine',
        last_name='Benez',
    )
    mommy.make(
        'blog.Post',
        status=Post.PUBLISHED,
        author=elaine,
    )

    #make an unpublished author
    unpublished_author = mommy.make(
        django_user_model,
        username='gcostanza'
    )
    mommy.make('blog.Post', author=unpublished_author, status=Post.DRAFT)

    # Expect cosmo and elaine to be returned, in this ordered
    expected = [cosmo, elaine]

    # make a request to the home view
    response = client.get('/')

    # the context is available in the test response
    result = response.context.get('authors')

    # cast result (query set) to a list to compare
    assert list(result) == expected

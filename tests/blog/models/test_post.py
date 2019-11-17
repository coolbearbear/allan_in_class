import datetime as dt
from freezegun import freeze_time
from model_mommy import mommy
import pytest

from blog.models import Post

pytestmark = pytest.mark.django_db

def test_published_posts_only_returns_those_with_published_status():
    post = mommy.make('blog.Post', status=Post.PUBLISHED)
    mommy.make('blog.Post', status=Post.DRAFT)
    expected = [post]

    assert list(Post.objects.published()) == expected

def test_draft_post():
    post = mommy.make('blog.Post', status=Post.DRAFT)
    mommy.make('blog.Post', status=Post.PUBLISHED)
    expected = [post]

    assert list(Post.objects.drafts()) == expected

@freeze_time(dt.datetime(2020, 1, 1, 1), tz_offset=0)
def test_published_action():
    post = mommy.make('blog.Post', published=None)
    post.publish()
    assert post.status == Post.PUBLISHED
    assert post.published == dt.datetime(2020, 1, 1, 1, tzinfo=dt.timezone.utc)


def test_get_authors_returns_users_who_have_authored_a_post(django_user_model):
    # create a user
    author = mommy.make(django_user_model)
    # create a post that is authored by the user
    mommy.make('blog.Post', author=author)
    # create another user - but this one won't have any post
    mommy.make(django_user_model)

    assert list(Post.objects.get_authors()) == [author]


def test_get_authors_returns_unique_users(django_user_model):
    # create a user
    author = mommy.make(django_user_model)
    # create multiple posts. the _quantity argument can be used
    # to specify how many objects to create.
    mommy.make('blog.Post', author=author, _quantity=3)

    assert list(Post.objects.get_authors()) == [author]

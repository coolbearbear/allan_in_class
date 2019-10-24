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

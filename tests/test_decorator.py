import pytest as pytest
from django.urls import reverse


@pytest.mark.django_db
@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        username="test",
        password="test",
    )


def test_urlconf_building(client):
    url = reverse("foo:foo")
    assert url == "/foo"
    response = client.get(url)
    assert response.status_code == 200


def test_login_required(client, settings, user):
    url = reverse("login_required")
    assert url == "/login_required"
    response = client.get(url)
    assert response.status_code == 302
    assert response.url == f"{settings.LOGIN_URL}?next=/login_required"

    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


def test_staff_required(client, user):
    url = reverse("staff_required")
    assert url == "/staff_required"
    response = client.get(url)
    assert response.status_code == 403

    user.is_staff = True
    user.save()

    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


def test_permissions_required(client, user):
    from django.contrib.auth.models import Permission

    url = reverse("permissions_required")

    assert url == "/permissions_required"
    response = client.get(url)
    assert response.status_code == 403

    user.user_permissions.add(
        Permission.objects.get(codename="view_user"),
    )
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


def test_urlconf_building_with_url_params(client):
    url = reverse("foo_id", kwargs={"foo_id": 1})
    assert url == "/foo/1/"
    response = client.get(url)
    assert response.status_code == 200


def test_urlconf_building_with_url_params_and_optional_url_params(client):
    url = reverse("bar")
    assert url == "/bar/"
    response = client.get(url)
    assert response.status_code == 200

    url = reverse("bar", kwargs={"bar_id": 1})
    assert url == "/bar/1/"
    response = client.get(url)
    assert response.status_code == 200


def test_include_view_urls_modules(client):
    url = reverse("baz")
    assert url == "/baz/"
    response = client.get(url)
    assert response.status_code == 200


def test_two_views_same_name(client):
    url = reverse("same_name")
    assert url == "/no_arguments/"
    response = client.get(url)
    assert response.status_code == 200

    url = reverse("same_name", kwargs={"foo_id": 1})
    assert url == "/arguments/1/"
    response = client.get(url)
    assert response.status_code == 200


def test_namespaced_decorator(client):
    url = reverse("namespaced:baz")
    assert url == "/namespaced/baz/"
    response = client.get(url)
    assert response.status_code == 200


def test_namespaced_and_prepended_decorator(client):
    url = reverse("namespaced_and_prepended:foo")
    assert url == "/foos/foo/"
    response = client.get(url)
    assert response.status_code == 200

    url = reverse("namespaced_and_prepended:multi")
    assert url == "/foos/list/"
    response = client.get(url)
    assert response.status_code == 200

    url = reverse("namespaced_and_prepended:multi", kwargs={"id": 42})
    assert url == "/foos/detail/42/"
    response = client.get(url)
    assert response.status_code == 200


def test_class_based_view(client):
    url = reverse("class_based_view")
    assert url == "/class_based_view/"
    response = client.get(url)
    assert response.status_code == 200


def test_multiple_decorators(client):
    url = reverse("one_of_many")
    assert url == "/one_of_many/"
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b"multi decorator"

    url = reverse("two_of_many", kwargs={"num": 2})
    assert url == "/two_of_many/2/"
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b"multi decorator 2"

    url = reverse("three_of_many", kwargs={"number": 3})
    assert url == "/three_of_many/3/"
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b"multi decorator 3"


def test_app_config(client):
    url = reverse("app_config_test:testing")
    assert url == "/app-config-test/testing/"
    response = client.get(url)
    assert response.status_code == 200

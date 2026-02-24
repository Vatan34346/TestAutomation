import pytest
from api.auth_api import AuthAPI, Response


@pytest.mark.parametrize(
    "username,password,expected_status,expect_tokens",
    #  потом все 500 надо заменить на 400+ соответсвующие  коды ошибко
    [
        ("archangel", "Mike2025!", 200, True),
        ("archangel", "wrongpass", 500, False),
        ("unknown_user", "whatever", 500, False),
        ("", "", 500, False),
        ("' OR '1'='1", "pass", 500, False),
    ]
)
def test_login_variants(api_client, username: str, password: str, expected_status: int, expect_tokens: bool) -> None:
    auth: AuthAPI = AuthAPI(api_client)
    response: Response = auth.login(username, password)
    assert response.status_code == expected_status

    cookies: list[str] = response.headers.get_list("set-cookie")
    access_token: str | None = None
    refresh_token: str | None = None

    for cookie in cookies:
        if cookie.startswith("token="):
            access_token = cookie.split(";", 1)[0].split("=", 1)[1]
        elif cookie.startswith("refresh_token="):
            refresh_token = cookie.split(";", 1)[0].split("=", 1)[1]

    if expect_tokens:
        assert access_token is not None
        assert refresh_token is not None
    else:
        assert access_token is None
        assert refresh_token is None


def test_refresh_token(authentication_client) -> None:
    """ Положительный тест для токенов"""
    auth: AuthAPI = AuthAPI(authentication_client)
    old_access: str | None = authentication_client.client.cookies.get("token")
    assert old_access is not None

    response: Response = auth.refresh()
    assert response.status_code == 200

    new_access: str | None = authentication_client.client.cookies.get("token")
    assert new_access is not None


@pytest.mark.parametrize(
    "initial_cookies,expected_status",
    # потом надо заменить все тесты на необходимые тут неправильно
    [
        ({}, 403),
        ({"refresh_token": "invalidtoken"}, 500),
    ]
)
def test_refresh_failures(authentication_client, initial_cookies: dict, expected_status: int):
    """Негативные  тест для токенов"""
    authentication_client.client.cookies.clear()
    for key, value in initial_cookies.items():
        authentication_client.client.cookies.set(key, value)

    auth: AuthAPI = AuthAPI(authentication_client)
    response: Response = auth.refresh()
    assert response.status_code == expected_status

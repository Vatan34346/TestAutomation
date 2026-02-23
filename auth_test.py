from api.auth_api import AuthAPI, Response


def test_login_success(api_client):
    auth = AuthAPI(api_client)
    response: Response = auth.login("archangel", "Mike2025!")

    assert response.status_code == 200
    body: list[str] = response.headers.get_list("set-cookie")

    access_token = None
    refresh_token = None

    for cookie in body:
        if cookie.startswith("token="):
            access_token = cookie.split(";", 1)[0].split("=", 1)[1]
        elif cookie.startswith("refresh_token="):
            refresh_token = cookie.split(";", 1)[0].split("=", 1)[1]

    assert access_token is not None
    assert refresh_token is not None


def test_refresh_token(authentication_client):
    auth = AuthAPI(authentication_client)
    old_access = authentication_client.client.cookies.get("token")
    assert old_access is not None

    response: Response = auth.refresh()
    assert response.status_code == 200

    new_access = authentication_client.client.cookies.get("token")
    assert new_access is not None

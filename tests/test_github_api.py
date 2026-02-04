import requests


def test_get_my_user_info(base_url, github_headers):
    response = requests.get(f"{base_url}/user", headers=github_headers) 

    assert response.status_code == 200
    data = response.json()
    assert "login" in data

    print(f"\nConectado como: {data['login']}")


def test_list_repositories(base_url, github_headers):
    response = requests.get(f"{base_url}/user/repos", headers=github_headers)

    assert response.status_code == 200

    assert isinstance(response.json(), list)


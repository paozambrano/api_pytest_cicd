import requests
import time

def test_get_my_user_info(base_url, github_headers):
    response = requests.get(f"{base_url}/user", headers=github_headers) 

    assert response.status_code == 200
    data = response.json()
    assert "login" in data

    print(f"\nConectado como: {data['login']}")


def test_list_repositories(base_url, github_headers):

    time.sleep(5)
    response = requests.get(f"{base_url}/user/repos", headers=github_headers)

    if response.status_code == 429:
        print(f"\nLímite alcanzado. Reintenta en: {response.headers.get('Retry-After')} segundos")

    assert response.status_code == 200

    assert isinstance(response.json(), list)


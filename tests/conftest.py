import pytest
import os
from dotenv import load_dotenv

load_dotenv()
@pytest.fixture
def github_headers():
    token = os.getenv("GITHUB_TOKEN")
    return{
        "Authorization": f"Bearer{token}",
        "Accept": "application/vnd.github+json"
    }

@pytest.fixture
def base_url():
    return "https://api.github.com"
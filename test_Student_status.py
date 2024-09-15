import pytest
import json
import html
from Student_status import app

@pytest.fixture
def client():
    return app.test_client()


def test_root(client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_submit(client):
    response = client.post('/submit', data={
        'science': '60',
        'maths': '70',
        'c': '80',
        'datascience': '90'
    })
    assert response.status_code == 302
    assert response.location == '/success/75'
import pytest
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['status'] == 'healthy'
    assert 'container' in data
    assert 'project' in data

# def test_secret_success(monkeypatch, client):
#     # Mock boto3.resource().Table().get_item()
#     class MockTable:
#         def get_item(self, Key):
#             return {'Item': {'secret_code': 'supersecret'}}
#     class MockDynamoDB:
#         def Table(self, name):
#             return MockTable()

#     def mock_boto3_resource(*args, **kwargs):
#         return MockDynamoDB()

#     monkeypatch.setattr('app.main.boto3.resource', mock_boto3_resource)

#     rv = client.get('/secret')
#     assert rv.status_code == 200
#     data = rv.get_json()
#     assert data['secret_code'] == 'supersecret'
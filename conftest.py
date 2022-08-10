import pytest
from server.app_server import server

@pytest.fixture
def app():
    app = server.app
    return app
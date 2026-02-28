import copy
import pytest
from fastapi.testclient import TestClient
import src.app as app_module

@pytest.fixture
def client():
    """Provide a TestClient for the FastAPI app."""
    return TestClient(app_module.app)

@pytest.fixture(autouse=True)
def reset_activities():
    """Snapshot activities, yield to test, then restore to keep tests isolated."""
    original = copy.deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(original)
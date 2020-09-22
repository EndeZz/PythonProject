import pytest
from people.Human import Human


@pytest.fixture
def human():
    return Human()
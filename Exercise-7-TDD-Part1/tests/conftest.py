import pytest

from models.company import Company

@pytest.fixture
def company():
  return Company("W's SA")
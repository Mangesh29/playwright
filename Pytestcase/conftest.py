import pytest

@pytest.fixture(scope ="session") # scope can be function, class , module , session
def preSetupWork():
    print(" I setup browser insatnace")
#fixture
import pytest 

@pytest.fixture(scope ="module") # scope can be function, class , module , session
def preWork():
    print(" I setup browser insatnace")




def test_initialCheck(preWork):
    print("This is frist test case")


def test_SecondCheck(preSetupWork):
    print("This is second test case")  
    
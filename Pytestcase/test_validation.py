#fixture
import pytest 

@pytest.fixture(scope ="module") # scope can be function, class , module , session
def preWork():
    print(" I setup browser insatnace") # pre condition code
    return "Fail" # post condition code


@pytest.fixture(scope ="function") # scope can be function, class , module , session
def secondWork():
    print(" I setup secondwork insatnace") # pre condition code
    yield  
    print("tear down validation")

@pytest.mark.smoke
def test_initialCheck(preWork, secondWork):
    print("This is frist test case")
    assert preWork =="Fail"


@pytest.mark.skip #skipping test case
def test_SecondCheck(preSetupWork, secondWork):
    print("This is second test case")  
 
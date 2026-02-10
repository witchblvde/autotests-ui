import pytest

@pytest.mark.smoke
def test_some_case():
    ...


@pytest.mark.regression
def test_regression_case():
    ...


@pytest.mark.smoke
class TestSuite:
    @pytest.mark.some
    def test_case_1(self):
        ...

    def test_case_2(self):
        ...


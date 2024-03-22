import sys, pytest

def test_basic_maths():
    assert 1 > 0

@pytest.mark.xfail(reason="This test is meant to fail")
def test_wrong_maths():
    assert 1 < 0

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0
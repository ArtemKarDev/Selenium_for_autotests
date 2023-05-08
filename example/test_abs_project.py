import pytest
# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
# def test_abs2():
#     assert abs(-42) == -42,  "Should be absolute value of a number"
#
# if __name__ == "__main__":
#     test_abs_project.main()

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
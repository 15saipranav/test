def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_diff():
    assert 3-1 == 2, "should be 2"


if __name__ == "__main__":
    test_sum()
    test_diff()
    print("Everything passed")

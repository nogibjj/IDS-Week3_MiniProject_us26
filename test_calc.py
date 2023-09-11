from calc import mul , sub , add

def test_mul():
    assert mul(1, 2) == 2
def test_sub():
    assert sub(1, 2) == -1
def test_add():
    assert add(1,2) == 3

test_mul()
test_sub()
test_add()

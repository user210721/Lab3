import price_info

print("test lab3")

def test_total_cost_shopping():
    result = []
    result = price_info.total_cost_shopping()

    assert (result == 46.75)

def test_cost_of_fruit():
    result = []
    result = price_info.cost_of_fruits('watermelon', 1)

    assert (result == 6.50)

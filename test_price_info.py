import price_info

print("Test_Lab3_price_info")


def test_total_cost_shopping():

    result = price_info.total_cost_shopping()

    assert (result == 46.75)


def test_cost_of_fruit():

    result = price_info.cost_of_fruits('watermelon', 100)

    assert (result == 650)
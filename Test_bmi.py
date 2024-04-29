import Lab2.bmi as bmi

print("Test_Lab2_BMI")
    

def test_bmi_normal_weight():
    
    result = bmi.calculate_bmi(1.70, 70) 

    assert (result == 0) 


def test_bmi_over_weight():
   
    result = bmi.calculate_bmi(1.60, 103)

    assert (result == 1)


def test_bmi_under_weight():
    
    result = bmi.calculate_bmi(1.65, 45)

    assert (result == -1)

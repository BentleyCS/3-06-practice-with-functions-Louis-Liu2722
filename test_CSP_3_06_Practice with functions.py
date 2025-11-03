import CSP_3_06_Practice_with_functions as HW


def test_multiply_differences():
    assert HW.multiplyDifferences(5, 2, 4, 1)==60
    assert HW.multiplyDifferences(15, 2, 4, 1) ==30030
    assert HW.multiplyDifferences(6, 3, 4, 5) ==36


def test_semi_perimeter():
    assert HW.semiPerimeter(2,4,1)==3.5
    assert HW.semiPerimeter(3,4,5)==6
    assert HW.semiPerimeter(9,4,4)==8.5


def test_herons():
    assert HW.herons(3,4,5)==6
    assert HW.herons(6,4,5)==9.921567416492215
    assert HW.herons(5,5,5)==10.825317547305483


def test_denominator():
    assert HW.denominator(5)==10
    assert HW.denominator(15)==30
    assert HW.denominator(-15)==-30


def test_plus_minus():
    assert HW.plusMinus(4,5)==(1,-9) or HW.plusMinus(4,5)==(-9,1)
    assert HW.plusMinus(6,12)==(6,-18) or HW.plusMinus(6,12)==(-18,6)


def test_main_calc():
    assert HW.mainCalc(-1,-6,8)==68
    assert HW.mainCalc(3,5,-7)==109
    assert HW.mainCalc(1,5,6)==1


def test_quadratic():
    assert HW.quadratic(-1, -6, 8) == (1.1231056256176606, -7.123105625617661) or HW.quadratic(-1, -6, 8) == (-7.123105625617661, 1.1231056256176606)
    assert HW.quadratic(3, 5, -7) == (-2.5733844181517584, 0.9067177514850918) or HW.quadratic(3, 5, -7) == (0.9067177514850918,-2.5733844181517584)
    assert HW.quadratic(1, 5, 6) == (-3,-2) or HW.quadratic(1, 5, 6) == (-2,-3)

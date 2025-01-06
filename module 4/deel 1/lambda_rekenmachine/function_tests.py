from functions import *
from test_lib import *

getal_1 = 3
getal_2 = 3

expected = addition(getal_1,getal_2)
result_lambdafunction1 = addition(getal_1,getal_2)
test('Test som functie', expected, result_lambdafunction1)

expected = subtraction(getal_1,getal_2)
result_lambdafunction2 = subtraction(getal_1,getal_2)
test('Test som functie', expected, result_lambdafunction2)

expected = multiplication(getal_1,getal_2)
result_lambdafunction3 = multiplication(getal_1,getal_2)
test('Test som functie', expected, result_lambdafunction3)

expected = division(getal_1,getal_2)
result_lambdafunction4 = division(getal_1,getal_2)
test('Test som functie', expected, result_lambdafunction4)

report()
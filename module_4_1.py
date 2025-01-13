from fake_math import divide as fake_divide
from true_math import divide as true_divide
result_1 = fake_divide(10, 5)
result_2 = fake_divide(10, 0)
result_3 = true_divide(20, 1)
result_4 = true_divide(20, 0)
print(result_1)
print(result_2)
print(result_3)
print(result_4)
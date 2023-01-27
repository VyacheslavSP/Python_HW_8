import Calculations
import Valid_strring
string = input("Введите выражение   ")

val_string = Valid_strring.valid_string(string)

print(Calculations.Calc(val_string))

#!/usr/bin/python3 

a = 10
b = 5

if __name__ == "__main__":
    import calculator_1

    add_result = calculator_1.add(a, b)
    sub_result = calculator_1.sub(a, b)
    mul_result = calculator_1.mul(a, b)
    div_result = calculator_1.div(a, b)

    print(f"{a} + {b} = {add_result}")
    print(f"{a} - {b} = {sub_result}")
    print(f"{a} * {b} = {mul_result}")
    print(f"{a} / {b} = {div_result}")

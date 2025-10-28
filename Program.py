def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль!"
    return a / b
    
def pow(a, b):
    return a**b


def main():
    print("=== Консольний калькулятор ===")
    print("Доступні операції: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("Введіть перше число:    "))
            op = input("Введіть операцію (+, -, *, /, ^ або 'q' для виходу): ").strip()
            
            if op.lower() == 'q':
                print("Вихід із програми. Бувай!")
                break
            
            num2 = float(input("Введіть друге число: "))
            
            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            elif op=='^':
                result = pow(num1, num2)
            else:
                print("Невідома операція! Спробуйте ще раз.")
                continue
            
            print(f"Результат: {result}\n")
        
        except ValueError:
            print("Помилка вводу! Введіть число.\n")

if __name__ == "__main__":
    main()

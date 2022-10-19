
def addition(a,b):
    return (a+b)


def subtraction(a,b):
    return (a-b)


def multiplication(a,b):
    return (a*b)


def division(a,b):
    if b != 0:
        return (a/b)
    else:
        print("ПОМИЛКА!!! На нуль ділити не можна!")


def exponentiation(a,b):
    return (a**b)


def reduction_to_the_square_root(a,b):
    return ((a)**0.5,(b)**0.5)


def reduction_to_the_cube_root(a,b):
    return ((a)**(1/3),(b)**(1/3))


a=()
b=()
while a != 111 and b!=222:
    a,b=map(int,input("Введіть значення змінних а і b через пробіл,"
                      " (для виходу введіть значення а 111, значення b 222): ").split())
    print("Додавання результат:", addition(a,b))
    print("Віднімання результат:", subtraction(a,b))
    print("Множення результат:", multiplication(a,b))
    print("Ділення результат:", division(a,b))
    print("Зведення в ступінь результат:", exponentiation(a,b))
    print("Корінь квадратний результат:", reduction_to_the_square_root(a,b))
    print("Корінь кубічний результат:", reduction_to_the_cube_root(a,b))

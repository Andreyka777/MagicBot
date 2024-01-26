def decorator(topping):
    def papper(basic_pizza):
        print(basic_pizza(), "Посыпанная перцем")
    def jalapeno(basic_pizza):
        print(basic_pizza(), "С добавлением халапеньо")
    def bbq(basic_pizza):
        print(basic_pizza(), "С соусом барбекю")
    if topping==1:
        return papper
    if topping==2:
        return jalapeno
    if topping==3:
        return bbq

@decorator(1)

def pepperoni():
    return "Тонкое тесто, смазанное томатным соусом, посыпано сыром с добавением колбасы и орегано."
import turtle

def pythagoras_tree(t, order, size, angle=45):
    """
    Рекурсивна функція для малювання дерева Піфагора
    
    Аргументи:
    t - turtle об'єкт
    order - рівень рекурсії 
    size - довжина стовбура
    angle - кут розгалуження 
    """
    if order == 0:
        # Базовий випадок рекурсії - малюємо листок
        t.forward(size)
        t.backward(size)
        return
    
    # Малюємо стовбур
    t.forward(size)
    
    # Зберігаємо позицію та кут для правої гілки
    pos = t.position()
    heading = t.heading()
    
    # Малюємо праву гілку
    t.left(angle)
    pythagoras_tree(t, order - 1, size * 0.8, angle)
    
    # Повертаємось до збереженої позиції
    t.setposition(pos)
    t.setheading(heading)
    
    # Малюємо ліву гілку
    t.right(angle)
    pythagoras_tree(t, order - 1, size * 0.8, angle)
    
    # Повертаємось до початку стовбура
    t.setposition(pos)
    t.setheading(heading)
    
    # Повертаємось до початкової точки
    t.backward(size)

def draw_pythagoras_tree(order, size=100, angle=45):
    """
    Функція для налаштування та запуску малювання дерева Піфагора
    
    Аргументи:
    order - рівень рекурсії (глибина дерева)
    size - довжина початкового стовбура
    angle - кут розгалуження
    """
    window = turtle.Screen()
    window.bgcolor("white")
    window.title(f"Дерево Піфагора (рівень {order})")
    
    t = turtle.Turtle()
    t.speed(0)  # Найшвидша швидкість
    t.left(90)  # Повертаємо turtle вертикально вгору
    t.penup()
    t.goto(0, -200)  # Починаємо знизу екрану
    t.pendown()
    t.pensize(2)
    t.color("red") 
    
    
    pythagoras_tree(t, order, size, angle)
    
    # Ховаємо turtle після малювання
    t.hideturtle()
    
    window.mainloop()

# Функція для запиту рівня рекурсії у користувача
def get_user_input():
    """Запитує у користувача рівень рекурсії"""
    while True:
        try:
            order = int(input("Введіть рівень рекурсії (рекомендовано від 1 до 10): "))
            if order < 0:
                print("Будь ласка, введіть невід'ємне число.")
            elif order > 10:
                confirm = input(f"Рівень {order} може працювати повільно. Продовжити? (так/ні): ")
                if confirm.lower() in ['так', 'yes', 'y', 'т']:
                    return order
            else:
                return order
        except ValueError:
            print("Будь ласка, введіть ціле число.")

# Основна частина програми
if __name__ == "__main__":
    
    # Запитуємо рівень рекурсії у користувача
    order = get_user_input()
    
    # Малюємо дерево
    print(f"Малюємо дерево Піфагора з рівнем рекурсії {order}...")
    draw_pythagoras_tree(order)
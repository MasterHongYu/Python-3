import turtle

# 創建一個畫布
screen = turtle.Screen()
screen.bgcolor("black")

# 創建一個海龜
star_turtle = turtle.Turtle()
star_turtle.speed(10)  # 設定畫筆速度

# 設定畫筆顏色
star_turtle.color("white")

# 函數來畫一個五角星
def draw_star(size):
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(144)

# 移動海龜到初始位置
star_turtle.penup()
star_turtle.goto(0, -100)
star_turtle.pendown()

# 繪製多個五角星
for _ in range(5):
    draw_star(200)
    star_turtle.right(144)

# 隱藏海龜
star_turtle.hideturtle()

# 關閉視窗
turtle.done()
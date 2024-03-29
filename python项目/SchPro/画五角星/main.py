import turtle as t

def draw_fiveStars(leng):
    count = 1
    while count <=5:
        t.fd(leng)
        t.rt(144)
        count += 1
    leng += 10
    if leng <=100:
        draw_fiveStars(leng)
def main():
    t.pu()
    t.bk(100)
    t.pd()
    t.pensize(2)
    t.pencolor('red')
    segment = 50
    draw_fiveStars(segment)
    t.exitonclick()
if __name__ == '__main__' :
    main()
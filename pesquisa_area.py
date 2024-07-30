def main():
    x=float(input("digite x"))
    y=float(input("digite y"))
    if((x>=(-4) or x<=(-3))and(y>=4 or y<=7))or((x>=(-3) or x<=(-2))and(y>=4 or y<=5))or((x>=(-3) or x<=(-2))and(y>=6 or y<=7))or((x>=(-2) or x<=(-1))and(y>=4 or y<=7))((x>=(1) or x<=(2))and(y>=4 or y<=7))((x>=(2) or x<=(3))and(y>=4 or y<=5))or((x>=(2) or x<=(3))and(y>=6 or y<=7))or((x>=(3) or x<=(4))and(y>=4 or y<=7))or((x>=(-3) or x<=(3))and(y>=1 or y<=2))or((x<=0 or x>=5)and(y<=0 or y>=8)):
        print("fora regiao")
    else:
        print("dentro regiao")

main()
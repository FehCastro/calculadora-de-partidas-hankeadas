def Saldo (vitorias, derrotas):
    resultado = vitorias - derrotas
    return resultado


v = int(input("Digite quantas vitórias você possui. "))
d = int(input("Digite quantas derrotas você possui. "))

r = Saldo(v, d)

if r < 10:
    print(f"O Herói tem {r} vitórias e está no nivél Ferro")
elif r >=  11 and r <= 20:
    print(f"O Herói tem {r} vitórias e está no nivél Bronze")
elif r >=  21 and r <= 50:
    print(f"O Herói tem {r} vitórias e está no nivél Prata")
elif r >=  51 and r <= 80:
    print(f"O Herói tem {r} vitórias e está no nivél Ouro")        
elif r >=  81 and r <= 90:
    print(f"O Herói tem {r} vitórias e está no nivél Diamante")       
elif r >=  91 and r <= 100:
    print(f"O Herói tem {r} vitórias e está no nivél Lendário")       
elif r >=  101:
    print(f"O Herói tem {r} vitórias e está no nivél Imortal")       


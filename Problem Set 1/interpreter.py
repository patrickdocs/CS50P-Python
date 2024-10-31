def main():
    x,y,z = [str(i) for i in input("Expression: ").split()]
    x, z = int(x), int(z)
    result = interpreter(x,y,z)
    print(f"{result:.1f}")

def interpreter(x,y,z):
    if y == "+": return(x + z)
    elif y == "-": return(x - z)
    elif y == "*": return(x * z)
    elif y == "/" and z != 0: return(x / z)

main()

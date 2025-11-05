def saludo(nombre: str) -> str:
    return f"Hola, {nombre}! Bienvenido/a a Git.22"

if __name__ == "__main__":
    nombre = input("¿Tu nombre? ")
    print(saludo(nombre))    

# funciones_matematicas.py
def suma(a, b):
    """
    Función que suma dos valores enteros.
    
    Args:
        a (int): Primer valor entero
        b (int): Segundo valor entero
    
    Returns:
        int: La suma de a y b
    """
    return a + b


def cuadrado(n):
    """
    Función que calcula el cuadrado de un valor entero.
    
    Args:
        n (int): Valor entero
    
    Returns:
        int: El cuadrado de n (n²)
    """
    return n * n


def cuadrado_binomio(a, b):
    """
    Función que calcula el cuadrado de un binomio.
    Aplica la fórmula: (a + b)² = a² + 2*a*b + b²
    
    Args:
        a (int): Primer término del binomio
        b (int): Segundo término del binomio
    
    Returns:
        int: El resultado del cuadrado del binomio
    """
    return cuadrado(a) + 2 * a * b + cuadrado(b)
    
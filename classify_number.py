# ---- Funciones provistas (NO modificar) ----

def is_even(n):
    """Dado un número entero n, retorna True si es par, False si es impar."""
    return n % 2 == 0

def is_positive(n):
    """Dado un número entero n, retorna True si es mayor a 0, False en caso contrario."""
    return n > 0

# ---- Función a implementar ----

def classify_number(n):


      if is_even(n) == True and is_positive(n) == True:
          return ("positive even")
      elif is_even(n) == False and is_positive(n) == True:
          return ("positive odd")
      elif is_even(n) == True and is_positive(n) == False and n!=0:
          return ("negative even")
      elif is_even(n) == False and is_positive(n) == False and n!=0:
          return ("negative odd")
      elif n==0:
          return ("zero")

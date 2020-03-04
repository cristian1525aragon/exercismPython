def sum_of_multiples(limite, multiplos):
    return sum(value for value in range(limite)
               if any(value % multiplos == 0
                      for multiplos in multiplos
                      if multiplos > 0))
    
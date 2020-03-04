def is_armstrong_number(numero):
    return sum(pow(int(a), len(str(numero))) for a in str(numero)) == numero

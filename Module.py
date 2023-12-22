def summa3(arv1:float,arv2:float,arv3:float)->float:
    """Kolme arvu summa
    
    :param float arv1: Esimene arv
    :param float arv2: Teine arv
    :param float arv3: Kolmas arv
    :rtype: float
    
    """

    summa=arv1+arv2+arv3
    return summa

def arithmetic(first: float, second: float, operation: str) -> float:
    """
    :param first: Первое число
    :param second: Второе число
    :param operation: Операция (+-*/)
    :rtype: float
    """
    if operation == '+':
        result = first + second
    elif operation == '-':
        result = first - second
    elif operation == '*':
        result = first * second
    elif operation == '/':
        if second != 0:
            result = first / second
        else:
            raise ValueError("Деление на ноль невозможно.")
    else:
        raise ValueError("Неподдерживаемая операция. Поддерживаются только: +, -, *, /")
    
    return result

#3

def square(arv1: float) -> float:
    """
    :param arv1: Число, для которого нужно возвести в квадрат.
    :return: Квадрат введенного числа.
    """
    result = arv1 * arv1
    return result

#4

def season(arv1: int) -> str:
    """
    :param arv1: Месяц.
    :return: Сезон.
    """
    talv = [12, 1, 2]
    kevad = [3, 4, 5]
    suvi = [6, 7, 8]
    sugis = [9, 10, 11]

    if arv1 in talv:
        return "talv"
    elif arv1 in kevad:
        return "kevad"
    elif arv1 in suvi:
        return "suvi"
    elif arv1 in sugis:
        return "sügis"
    else:
        return "Vigane kuu"

#2
def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine
    Tagastab true, kui liigaasta ja false kui on tavaline aasta
    :param int aasta: aasta number
    :rtype: bool tagastab loogilises formaadis tulemus

    """

    if aasta%4==0:
        v=True 
    else:
        v:False 
    return v 

#5

def bank(money:float,years:int)->float:
    """
    :param 1: Money
    :param 2: years
    :param 3: final
    """
    money = int(input("How many need to put: "))
    years = int(input("How many years: "))

    for i in range(years):
        money = money+money*0.1

    return money

 
 #6

 def is_prime(arv:int)->bool:

    """Number check
    :param 1: number
    :rtype: final number
    
    """

     arv = int(range(1,1001))
     if arv%arv == 0 and arv>1:
         return True
     else: 
         return False

#7

def date():

    """Date check
    :param 1: day
    :param 2: month
    :param 3: year
    :rtype: final result
    """

    day = int(input("Write day: "))
    if day < 31 and day <:
        print("Okay, write month:")
    else:
        print("Incorrect number")

    month = int(input("Write month: "))
    if month < 12:
        print("Okay, finally write year: ")
    else:
        print("Incorrect month: ")

    year = int(input("Write year: "))
    if year < 2024:
        final = day, month, year
        print(final)
    else:
        print("Incorrect year")






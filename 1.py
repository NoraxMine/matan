try:
    money = int(input("Сколько деньга есть?\n"))
except:
    print('Чет не так')
else:
    if money >= 50:
        print("идите в 3 зону")
    elif money >= 30:
        print("идите в 2 зону")
    elif money >= 10:
        print("идите в 1 зону")
    else:
        print("Мало денег, уходите")

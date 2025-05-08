import os


def shutdown():
    os.system("shutdown -s")

try:
    x = float(input('Введите ваши X координаты на пляже:\n'))
    y = float(input('Введите ваши Y координаты на пляже:\n'))
except:
    print('Вы чет не так ввели, но все равно взорвались!!!!')

print('Вы взорвались!')
shutdown()
x = input()
y = input()

try:
    result = int(x)/int(y)
except (ZeroDivisionError, ValueError, TypeError):
    print('ошибка =(')
else:
    print('result is', result)
finally:
    print('end') 
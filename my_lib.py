def get_week( n:int ):
    r = 'понедельник'
    if n == 1:
        r = 'понедельник'
    if n == 2:
        r = 'вторник'
    if n == 3:
        r = 'среда'
    if n == 4:
        r = 'четверг'
    if n == 5:
        r = 'пятница'
    if n == 6:
        r = 'суббота'
    if n == 0:
        r = 'воскресенье'
    return r
def convert(milliseconds):
    hour_in_milliseconds = 60*60*1000
    hours = milliseconds // hour_in_milliseconds
    milliseconds_left = milliseconds % hour_in_milliseconds
    minutes_in_milliseconds = 60*1000
    minutes = milliseconds_left // minutes_in_milliseconds
    milliseconds_left %= minutes_in_milliseconds
    seconds = milliseconds_left // 1000
    return f'{hours} hour/s'*(hours != 0) + f' {minutes} minute/s'*(minutes != 0) + f' {seconds} second/s' *(seconds != 0) or f'just {milliseconds} millisecond/s' * (milliseconds < 1000)
is_invalid = False

while True:
    info = """
Please enter the milliseconds (should be greater than zero) : """
    alphanum = input('\nNot Valid Input !!!\n'*is_invalid + info).strip()
    if not alphanum.isdecimal():
        if alphanum.lower() == 'exit':
            print('\nExiting the program... Good Bye')
            break
        else:
            is_invalid = True
            continue
    millisecs = int(alphanum)
    if 0 < millisecs:
        print(f'\nMilliseconds of "{alphanum}"" is equal to {convert(millisecs)}')
        is_invalid = False
    else:
        is_invalid = True
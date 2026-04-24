def check_year(prompt):
    while True:
        year = input(prompt)
        try:
            return int(year)
        except ValueError:
            print('Enter a number.')
            continue


print('Is it a leap year?')
while True:
    year = check_year('Enter the year: ')
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('Leap.')
    else:
        print('Not leap.')
    while True:
        ans = input('Another year? y/n: ').lower()
        if ans == 'y':
            break
        elif ans == 'n':
            print('Thank you!')
            exit()
        else:
            print('Invalid answer.')
            continue

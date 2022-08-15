def user_telephone(code):
    def qwert(number):
        print(code + number)

    return qwert


my_number = user_telephone('+044')

my_number('838372893')
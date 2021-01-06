def get_info():
    return input('enter your info:name family age)\n').split()


info = get_info()

template = f"""
NAME: {info[0].title()}
LAST: {info[1].upper()}
AGE: {info[2]}
*******************"""
file = open('names.txt', 'a')
file.write(template)
file.close()
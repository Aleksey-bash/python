import re
EMAIL = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')


def email_parse(email):
    found_info = EMAIL.findall(email)[0]
    if found_info:
        name, adr = found_info
    else:
        raise ValueError(f'wrong email: {email}')
    print(name, adr)


email_parse('zakharovaleksey777@gmail.com')
email_parse('zakharovaleksey777gmail.com')




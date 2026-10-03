def pure(name):
    
    duplicate = name.strip().title()
    return duplicate

def first_name(username):
    first= pure(username)[0:pure(username).find(" ")]
    return first


def last_name(username):
    last = pure(username)[pure(username).find(" "):len(pure(username))]
    return last

def email_converter(email):
    
    purify = email.strip().lower()
    unhidden = purify[1:purify.find("@")]
    count = "*"*len(unhidden)
    gmail = purify.replace(unhidden, count)
    return(gmail)


def hide_password(pas):
    code = "*" * len(pas)
    passcode = pas.replace(pas, code)
    return passcode

from models import User, List

# Auxiliary functions

# Takes username and password and returns the user's first name
def getName(usr, pwd):
    results = User.objects.filter(user_name = usr, password = pwd, is_admin = True)
    return str(results.values_list('first_name', flat = True).get())

# Takes username and password and searches database for an admin account
def adminExists(usr, pwd):
    results = User.objects.filter(user_name = usr, password = pwd, is_admin = True)
    if(len(results) > 0):
        return True
    else:
        return False

def getListNames():
    results = List.objects.filter()
    r = results.values_list('name', flat = True)
    return r

def getListUsers(listName):
    results = User.objects.filter(lists__name = listName).order_by("last_name")
    r = results.values_list(flat = True)
    return r

def getSenderEmails():
    results = User.objects.filter(is_sender = True)
    r = results.values_list('email', flat = True)
    return r

def generateUserName(first, last):
    number = 0
    flag = True
    first = first[0]
    usr = first + last
    while flag:
        results = User.objects.filter(user_name = usr)
        if(len(results) > 0):
            flag = True
            number = number + 1
            usr = usr + str(number)
        else:
            flag = False
    return usr

# TODO: return false if file type is not an image
# Replaces the site logo with the file f
def replaceLogo(f):
    try:
        with open('evvdayschool/static/res/logo.jpg', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return True
    except:
        return False
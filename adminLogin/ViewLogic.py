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

def getUserListNames(userEmail):
    u = User.objects.filter(email = userEmail)[0]
    ul = u.lists
    userLists = ul.values_list('name', flat = True)
    return userLists

def getUserListOwnership(userEmail):
    ownership = []
    lists = getListNames()
    userLists = getUserListNames(userEmail)
    for i in range(len(lists)):
        if lists[i] in userLists:
            ownership.append(True)
        else:
            ownership.append(False)
    final = []
    for i in range(len(lists)):
        final.append([lists[i], ownership[i]])
    return final

def removeUserFromList(userEmail, list):
    l = List.objects.filter(name = list)
    u = User.objects.filter(email = userEmail)[0]
    if len(l) > 0:
        u.lists.remove(l[0])

def addUserToList(userEmail, list):
    l = List.objects.filter(name = list)[0]
    u = User.objects.filter(email = userEmail)[0]
    u.lists.add(l)

def addUserLists(email, lists):
    for list in lists:
        if list[1] == "0":
            removeUserFromList(email, list[0])
        else:
            addUserToList(email, list[0])

def getListUsers(listName):
    results = User.objects.filter(lists__name = listName).order_by("last_name")
    r = results.values_list(flat = True)
    return r

def stringToList(str):
    list = str.split(",")
    for i in range(0, len(list)):
        list[i] = list[i].split("|")
    del list[-1]
    return list

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
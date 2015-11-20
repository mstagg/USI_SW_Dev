from models import User, List

# Auxiliary functions

# Takes username and password and searches database for the user
# Returns the user's first name
def getName(usr, pwd):
    results = User.objects.filter(user_name = usr, password = pwd, is_admin = True)
    return str(results.values_list('first_name', flat = True).get())


# Takes username and password and searches database for an admin account
# Returns true if admin account exists
def adminExists(usr, pwd):
    results = User.objects.filter(user_name = usr, password = pwd, is_admin = True)
    if(len(results) > 0):
        return True
    else:
        return False


# Searches database for mailing list names
# Returns a list of strings
def getListNames():
    results = List.objects.filter()
    r = results.values_list('name', flat = True)
    return r


# Searches database for mailing list names that belong to a specific sender
# Returns list of strings
def getUserListNames(userEmail):
    u = User.objects.filter(email = userEmail)[0]
    ul = u.lists
    userLists = ul.values_list('name', flat = True)
    return userLists


# Searches database for all mailing list names and shows whether a specific sender owns each list
# Returns 2D list in format [[LISTNAME, OWNERSHIP], [LISTNAME, OWNERSHIP], etc...]
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


# Takes a user's email and removes that user from a given list
def removeUserFromList(userEmail, list):
    l = List.objects.filter(name = list)[0]
    u = User.objects.filter(email = userEmail)[0]
    u.lists.remove(l[0])


# Takes a user's email and adds that user to a given list
def addUserToList(userEmail, list):
    l = List.objects.filter(name = list)[0]
    u = User.objects.filter(email = userEmail)[0]
    u.lists.add(l)


# Takes a user's email and adds or removes that user from a list based on data in 2D list
# 2D list in format [[LISTNAME, OWNERSHIP], [LISTNAME, OWNERSHIP], etc...]
def addUserLists(email, lists):
    for list in lists:
        if list[1] == "0":
            removeUserFromList(email, list[0])
        else:
            addUserToList(email, list[0])


# Takes a list name and searches the database for all users in the list
# Returns list of strings
def getListUsers(listName):
    results = User.objects.filter(lists__name = listName).order_by("last_name")
    r = results.values_list(flat = True)
    return r


# Used to convert a string of data from POST request into a python list
# Input in format "LISTNAME|OWNERSHIP,LISTNAME|OWNERSHIP, etc...]
# Returns 2D python list
def stringToList(str):
    list = str.split(",")
    for i in range(0, len(list)):
        list[i] = list[i].split("|")
    del list[-1]
    return list


# Searches database for all users that are senders
# Returns a list of email strings
def getSenderEmails():
    results = User.objects.filter(is_sender = True)
    r = results.values_list('email', flat = True)
    return r


# Generates a username by combining the first letter of the first name
# with the last name
# Returns username as string
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
# Returns true if operation was successful
def replaceLogo(f):
    try:
        with open('evvdayschool/static/res/logo.jpg', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return True
    except:
        return False
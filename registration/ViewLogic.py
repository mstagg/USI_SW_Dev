from adminLogin.models import User, List, AccountStatus

# Auxiliary functions

# Searches database for mailing list names
# Returns a list of strings
def getListNames():
    results = List.objects.filter()
    r = results.values_list('name', flat = True)
    return r

def getActiveStatus():
    try:
        results = AccountStatus.objects.filter().order_by('-change_date')[0]
        return results.active_code
    except:
        return True


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

# Used to convert a string of data from POST request into a python list
# Input in format "LISTNAME|OWNERSHIP,LISTNAME|OWNERSHIP, etc...]
# Returns 2D python list
def stringToList(str):
    list = str.split(",")
    for i in range(0, len(list)):
        list[i] = list[i].split("|")
    del list[-1]
    return list

# Takes a user's email and adds that user to a given list
def addUserToList(usrnme, list):
    l = List.objects.filter(name = list)[0]
    u = User.objects.filter(user_name = usrnme)[0]
    u.lists.add(l)
    l.size = l.size + 1
    l.save


# Takes a user's email and adds or removes that user from a list based on data in 2D list
# 2D list in format [[LISTNAME, OWNERSHIP], [LISTNAME, OWNERSHIP], etc...]
def addUserLists(usrnme, lists):
    for list in lists:
        if list[1] == "0":
            pass
        else:
            addUserToList(usrnme, list[0])

def userExists(first, last, phone):
    l = User.objects.filter(first_name = first, last_name = last, phone = phone)
    if(len(l) > 0):
        return False
    else:
        return True

def getUserLists(first, last, phone):
    u = User.objects.filter(first_name = first, last_name = last, phone = phone)[0]
    return u.lists.values_list('name', flat = True)


def addUser(first, last, phone, lists):
    u = User(user_name = generateUserName(first, last),
                 password = "",
                 email = "",
                 pin = 0,
                 is_admin = False,
                 is_sender = False,
                 first_name = first,
                 last_name = last,
                 phone = phone,
                 active = False)
    l = stringToList(lists)
    if(userExists(u.first_name, u.last_name, u.phone)):
        u.save()
        addUserLists(u.user_name, l)
        u.save()

def activateUser(first, last, phone):
    u = User.objects.filter(first_name = first, last_name = last, phone = phone)[0]
    u.active = True
    u.save()


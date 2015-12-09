import datetime
from adminLogin.models import User, Message, AccountStatus

# Auxiliary functions

# Takes username and password and searches database for an admin account
# Returns true if admin account exists
def senderExists(em, p):
    results = User.objects.filter(email = em, pin = p, is_sender = True)
    if(len(results) > 0):
        return True
    else:
        return False


def getListUsers(listName):
    results = User.objects.filter(active = True,lists__name = listName).order_by("last_name")
    r = results.values_list(flat = True)
    return r

def getSenderLists(userEmail):
    u = User.objects.filter(email = userEmail, is_sender = True)[0]
    ul = u.lists
    userLists = ul.values_list('name', flat = True)
    rtn = []
    for u in userLists:
        t = []
        t.append(str(u))
        t.append(str(len(getListUsers(u))))
        rtn.append(t)
    return rtn

def send(msg, list):
    m = Message(msg = msg, list = list, change_date = datetime.datetime.now())
    m.size = len(getListUsers(list))
    m.save()

def enoughTokens(size):
    s = AccountStatus.objects.all().order_by('-change_date')[0]
    tst = s.token_amount - size
    if tst < 0:
        return False
    else:
        return True

def removeTokens(size):
    acc = AccountStatus.objects.all().order_by('-change_date')[0]
    s = acc.token_amount
    s = s - size
    a = AccountStatus(token_amount = s)
    a.security_code = acc.security_code
    a.active_code = acc.active_code
    a.token_amount = s
    a.change_date = datetime.datetime.now()
    a.save()

def numTokens():
    acc = AccountStatus.objects.all().order_by('-change_date')[0]
    return acc.token_amount
import datetime
from adminLogin.models import User

# Auxiliary functions

# Takes username and password and searches database for an admin account
# Returns true if admin account exists
def senderExists(em, p):
    results = User.objects.filter(email = em, pin = p, is_sender = True)
    if(len(results) > 0):
        return True
    else:
        return False


def getSenderLists(userEmail):
    u = User.objects.filter(email = userEmail, is_sender = True)[0]
    ul = u.lists
    userLists = ul.values_list('name', flat = True)
    return userLists
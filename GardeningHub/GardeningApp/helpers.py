from .models import RegisteredUsers


def verify(username, password):
    results = RegisteredUsers.objects.filter(userName=username)
    if len(results) == 0:
        return False
    if results[0].password != password:
        return False
    return True


def checkUsernameDuplication(username):
    results = RegisteredUsers.objects.filter(userName=username)
    if len(results) > 0:
        # someone is using entered username
        return True
    # if username is available
    return False

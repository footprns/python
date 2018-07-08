import time
# default value is calculate one time when function executed
def show_default(arg=time.ctime()):
    print(arg)

def show_default_current(arg=None):
    if arg is None:
        arg = arg=time.ctime()
    return arg


def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu

# Get Path actual
def currentFile():
    import sys
    import os

    # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        currentPath = os.path.dirname(sys.executable)
    elif __file__:
        currentPath = os.path.dirname(__file__)        
    return currentPath

c = currentFile()
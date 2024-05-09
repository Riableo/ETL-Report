# Get Path actual
def currentFile():
    import sys
    import os
    from log import manageLog

    # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        currentPath = os.path.dirname(sys.executable)
        # extFile = '../Informes/Inform'+d+'.pdf'
        
        # Validate entry
        #print('exe current')
        manageLog('Process','Execute by .exe')
    elif __file__:
        currentPath = os.path.dirname(__file__)
        # extFile = '../Informes/Inform'+d+'.pdf'
        
        # Validate entry
        print('por codigo')
        manageLog('Process', 'Execute by script file')
    return currentPath

c = currentFile()
from functions import fileDate

# if not exist create, but if exist add to note
def manageLog(text = 'Start Process...', mssg = ''):
    import os
    import currentPath

    # c,extFile = currentFile()

    txtFile = os.path.join(currentPath.c,'log.txt')

    try:
        f = open(txtFile, 'r')
    except FileNotFoundError:  
        date = fileDate('log')
        
        # create if not exist
        f = open(txtFile, 'w')
        f.write('File created at '+date)
        f.write('\n' + '-------------------')
        f.write('\n' + '['+date+'] Process beginning')
        f.close()
    else:
        date = fileDate('log')
        # Add to note
        match text:
            
            case 'Start Process...':
                f = open(txtFile, 'a')
                f.write('\n' + '-------------------')
                f.write('\n' + '['+date+'] Process beginning')
                f.close()
            case 'Process':
                f = open(txtFile, 'a')
                f.write('\n' + '['+date+'] ' + mssg)
                f.close()
            case 'Diagram':
                f = open(txtFile, 'a')
                f.write('\n' + '['+date+'] Diagram created ' + mssg)
                f.close()
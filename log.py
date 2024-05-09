from functions import fileDate

# if not exist create, but if exist add to note
def manageLog(text = 'Start Process...', mssg = ''):
    try:
        f = open('log.txt', 'r')
    except FileNotFoundError:  
        date = fileDate('log')
        
        # create if not exist
        f = open('log.txt', 'w')
        f.write('File created at '+date)
        f.write('\n' + '-------------------')
        f.write('\n' + '['+date+'] Process beginning')
        f.close()
    else:
        date = fileDate('log')
        # Add to note
        match text:
            
            case 'Start Process...':
                f = open('log.txt', 'a')
                f.write('\n' + '-------------------')
                f.write('\n' + '['+date+'] Process beginning')
                f.close()
            case 'Process':
                f = open('log.txt', 'a')
                f.write('\n' + '['+date+'] ' + mssg)
                f.close()
            case 'Diagram':
                f = open('log.txt', 'a')
                f.write('\n' + '['+date+'] Diagram created ' + mssg)
                f.close()

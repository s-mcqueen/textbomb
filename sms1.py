from twilio.rest import TwilioRestClient
import re

client = TwilioRestClient()

def cleanNum(dirtyNum):
    ''' formats a phone number '''
    return "+1" + re.sub('[ )(-]','',dirtyNum).strip("\n")

def cleanList(dirtyList):
    ''' formats a list of phone numbers '''
    return [cleanNum(d) for d in dirtyList]

def readIn(numFile):
    ''' Parse a text file of phone numbers into a list, 
        and clean up the formatting of the list before returning '''
    f = open(numFile, 'r')
    lines = f.readlines()
    return cleanList(lines) 

def sms(toNum, textBody):
    ''' Send a message to a phone number '''
    client.sms.messages.create(to=toNum, from_="+13602052266", body=textBody)
    print "sent the message: (" + textBody + ") to " + toNum

def textBomb(numbers, textBody):
    ''' Send a message to a list of phone numbers '''
    for num in numbers:
        sms(num, textBody)

# def sendOne():
#     ''' Send 1 message to 1 phone number from commandline '''
#     rawNum = raw_input("Enter a phone number: ")
#     text = raw_input("Enter a text message to send: " )
#     go = raw_input("Send? (type yes or no) " )
    
#     toNum = cleanNum(rawNum) 

#     if (go == "yes"):
#         print "ok, sending..............."
#         sms(toNum, text)
#     else:
#         print "ok, not sent"
  
def bombsAway():
    ''' Call textbomb from commandline '''
    # numFile = raw_input("Enter a file name: ")
    numFile = "numbers.txt" # for ease of use right now...
    text = raw_input("Enter a text message to send: ")
    go = raw_input("Send? (type yes or no) ")

    if (go == "yes"):
        print "ok, preparing numbers.............."
        numbers = readIn(numFile)
        print "sending texts................."
        textBomb(numbers, text)
    else:
        print "ok, not sent"

def main():
    bombsAway()

if __name__ == "__main__":
    main()

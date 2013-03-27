from twilio.rest import TwilioRestClient
import re

client = TwilioRestClient()

def cleanNum(dirtyNum):
    ''' cleans up phone number formatting '''
    clean = re.sub('[ )(-]','', dirtyNum)
    clean = "+1" + clean
    return clean

def cleanList(dirtyList):
    c = []

    for d in dirtyList:
        c.append(cleanNum(d))
    return c

def sms(toNum, textBody):
    ''' sends a given text to a given phone number '''
    client.sms.messages.create(to=toNum, from_="+13602052266", body=textBody)
    print "sent the message: (" + textBody + ") to " + toNum

def textBomb(numbers, textBody):
    i=0
    for num in numbers:
        sms(num, textBody)
        i+=1
    print "sent " + str(i) + " texts"


def readIn(numFile):
    f = open(numFile, 'r')
    lines = []
    for l in f:
        lines.append(l)
    cleanedInput = cleanList(lines) 
    return cleanedInput

def sendOne():
    rawNum = raw_input("Enter a phone number: ")
    text = raw_input("Enter a text message to send: " )
    go = raw_input("Send? (type yes or no) " )
    
    toNum = cleanNum(rawNum) 

    if (go == "yes"):
        print "ok, sending..............."
        sms(toNum, text)
    else:
        print "ok, not sent"

def sendBomb():
    numFile = raw_input("Enter a file name: " )
    text = raw_input("Enter a text message to send: " )
    go = raw_input("Send? (type yes or no) " )

    if (go == "yes"):
        print "ok, preparing numbers.............."
        numbers = readIn(numFile)
        print "sending texts................."
        textBomb(numbers, text)
    else:
        print "ok, not sent"

def main():
   sendOne()

if __name__ == "__main__":
    main()

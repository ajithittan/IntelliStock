import configparser
import configparser
from TurtleProgram import retrievedatafromweb

class checkTriggers:

    def checkforsignificantchange (self,inpVal):

        listofStks = retrievedatafromweb().retDataToRun(inpVal)

        for eachstk in listofStks:
            print("test...")

        print("trigger....",listofStks)

    def triggercondhit(self,inpStk):

        config = configparser.ConfigParser()
        config.read("configitems.ini")

        listofStks = retrievedatafromweb().retDataToRun(inpVal)


#objretdata = checkTriggers()
#objretdata.checkforsignificantchange("CURRENT")

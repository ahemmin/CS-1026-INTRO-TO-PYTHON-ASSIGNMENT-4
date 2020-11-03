from processUpdates import Processor_for_Updates_File,processUpdates

cntryFileName=input("file containing country data: ")
updateFileName=input("file containing updates: ")
c=processUpdates(cntryFileName,updateFileName)

print("Processing country data...")

from catalogue import CountryCatalogue          #Importing class CountryCatalogue

def processUpdates(cntryFileName,updateFileName):       #Main function that actually changes values and export new version of data base
    Output_For_Exit_Without_Entries=open("output.txt","w")
    x=0
    while x!=True:      #Will remain asking for new files if either does not run
        try:        #Managing exceptions
            Update_File=open(updateFileName,"r",encoding="utf-8")#Attempts to open update file
            Update_Data=Processor_for_Updates_File(Update_File)#Processes updates file
            Original_Country_Data=CountryCatalogue(cntryFileName)   #Processing country file
            Country_List=Original_Country_Data.Country_List_Maker()#Creating country list
            for Country in Update_Data:#Iterates over country keys in update file
                x=True      #Stops while loop
                Country_Values=Update_Data[Country]    #Creates dictionary with data type (P,A or C) as key and associated value as value
                for Data_Type in Country_Values:#Iterates over data types present in the updates for a given country
                    Data_Type_Values=Country_Values[Data_Type]#Accessing associated value for given data type
                    if Data_Type=="P":#Using previous functions the values are changed according to the data type sorted by if statements
                        if Country in Country_List:
                            Original_Country_Data.setPopulationofCountry(Country,Data_Type_Values)
                        else:   #For any of these else statements they exist to deal with updates present for countries that do not exist in the original data base, therefore must be added both to data base and country list
                            Original_Country_Data.addCountry(Country,"",Data_Type_Values)
                            Country_List.append(Country)
                    elif Data_Type=="A":
                        if Country in Country_List:
                            Original_Country_Data.setAreaofCountry(Country,Data_Type_Values)
                        else:
                            Original_Country_Data.addCountry(Country,"","",Data_Type_Values)
                            Country_List.append(Country)
                    elif Data_Type=="C":
                        if Country in Country_List:
                            Original_Country_Data.setContinentofCountry(Country,Data_Type_Values)
                        else:
                            Original_Country_Data.addCountry(Country,Data_Type_Values)
                            Country_List.append(Country)
            Original_Country_Data.saveCountryCatalogue("output.txt")#Exports results
            return True

        except:     #Deals with non-existent files
            Response=input("Would you like to quit the program?(Y(yes) or N(no))=: ")
            Response=Response.lower()
            if Response=="n":       #Used to obtain new file names that can be checked to see if they exist and therefore can be opened
                print("At least one file does not exist")
                updateFileName=input("Select a new update file: ")
                cntryFileName=input("Select a new country file: ")
            else:       #Result if user chooses to quit
                Output_For_Exit_Without_Entries.write("Update Unsuccessful\n")
                return False

def Processor_for_Updates_File(Update_File):        #Processes updates file
    Formatted_Updates_for_Countries= {}
    for line in Update_File:        #Iterates over lines in update files
        Sub_dictonary={}
        Stripping_Punc=line.replace(" ","")
        Stripping_Punc2=Stripping_Punc.strip("\n")     #Strip punctuation (\n)
        Splitting_into_List=Stripping_Punc2.split(";")   #Creating list where elements are split at ;
        Country_Name=Splitting_into_List[0]     #Storing country name to be used as key in dictionary
        for i in range(1,len(Splitting_into_List)): #Iterating over length of list contained in given country key (contains update data)
           Splitting_Data=Splitting_into_List[i].split("=")     #Splits data type (P,A,C) from its value at = as elements in a list
           Data_Type=Splitting_Data[0]      #Storing data type
           Sub_dictonary[Data_Type]=Splitting_Data[1]       #Making subdictionary with data type as key and associated value as value
           Formatted_Updates_for_Countries[Country_Name]=Sub_dictonary  #Adds subdictionary as the values for a given country key

    return Formatted_Updates_for_Countries

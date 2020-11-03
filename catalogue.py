from country import Country         #Import Class

class CountryCatalogue:         #Creating new class CountryCatalogue

    def __init__(self,countryFile):         #Constructor
        try:                    #Try/except statement to ensure files exist
            self._countryFile=open(countryFile,"r",encoding="utf-8")    #Attempting to open country file
            self._countryCat={}         #Initializing dictionary
            for line in self._countryFile:          #Iterating over each line of data in country file
                Stripping_Punc=line.strip("\n")     #Stripping punctuation (\n)
                Splitting_into_List=Stripping_Punc.split("|")   #Creating list, seperating elements at vertical bar
                Country_Name=Splitting_into_List[0]     #Isolating country name so that it can be used as key in dictionary
                self._countryCat[Country_Name]=Splitting_into_List[1:4]     #Creating dictionary with country names as keys and values are remaining list elements
        except:
            print()


    def setPopulationofCountry(self,Country_Name,population):       #Sets population for a given country to new value
        self._countryCat[Country_Name][1]=population                #Changes 2nd element in list contained in given country key
        return self._countryCat

    def setAreaofCountry(self,Country_Name,area):           #Sets area for given country to new value
        self._countryCat[Country_Name][2]=area             #Changes 3rd element in list contained in given country key
        return self._countryCat

    def setContinentofCountry(self,Country_Name,continent):     #Sets continent for given country
        self._countryCat[Country_Name][0]=continent         #Changes 1st element in list contained in given country key
        return self._countryCat

    def findCountry(self,Country_Name):         #Checks to see if country in data base
       if Country_Name in self._countryCat:
           return Country_Name+":", self._countryCat[Country_Name]      #returns object or nothing
       else:
           return None

    def addCountry(self,Country_Name="",continent="",population="",area=""):      #Adds countries to data base
        if Country_Name not in self._countryCat:        #Checks to see if country already exists in data base
            self._countryCat[Country_Name]=[continent,population,area]      #Creates new key with sepcified values obtained from parameters
            return True
        else:
            return False       #Returned if country already exists in data base

    def printCountryCatalogue(self):        #Prints data in data base in readable fashion/format
        for Country_Name in self._countryCat:       #Iterating over country keys
            Organized_info=Country(Country_Name,self._countryCat[Country_Name][1],self._countryCat[Country_Name][2],self._countryCat[Country_Name][0])  #Formatting
            Formatted_Data=Organized_info.__rep__()     #Utilizing previous function to print in readable manner
            print(Formatted_Data)

    def saveCountryCatalogue(self,fname):       #Writes/exports results to a text document
        Vertical_Bar="|"
        New_Line="\n"
        Name_of_file=str(fname)
        Output_file=open(Name_of_file,"w")  #Opening file for writing
        Output_file.write("Country"+Vertical_Bar+"Continent"+Vertical_Bar+"Population"+Vertical_Bar+"Area"+New_Line) #Formatting
        self._countryCat.pop("Country")#Get rid of titles prior to sorting
        for Country_Name in sorted(self._countryCat):#Sorting dictionary alphabetically
            Output_file.write(Country_Name+Vertical_Bar+self._countryCat[Country_Name][1]+Vertical_Bar+self._countryCat[Country_Name][2]+Vertical_Bar+self._countryCat[Country_Name][0]+New_Line)#Writing formatted data to outfile

    def Country_List_Maker(self):   #Creates a list of countries in data base
        Country_List=[]
        for Country_Name in self._countryCat:   #Iterates over country keys in dictionary
            Country_List.append(Country_Name)       #Adds country name to list
        return Country_List








class Country:          #Creating class country

    def __init__(self,name,pop,area,continent):             #Constructor
        self._name=name         #Creating Instance Variables
        self._pop=pop
        self._area=area
        self._continent=continent

    def getName(self):              #Returns country name
        return self._name

    def getPopulation(self):        #Returns country population
        return self._pop

    def getArea(self):              #Returns country area
        return self._area

    def getContinent(self):         #Returns country continent
        return self._continent

    def setPopulation(self,New_Population):     #Sets population for given country to desired value designated by parameter(argument)
        self._pop=int(New_Population)

    def setArea(self,New_Area):             #Sets area for given country to desired area value
        self._area=int(New_Area)

    def setContinent(self,New_Continent):           #Sets continent for a given country to desired continent
        self._continent=int(New_Continent)

    def __rep__(self):          #Formatting data for given country into readable statement
        return str(self._name)+"(pop: "+ str(self._pop)+", size: "+str(self._area)+") in "+str(self._continent)




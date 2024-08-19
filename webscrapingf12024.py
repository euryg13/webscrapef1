import re
from urllib.request import urlopen



from bs4 import BeautifulSoup
def openlink(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return(html)


drivers_list = ["Max Verstappen", "Lando Norris", "Charles Leclerc", "Oscar Piastri", "Carlos Sainz", "Lewis Hamilton", "Sergio Perez", "George Russel", "Fernando Alonso", "Lance Stroll", "Nico Hulkenberg", "Yuki Tsunoda", "Daniel Riccardo", "Oliver Bearman", "Pierre Gasly", "Kevin Magnussen", "Esteban Ocon", "Alexander Albon", "Zhou Guanyu", "Logan Sargeant", "valterri Bottas"]


html_site = openlink("https://www.formula1.com/en/results/2024/races")

soup = BeautifulSoup(html_site , "html.parser")

text_of_site = soup.get_text()


print(text_of_site)

#print(re.findall("Bahrain", text_of_site))

refined_text_of_site = (text_of_site.removeprefix("2024 RACE RESULTSSkip to contentF1®F2™F3™F1® ACADEMYAuthenticsStoreTicketsHospitalityExperiencesSign InSubscribeLatestVideoF1 UnlockedScheduleResultsDriversTeamsGamingLive TimingdefaultmobiletabletlaptopdesktopdesktopWideSeason202420232022202120202019201820172016201520142013201220112010200920082007200620052004200320022001200019991998199719961995199419931992199119901989198819871986198519841983198219811980197919781977197619751974197319721971197019691968196719661965196419631962196119601959195819571956195519541953195219511950CategoriesRacesDriversTeamsDHL Fastest Lap AwardResultsAllBahrainSaudi ArabiaAustraliaJapanChinaMiamiEmilia-RomagnaMonacoCanadaSpainAustriaGreat BritainHungaryBelgiumNetherlandsItalyAzerbaijanSingaporeUnited StatesMexicoBrazilLas VegasQatarAbu Dhabi2024 RACE RESULTSGrand PrixDateWinnerCarLapsTime"))

user_input = input("What race do you want to know about? (Type in the country's name) ")

index_of_input = (refined_text_of_site.find(user_input))

list_of_2024 = []

for x in re.finditer('2024', refined_text_of_site):
         print('2024 found', x.start(), x.end())
         list_of_2024.append(x.start())

print(list_of_2024)

def closest_2024(list_of_2024, index_of_input, refined_text_of_site, drivers_list):
    index_2024 = (min(list_of_2024, key=lambda x: abs(x - index_of_input)))
    sectioned_string = (refined_text_of_site[(index_2024+3):(index_2024+20)])
    f = "4Max VerstappenVE"
    for driver in drivers_list:
        if driver in sectioned_string:
            return print(driver, "is the winner of that race!")


closest_2024(list_of_2024, index_of_input, refined_text_of_site, drivers_list)





#Alright future me, this is my thought process, for when you have to come back later and hate yourself for everything you've written in this godforesaken program.
# I was thinking that since the length of the race names aren't consistent, but what IS consistent is the length of the year numbers, 2024, (4), it makes it easy
# to find the closest 2024 and move over to the name right next to it. Our issue now is trying to store these indexes with their respective 2024s.


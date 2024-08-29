import tkinter as tk
from tkinter import ttk

root=tk.Tk()

def button_clicked():
    print("congrats u clicked a button. retard.")









#-----------------------------------------------------------------------------

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




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BUTTONS FOR EACH RACE'S WINNER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


list_of_countries = {
    "ba" : "Bahrain",
    "sa" : "Saudi Arabia",
    "au" : "Australia",
    "ja" : "Japan",
    "ch" : "China",
    "mi" : "Miami",
    "em" : "Emilia-Romagna",
    "mo" : "Monaco",
    "ca" : "Canada",
    "sp" : "Spain",
    "as" : "Austria",
    "gr" : "Great Britain",
    "hu" : "Hungary",
    "be" : "Belgium",
    "ne" : "Netherlands",
    "it" : "Italy",
    "az" : "Azerbaijan",
    "si" : "Singapore",
    "un" : "United States",
    "me" : "Mexico",
    "br" : "Brazil",
    "la" : "Las Vegas",
    "qa" : "Qatar",
    "ab" : "Abu Dhabi"
}

user_input = None

def race_chosen(key):

    global user_input
    user_input = key
    #root.destroy()
    return user_input




Bahrain = ttk.Button(root, text='Bahrain', command=lambda: race_chosen(list_of_countries["ba"])).pack()


SaudiArabia = ttk.Button(root, text='Saudi Arabia', command=lambda: race_chosen(list_of_countries["sa"])).pack()


Australia = ttk.Button(root, text='Australia', command=lambda: race_chosen(list_of_countries["au"])).pack()


Japan = ttk.Button(root, text='Japan', command=lambda: race_chosen(list_of_countries["ja"])).pack()


China = ttk.Button(root, text='China', command=lambda: race_chosen(list_of_countries["ch"])).pack()


Miami = ttk.Button(root, text='Miami', command=lambda: race_chosen(list_of_countries["mi"])).pack()


Emilia_Romagna = ttk.Button(root, text='Emilia-Romagna', command=lambda: race_chosen(list_of_countries["em"])).pack()


Monaco = ttk.Button(root, text='Monaco', command=lambda: race_chosen(list_of_countries["mo"])).pack()


Canada = ttk.Button(root, text = 'Canada', command=lambda: race_chosen(list_of_countries["ca"])).pack()


Spain = ttk.Button(root, text='Spain', command=lambda: race_chosen(list_of_countries["sp"])).pack()


Austria = ttk.Button(root, text='Spain', command=lambda: race_chosen(list_of_countries["as"])).pack()


Great_Britain = ttk.Button(root, text="Great Britain", command=lambda: race_chosen(list_of_countries["gr"])).pack()


Hungary = ttk.Button(root, text="Hungary", command=lambda: race_chosen(list_of_countries["hu"])).pack()


Belgium = ttk.Button(root, text="Belgium", command=lambda: race_chosen(list_of_countries["be"])).pack()


Netherlands = ttk.Button(root, text="Netherlands", command=lambda: race_chosen(list_of_countries["ne"])).pack()


Italy = ttk.Button(root, text="Italy", command=lambda: race_chosen(list_of_countries["it"])).pack()


Azerbaijan = ttk.Button(root, text="Azerbaijan", command=lambda: race_chosen(list_of_countries["az"])).pack()


Singapore = ttk.Button(root, text="Singapore", command=lambda: race_chosen(list_of_countries["si"])).pack()


United_States = ttk.Button(root, text="United States", command=lambda: race_chosen(list_of_countries["un"])).pack()


Mexico = ttk.Button(root, text="Mexico", command=lambda: race_chosen(list_of_countries["me"])).pack()

Las_Vegas = ttk.Button(root, text="Las Vegas", command=lambda: race_chosen(list_of_countries["la"])).pack()


Qatar = ttk.Button(root, text="Qatar", command=lambda: race_chosen(list_of_countries["qa"])).pack()

Abu_Dhabi = ttk.Button(root, text="Abu Dhabi", command=lambda: race_chosen(list_of_countries["ab"])).pack()

driver = ""

label = ttk.Label(root, text=driver)




root.mainloop()

#So the issue here is that I was trying to get the window to live update. Problem is, is that no code past root.mainloop() will run as long as the window stays open. Suggested methods online
# are root.after() which I don't think works for this specific program. Then again at the time of writing this I'm on the cusp of a huge migraine.
# Multithreading is another option which I haven't explored in depth enough yet to rule out. I'm tired. 



index_of_input = (refined_text_of_site.find(user_input))

list_of_2024 = []



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BUTTONS FOR EACH RACE'S WINNER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




for x in re.finditer('2024', refined_text_of_site):
         print('2024 found', x.start(), x.end())
         list_of_2024.append(x.start())

print(list_of_2024)

def closest_2024(list_of_2024, index_of_input, refined_text_of_site, drivers_list):
    index_2024 = (min(list_of_2024, key=lambda x: abs(x - index_of_input)))
    sectioned_string = (refined_text_of_site[(index_2024+3):(index_2024+20)])
    f = "4Max VerstappenVE"
    global driver
    for driver in drivers_list:
        if driver in sectioned_string:
            return print(driver, "is the winner of that race!")


closest_2024(list_of_2024, index_of_input, refined_text_of_site, drivers_list)




#Alright future me, this is my thought process, for when you have to come back later and hate yourself for everything you've written in this godforesaken program.
# I was thinking that since the length of the race names aren't consistent, but what IS consistent is the length of the year numbers, 2024, (4), it makes it easy
# to find the closest 2024 and move over to the name right next to it. Our issue now is trying to store these indexes with their respective 2024s.


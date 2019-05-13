import requests
from bs4 import BeautifulSoup
import functions

file = open("test.txt","w+")

# Variables
# Urls for the requests
urlListShips = 'https://azurlane.koumakan.jp/List_of_Ships'
baseUrlShips = 'https://azurlane.koumakan.jp'

# Arrays
listTr = []
listUrlShips = []

# Request for the list of ships
r = requests.get(urlListShips)

# Html of the list of ships 
mainPage = BeautifulSoup(r.text, "html.parser")

# Stock in listTr all the tr for Standard ships List
listTr.extend(mainPage.findAll('table')[0].tbody.findAll('tr'))

# Loop on list of tr
for element in listTr :
    # Only for the td elements no th
    if (element.td) :
        # Add the url of the ship to the list
        listUrlShips.append(baseUrlShips + element.find('a').get('href'))

# Loop for each ship
for shipUrl in listUrlShips :
    r = requests.get(shipUrl)
    shipPage = BeautifulSoup(r.text, "html.parser")
    # Get name
    shipName = shipPage.find('h1').getText()

    # Get icon
    shipIconUrl = baseUrlShips + shipPage.find('img').get('src')

    # Get construction time
    shipConstructionTime = shipPage.findAll('table')[0].findAll('td')[0].getText()

    # Get id
    shipId = "C" + shipPage.findAll('table')[1].findAll('td')[0].getText()

    # Get nationality
    shipNationalityName = shipPage.findAll('table')[1].findAll('td')[1].getText()
    #TODO On insert set id where nationalityName = nationalityName in nationality Table

    # Get type ship
    shipType = shipPage.findAll('table')[1].findAll('td')[2].getText()
    #TODO On insert set id where typeName = typeName in typeShip Table

    # Get skins
    listSkins = shipPage.find('div', attrs={"class": u"shiparttabbernew"}).findAll('div', attrs={"class": u"tabbertab"})
    for skin in listSkins :
        # Skin name
        skinName = skin.get('title')

        # Skin img url
        skinUrl = baseUrlShips + skin.find('img').get('src')

    # Get stats
    tabStats = shipPage.find('div', attrs={"style": u"padding-top:7px"}).findAll('div', attrs={"class": u"tabbertab"})

    for tab in tabStats :
        # Get name tab
        tabName = tab.get('title').strip()

        if tabName == 'Level 120 Retrofit':
            listTd = tab.find('table').findAll('td')
            functions.getStatsShip(listTd)
        elif tabName == 'Level 120':
            listTd = tab.find('table').findAll('td')
            functions.getStatsShip(listTd)

    # Get Skills
    # file.write("%s\n" % shipName.encode('utf-8'))

    tableSkillsTh = shipPage.find('table', attrs={"class": u"mw-collapsible"}).findAll('th')
    tableSkillsTd = shipPage.find('table', attrs={"class": u"mw-collapsible"}).findAll('td')

    # Skill 1
    skillName1 = tableSkillsTh[3].getText()
    skillDescription1 = tableSkillsTd[1].getText()
    if len(skillName1) > 3:
        # file.write("Skill description 1 : %s\n" % skillDescription1.encode('utf-8'))
        # Skill 2
        skillName2 = tableSkillsTh[5].getText()
        skillDescription2 = tableSkillsTd[3].getText()
        if len(skillName2) > 3 :
            # file.write("Skill description 2 : %s\n" % skillDescription2.encode('utf-8'))
            # Skill 3
            skillName3 = tableSkillsTh[7].getText()
            skillDescription3 = tableSkillsTd[5].getText()
            if len(skillName3) > 3 :
                a = 'a'
                # file.write("Skill description 3 : %s\n" % skillDescription3.encode('utf-8'))

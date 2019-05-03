import requests
from bs4 import BeautifulSoup

file = open("test.txt","w+")

# Variables
# Urls for the requests
urlListShips = 'https://azurlane.koumakan.jp/List_of_Ships'
baseUrlShips = 'https://azurlane.koumakan.jp'
# Arrays
listTr = []
listUrlShips = []
# Dictionnary for the rarity
rarityDictionnary = {
    "Rarity Normal.png": "Normal",
    "Rare.png": "Rare",
    "Elite.png": "Elite",
    "SuperRare.png": "Super Rare",
    "Unreleased.png": "Unreleased",
    "Priority.png": "Priority",
    "Decisive.png": "Decisive"
}

# Request for the list of ships
r = requests.get(urlListShips)

# Html of the list of ships 
mainPage = BeautifulSoup(r.text, "html.parser")

# Stock in listTr all the tr for Collab ships List
listTr.extend(mainPage.findAll('table')[2].tbody.findAll('tr'))

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
    #file.write("%s\r\n" % name.encode('utf-8'))

    # Get icon
    shipIconUrl = baseUrlShips + shipPage.find('img').get('src')

    # Get construction time
    shipConstructionTime = shipPage.findAll('table')[0].findAll('td')[0].getText()

    # Get rarity
    shipRarityName = rarityDictionnary[shipPage.findAll('table')[0].find('img').get('alt')]
    #TODO On insert set id where rarityName = rarityName in rarity Table

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
        tabName = tab.get('title')

        listTd = tab.find('table').findAll('td')

        # Get hp
        shipHp = listTd[0].getText()

        # Get armor
        shipArmor = listTd[1].getText()

        # Get reload
        shipReload = listTd[2].getText()

        # Get luck
        shipLuck = listTd[3].getText()

        # Get firepower
        shipFirepower = listTd[4].getText()

        # Get torpedo
        shipTorpedo = listTd[5].getText()

        # Get evasion
        shipEvasion = listTd[6].getText()

        # Get speed
        shipSpeed = listTd[7].getText()

        # Get anti-air
        shipAntiAir = listTd[8].getText()

        # Get aviation
        shipAviation = listTd[9].getText()

        # Get oil consumption
        shipOilConsumption = listTd[10].getText()

        # Get accuracy
        shipAccuracy = listTd[11].getText()

        # Get anti-submarine
        shipAntiSubmarine = listTd[12].getText()

    # Get equipment
    tableEquipmentTd = shipPage.find('div', attrs={"style": u"text-align:center;"}).find('table').findAll('td')

    # Equipment 1 efficiency
    equipment1Efficiency = tableEquipmentTd[1].getText()

    # Equipment 1 type
    equipment1Type = tableEquipmentTd[2].getText()

    # Equipment 2 efficiency
    equipment2Efficiency = tableEquipmentTd[4].getText()

    # Equipment 2 type
    equipment2Type = tableEquipmentTd[5].getText()

    # Equipment 3 efficiency
    equipment3Efficiency = tableEquipmentTd[7].getText()

    # Equipment 3 type
    equipment3Type = tableEquipmentTd[8].getText()

    # Get Skills
    # file.write("%s\n" % shipName)

    tableSkillsTh = shipPage.find('table', attrs={"class": u"mw-collapsible"}).findAll('th')
    tableSkillsTd = shipPage.find('table', attrs={"class": u"mw-collapsible"}).findAll('td')

    # Skill 1
    skillName1 = tableSkillsTh[3].getText()
    skillDescription1 = tableSkillsTd[1].getText()
    if len(skillName1) > 3 :
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
                # file.write("Skill description 3 : %s\n" % skillDescription3.encode('utf-8'))

    # TODO Get Construction / Drops

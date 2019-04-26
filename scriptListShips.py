import requests
from bs4 import BeautifulSoup

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

# Stock in listTr all the tr for Standard List, Prototype List, Collab ships List
listTr.extend(mainPage.findAll('table')[0].tbody.findAll('tr'))
listTr.extend(mainPage.findAll('table')[1].tbody.findAll('tr'))
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
    name = shipPage.find('h1').getText()
    # Get icon
    urlIcon = baseUrlShips + shipPage.find('img').get('src')
    # Get construction time
    shipPage.findAll('table')[0].findAll('td')[0].getText()
    # Get rarity
    rarityDictionnary[shipPage.findAll('table')[0].find('img').get('alt')]
    # Get id
    shipPage.findAll('table')[1].findAll('td')[0].getText()
    # Get nationality
    shipPage.findAll('table')[1].findAll('td')[1].getText()
    # Get type ship
    shipPage.findAll('table')[1].findAll('td')[2].getText()
    # Get skins
    listSkins = shipPage.find('div', attrs={"class": u"shiparttabbernew"}).findAll('div', attrs={"class": u"tabbertab"})
    for skin in listSkins :
        # Skin name
        skin.get('title')
        # Skin img url
        skinUrl = baseUrlShips + skin.find('img').get('src')
    # Get stats
    tabStats = shipPage.find('div', attrs={"style": u"padding-top:7px"}).findAll('div', attrs={"class": u"tabbertab"})
    for tab in tabStats :
        # Get name tab
        tab.get('title')
        listTd = tab.find('table').findAll('td')
        # Get hp
        listTd[0].getText()
        # Get armor
        listTd[1].getText()
        # Get reload
        listTd[2].getText()
        # Get luck
        listTd[3].getText()
        # Get firepower
        listTd[4].getText()
        # Get torpedo
        listTd[5].getText()
        # Get evasion
        listTd[6].getText()
        # Get speed
        listTd[7].getText()
        # Get anti-air
        listTd[7].getText()
        # Get aviation
        listTd[8].getText()
        # Get oil consumption
        listTd[9].getText()
        # Get accuracy
        listTd[10].getText()
        # Get anti-submarine
        listTd[11].getText()

    # Get equipment
    tableEquipmentTd = shipPage.find('div', attrs={"style": u"text-align:center;"}).find('table').findAll('td')
    # Equipment 1 efficiency
    tableEquipmentTd[1].getText()
    # Equipment 1 type
    tableEquipmentTd[2].getText()
    # Equipment 2 efficiency
    tableEquipmentTd[4].getText()
    # Equipment 2 type
    tableEquipmentTd[5].getText()
    # Equipment 3 efficiency
    tableEquipmentTd[7].getText()
    # Equipment 3 type
    tableEquipmentTd[8].getText()
    #break
    #TODO Get skills & Get Construction / Drops

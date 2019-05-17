import requests
from bs4 import BeautifulSoup
import myconstants

def getMainPageListShips():
    # Request for the list of ships
    r = requests.get(myconstants.urlListShips)

    # Html of the list of ships 
    return BeautifulSoup(r.text, "html.parser")

def getTrStandardShips(mainPage):
    return mainPage.findAll('table')[0].tbody.findAll('tr')

def getTrPrototypeShips(mainPage):
    return mainPage.findAll('table')[1].tbody.findAll('tr')

def getTrCollabShips(mainPage):
    return mainPage.findAll('table')[2].tbody.findAll('tr')

def getShipUrl(element):
    return myconstants.baseUrlShips + element.find('a').get('href')

def getShipPage(shipUrl):
    # Request for the ship url
    r = requests.get(shipUrl)

    # Html of the ship
    return BeautifulSoup(r.text, "html.parser")

def getShipName(shipPage):
    return shipPage.find('h1').getText().strip()

def getShipIcon(shipPage):
    return myconstants.baseUrlShips + shipPage.find('img').get('src')

def getShipConstructionTime(shipPage):
    return shipPage.findAll('table')[0].findAll('td')[0].getText().strip()

def getShipId(shipPage):
    return shipPage.findAll('table')[1].findAll('td')[0].getText().strip()

def getShipIdCollab(shipPage):
    return "C" + shipPage.findAll('table')[1].findAll('td')[0].getText().strip()

def getShipNationality(shipPage):
    return shipPage.findAll('table')[1].findAll('td')[1].getText().strip()

def getShipType(shipPage):
    return shipPage.findAll('table')[1].findAll('td')[2].getText().strip()

def getShipSkins(shipPage):
    return shipPage.find('div', attrs={"class": u"shiparttabbernew"}).findAll('div', attrs={"class": u"tabbertab"})

def getSkinName(skin):
    return skin.get('title')

def getSkinUrl(skin):
    return myconstants.baseUrlShips + skin.find('img').get('src')

def getTabsStats(shipPage):
    return shipPage.find('div', attrs={"style": u"padding-top:7px"}).findAll('div', attrs={"class": u"tabbertab"})

def getTabName(tab):
    return tab.get('title').strip()

def getTabTd(tab):
    return tab.find('table').findAll('td')

def getStatsShip(listTd):
    # Get hp
    shipHp = listTd[0].getText().strip()
    
    # Get armor
    shipArmor = listTd[1].getText().strip()

    # Get reload
    shipReload = listTd[2].getText().strip()

    # Get luck
    shipLuck = listTd[3].getText().strip()

    # Get firepower
    shipFirepower = listTd[4].getText().strip()

    # Get torpedo
    shipTorpedo = listTd[5].getText().strip()

    # Get evasion
    shipEvasion = listTd[6].getText().strip()

    # Get speed
    shipSpeed = listTd[7].getText().strip()

    # Get anti-air
    shipAntiAir = listTd[8].getText().strip()

    # Get aviation
    shipAviation = listTd[9].getText().strip()

    # Get oil consumption
    shipOilConsumption = listTd[10].getText().strip()

    # Get accuracy
    shipAccuracy = listTd[11].getText().strip()

    # Get anti-submarine
    shipAntiSubmarine = listTd[12].getText().strip()

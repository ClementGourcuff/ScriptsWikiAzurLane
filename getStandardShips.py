import functions
import myconstants

# Arrays
listTr = []
listUrlShips = []

# Get main page list ships
mainPage = functions.getMainPageListShips()

# Stock in listTr all the tr for Prototype ships List
listTr.extend(functions.getTrStandardShips(mainPage))

# Loop on list of tr
for element in listTr :
    # Only for the td elements no th
    if (element.td) :
        # Add the url of the ship to the list
        listUrlShips.append(functions.getShipUrl(element))

# Loop for each ship
for shipUrl in listUrlShips :
    # Get ship page
    shipPage = functions.getShipPage(shipUrl)

    # Get ship name
    shipName = functions.getShipName(shipPage)

    # Get ship icon
    shipIconUrl = functions.getShipIcon(shipPage)

    # Get ship construction time
    shipConstructionTime = functions.getShipConstructionTime(shipPage)

    # Get ship id
    shipId = functions.getShipId(shipPage)

    # Get ship nationality
    shipNationalityName = functions.getShipNationality(shipPage)
    #TODO On insert set id where nationalityName = nationalityName in nationality Table

    # Get type ship
    shipType = functions.getShipType(shipPage)
    #TODO On insert set id where typeName = typeName in typeShip Table

    # Get skins
    listSkins = functions.getShipSkins(shipPage)
    for skin in listSkins :
        # Skin name
        skinName = functions.getSkinName(skin)
        
        # Skin img url
        skinUrl = functions.getSkinUrl(skin)

    # Get stats
    tabStats = functions.getTabsStats(shipPage)
    for tab in tabStats :
        # Get name tab
        tabName = functions.getTabName(tab)

        if tabName == 'Level 120 Retrofit':
            listTd = functions.getTabTd(tab)
            functions.getStatsShip(listTd)
        elif tabName == 'Level 120':
            listTd = functions.getTabTd(tab)
            functions.getStatsShip(listTd)

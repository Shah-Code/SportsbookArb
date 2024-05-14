import pandas as pd
import json
import shin
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

version = "123.0.6312.105"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = '/Users/peanut/Testing/Live-Sports-Arbitrage-Bet-Finder/chromeTesting.app'


driver = webdriver.Chrome(options = chrome_options)

driver.get("https://api.prizepicks.com/projections")

idToplayer = {}
fantasy = {}

#Hitting Stats
baseHRBI = {}
demonHRBI = {}
baseTB = {}
demonTB = {}
baseHSO = {}
demonHSO = {}
baseW = {}
baseR = {}
#Pitching Stats
baseSO = {}
demonSO = {}
baseHA = {}
demonHA = {}
basePO = {}
demonPO = {}
#1st Inning
baseNRF = {}

demonS = {}
demonHR = {}
demonSB = {}
demonWA = {}


#Basketball
basePts = {}
basePRA = {}
baseReb = {}
baseA = {}
base3 = {}
basePR = {}
basePA = {}
baseRA = {}
baseBlks = {}
baseStls = {}
baseBS = {}
baseTO = {}

pp = driver.page_source
soup = BeautifulSoup(pp, "html.parser")
data = json.loads(soup.pre.text)
for item in data['included']:
    idToplayer[item["id"]] = item["attributes"]["name"]
for projection in data['data']:
    player = idToplayer[projection['relationships']['new_player']['data']['id']]
    if projection['attributes']['odds_type'] == "demon":
        if (projection['attributes']['stat_type'] == "Hits+Runs+RBIs"):
            demonHRBI[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Pitcher Strikeouts"):
            demonSO[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Total Bases"):
            demonTB[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Hits Allowed"):
            demonHA[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Pitching Outs"):
            demonPO[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Hitter Strikeouts"):
            demonHSO[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Singles"):
            demonS[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Home Runs"):
            demonHR[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Stolen Bases"):
            demonSB[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Walks Allowed"):
            demonWA[player] = float(projection['attributes']['line_score'])
    if projection['attributes']['odds_type'] == "standard":
        if (projection['attributes']['stat_type'] == "Hitter Fantasy Score"):
            fantasy[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Hits+Runs+RBIs"):
            baseHRBI[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Pitcher Strikeouts"):
            baseSO[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Total Bases"):
            baseTB[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "1st Inning Runs Allowed"):
            baseNRF[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Hits Allowed"):
            baseHA[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Pitching Outs"):
            basePO[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Hitter Strikeouts"):
            baseHSO[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Walks"):
            baseW[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Runs"):
            baseR[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Pts+Rebs+Asts"):
            basePRA[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Points"):
            basePts[player] = float(projection['attributes']['line_score']) 
        if (projection['attributes']['stat_type'] == "Pts+Asts"):
            basePA[player] = float(projection['attributes']['line_score']) 
        if (projection['attributes']['stat_type'] == "Pts+Rebs"):
            basePR[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Rebs+Asts"):
            baseRA[player] = float(projection['attributes']['line_score']) 
        if (projection['attributes']['stat_type'] == "Rebounds"):
            baseReb[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Assists"):
            baseA[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Steals"):
            baseStls[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Blocked Shots"):
            baseBlks[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Blks+Stls"):
            baseBS[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "Turnovers"):
            baseTO[player] = float(projection['attributes']['line_score'])
        if (projection['attributes']['stat_type'] == "3-PT Made"):
            base3[player] = float(projection['attributes']['line_score'])      
driver.implicitly_wait(10)

ppHdf = pd.DataFrame([baseHRBI, baseTB, baseHSO]).T.reset_index()
ppPdf = pd.DataFrame([baseSO, baseHA, basePO, baseNRF]).T.reset_index()
ppHdf.columns = ['Hitter', 'HRBI', 'TB', 'HSO']
ppPdf.columns = ['Pitcher', 'SO', 'HA', 'PO', 'NRF']

driver.get("https://sportsbook.draftkings.com/leagues/basketball/nba?category=player-points&subcategory=points")
#Hitting Stats
dkH = {}
dkHRBI = {}
dkTB = {}
dkHSO = {}
dkW = {}
dkR = {}
dkD = {}
#Pitching Stats
dkSO = {}
dkHA = {}
dkPO = {}
#1st Inning
dkNRF = {}

dkS = {}
dkHR = {}
dkSB = {}
dkWA = {}

#Basketball
dkPts = {}
dkPRA = {}
dkReb = {}
dkA = {}
dk3 = {}
dkPR = {}
dkPA = {}
dkRA = {}
dkBlks = {}
dkStls = {}
dkBS = {}
dkTO = {}

driver.implicitly_wait(5)

def convert(over, under):
    o = int(over[1:])
    u = int(under[1:])
    scale = u / o
    do = 0
    du = 0
    if (over[0] == '−'):
        do = ((100/o) + 1)
    else:
        do = ((o/100) + 1)
    if (under[0] == '−'):
        du = ((100/u) + 1)
    else:
        du = ((u/100) + 1)
    return shin.calculate_implied_probabilities([do, du])   

def statClick(stat):
    btn = driver.find_element(By.ID, stat)
    driver.execute_script("arguments[0].click();",btn)
    driver.implicitly_wait(10)

def getData(stat, xp):
    dk = globals()["dk" + stat]
    lines = driver.find_elements(By.XPATH, xp)
    for pline in lines:
        player_name = pline.find_element(By.CLASS_NAME, 'sportsbook-row-name').text
        line = pline.find_element(By.CLASS_NAME, "sportsbook-outcome-cell__line").text
        if (len(line) == 0):
            continue
        line = float(line)
        ou = pline.find_elements(By.CLASS_NAME, 'american')
        if (len(ou) == 2):
            realou = convert(ou[0].text, ou[1].text)
            dk[player_name] = (line, realou[0], realou[1])
    driver.implicitly_wait(5)

getData('Pts', '//tbody[@class="sportsbook-table__body"]/tr')

statClick("game_category_Player Threes")

getData('3', '//div[@aria-labelledby="game_category_Player Threes"]//tbody[@class="sportsbook-table__body"]/tr')

statClick("game_category_Player Combos")

getData('PRA', '//div[@aria-labelledby="game_category_Player Combos"]//tbody[@class="sportsbook-table__body"]/tr')

statClick("subcategory_Pts + Reb")

getData('PR', '//div[@aria-labelledby="game_category_Player Combos"]//tbody[@class="sportsbook-table__body"]/tr')

statClick('subcategory_Pts + Ast')

getData('PA', '//div[@aria-labelledby="game_category_Player Combos"]//tbody[@class="sportsbook-table__body"]/tr')

statClick('subcategory_Ast + Reb')

getData('RA', '//div[@aria-labelledby="game_category_Player Combos"]//tbody[@class="sportsbook-table__body"]/tr')

statClick('game_category_Player Rebounds')

getData('Reb', '//div[@aria-labelledby="game_category_Player Rebounds"]//tbody[@class="sportsbook-table__body"]/tr')

statClick('game_category_Player Assists')

getData('A', '//div[@aria-labelledby="game_category_Player Assists"]//tbody[@class="sportsbook-table__body"]/tr')

statClick('game_category_Player Defense')

getData('Stls', '//div[@aria-labelledby="game_category_Player Defense"]//tbody[@class="sportsbook-table__body"]/tr')

statClick('subcategory_Blocks')

getData('Blks', '//div[@aria-labelledby="game_category_Player Defense"]//tbody[@class="sportsbook-table__body"]/tr')

statClick('subcategory_Steals + Blocks')

getData('BS', '//div[@aria-labelledby="game_category_Player Defense"]//tbody[@class="sportsbook-table__body"]/tr')

statClick('subcategory_Turnovers')

getData('TO', '//div[@aria-labelledby="game_category_Player Defense"]//tbody[@class="sportsbook-table__body"]/tr')

driver.implicitly_wait(15)

driver.get("https://sportsbook.draftkings.com/leagues/baseball/mlb?category=batter-props&subcategory=home-runs")

driver.implicitly_wait(15)

getData('HR', '//tbody[@class="sportsbook-table__body"]/tr')

statClick("subcategory_Total Bases")
    
getData('TB', '//tbody[@class="sportsbook-table__body"]/tr')

statClick("subcategory_Runs Scored")

getData('R', '//tbody[@class="sportsbook-table__body"]/tr')

statClick("subcategory_Hits + Runs + RBIs")

getData('HRBI', '//tbody[@class="sportsbook-table__body"]/tr')

statClick("subcategory_Stolen Bases")

getData('SB', '//tbody[@class="sportsbook-table__body"]/tr')

statClick("subcategory_Strikeouts")

getData('HSO', '//tbody[@class="sportsbook-table__body"]/tr')

statClick("subcategory_Singles")

getData('S', '//tbody[@class="sportsbook-table__body"]/tr')

statClick('subcategory_Doubles')

getData('D', '//tbody[@class="sportsbook-table__body"]/tr')

statClick("subcategory_Walks")

getData('W', '//tbody[@class="sportsbook-table__body"]/tr')

statClick("game_category_Pitcher Props")

driver.implicitly_wait(5)

statClick("subcategory_Strikeouts Thrown")

getData('SO', '//div[@aria-labelledby="game_category_Pitcher Props"]//tbody[@class="sportsbook-table__body"]/tr')

statClick("subcategory_Outs Recorded")

getData('PO', '//div[@aria-labelledby="game_category_Pitcher Props"]//tbody[@class="sportsbook-table__body"]/tr')

statClick("subcategory_Hits Allowed")

getData('HA', '//div[@aria-labelledby="game_category_Pitcher Props"]//tbody[@class="sportsbook-table__body"]/tr')

statClick("subcategory_Walks Allowed")

getData('WA', '//div[@aria-labelledby="game_category_Pitcher Props"]//tbody[@class="sportsbook-table__body"]/tr')

driver.quit()

def FantasyScore(player):
    return dkHR[player] * 10 + dkS[player] * 3 + dkD[player] * 5 + ((dkR[player] - dkHR[player]) * 2) 

def potential(stat):
    base = globals()["base" + stat]
    dk = globals()["dk" + stat]

    print("\n" + stat + "\n")
    for player in base.keys():
        if player in dk.keys():
            if (dk[player][0] == base[player]):
                if (dk[player][1] >= 0.553 or dk[player][2] >= 0.553):
                    print(f"***{player} :: {dk[player][1]} | {dk[player][2]}***")
                elif (dk[player][1] >= 0.535 or dk[player][2] >= 0.535):
                    print(f"{player} :: {dk[player][1]} | {dk[player][2]} ")

def dPotential(stat):
    demon = globals()["demon" + stat]
    dk = globals()["dk" + stat]

    print("\n Demon " + stat + "\n")
    for player in demon.keys():
        if player in dk.keys():
            if (dk[player][0] == demon[player]):
                if (dk[player][1] >= 0.45):
                    print(f"{player} :: {dk[player][1]} | {dk[player][2]} ")     

potential("TB")
potential("R")
potential("W")
potential("HRBI")
potential("HSO")
potential("SO")
potential("PO")
potential("HA")
potential('Pts')
potential('PRA')
potential('Reb')
potential('A')
potential('3')
potential('PR')
potential('PA')
potential('RA')
potential('Blks')
potential('Stls')
potential('BS')
potential('TO')

dPotential("S")
dPotential("HR")
dPotential("SB")
dPotential("SO")
dPotential("PO")
dPotential("HA")
dPotential("WA")
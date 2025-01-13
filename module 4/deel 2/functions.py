import time
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HORSE_COPPER_PER_DAY, COST_FOOD_HUMAN_COPPER_PER_DAY

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return float(amount / 10)

def silver2gold(amount:int) -> float:
    return float(amount / 5)

def copper2gold(amount:int) -> float:
    return float(amount / 50)

def platinum2gold(amount:int) -> float:
    return 25 * amount

def getPersonCashInGold(personCash: dict) -> float:
    total_gold = 0.0
    if "copper" in personCash:
        total_gold += copper2gold(personCash["copper"])
    if "silver" in personCash:
        total_gold += silver2gold(personCash["silver"])
    if "gold" in personCash:
        total_gold += personCash["gold"] 
    if "platinum" in personCash:
        total_gold += platinum2gold(personCash["platinum"])
    return total_gold

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    total_copper_cost = (people * COST_FOOD_HUMAN_COPPER_PER_DAY * JOURNEY_IN_DAYS) + (horses * COST_FOOD_HORSE_COPPER_PER_DAY * JOURNEY_IN_DAYS)
    total_gold_cost = copper2gold(total_copper_cost)

    return total_gold_cost

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    lijst = []
    for item in list:
        if item.get(key) == value:
            lijst.append(item)
    return lijst

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True) 

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True) 

def getAdventuringFriends(friends:list) -> list:
    adventuring_people = getAdventuringPeople(friends)
    return getShareWithFriends(adventuring_people)

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    pass

def getNumberOfTentsNeeded(people:int) -> int:
    pass

def getTotalRentalCost(horses:int, tents:int) -> float:
    pass

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()
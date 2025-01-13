import time
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HORSE_COPPER_PER_DAY, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_TENT_GOLD_PER_WEEK, COST_HORSE_SILVER_PER_DAY

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
    horses = people // 2
    if people % 2 > 0:
        horses += 1
    return horses

def getNumberOfTentsNeeded(people:int) -> int:
    tents = people // 3
    if people % 3 > 0:
        tents += 1
    return tents

def getTotalRentalCost(horses:int, tents:int) -> float:
    weeks = JOURNEY_IN_DAYS // 7
    if JOURNEY_IN_DAYS & 7 > 0:
        weeks += 1

    tent_cost_in_gold = tents * COST_TENT_GOLD_PER_WEEK * weeks
    horse_cost_in_silver = horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS

    horse_cost_in_gold = horse_cost_in_silver / 5  # Convert silver to gold
    total_cost_in_gold = tent_cost_in_gold + horse_cost_in_gold

    return total_cost_in_gold

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    lijst = []
    for item in items:
        amount = item['amount']
        unit = item['unit']
        name = item['name']
        lijst.append(f"{amount}{unit} {name}".strip())

    if len(lijst) == 0:
        return ""
    elif len(lijst) == 1:
        return lijst[0]
    else:
        laatste_item = lijst.pop()
        return ", ".join(lijst) + " & " + laatste_item

def getItemsValueInGold(items:list) -> float:
    total_value_in_gold = 0.0
    for item in items:
        amount = item['amount']
        price_amount = item['price']['amount']
        price_type = item['price']['type']

        # Convert the price to gold
        if price_type == "copper":
            value_in_gold = copper2gold(price_amount)
        elif price_type == "silver":
            value_in_gold = silver2gold(price_amount)
        elif price_type == "gold":
            value_in_gold = price_amount
        elif price_type == "platinum":
            value_in_gold = platinum2gold(price_amount)

        total_value_in_gold += value_in_gold * amount

    return total_value_in_gold

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
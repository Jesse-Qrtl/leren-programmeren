import time
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HORSE_COPPER_PER_DAY, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_TENT_GOLD_PER_WEEK, COST_HORSE_SILVER_PER_DAY,COST_INN_HUMAN_SILVER_PER_NIGHT,COST_INN_HORSE_COPPER_PER_NIGHT
from math import ceil

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
    return ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    weeks = ceil(JOURNEY_IN_DAYS / 7)

    tent_cost_in_gold = tents * COST_TENT_GOLD_PER_WEEK * weeks
    horse_cost_in_silver = horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS

    horse_cost_in_gold = silver2gold(horse_cost_in_silver)
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
    total_gold = 0.0
    for person in people:
        amount_gold = getPersonCashInGold(person['cash'])
        total_gold += round(amount_gold,2)
    return total_gold

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    lijst = []
    for investor in investors:
        if investor['profitReturn'] < 10:
            lijst.append(investor)
    return lijst

def getAdventuringInvestors(investors:list) -> list:
    lijst = []
    for investor in investors:
        if investor['adventuring']:
            if investor['profitReturn'] < 10:
                lijst.append(investor)
    return lijst

def getTotalInvestorsCosts(investors: list, gear: list) -> float:
    amount_investors = len(getInterestingInvestors(getAdventuringInvestors(investors)))
    amount_gear = len(gear)
    tents = amount_investors
    horses = amount_investors

    if amount_investors == 0:
        return 0.0
    if amount_gear == 0:
        return 0.0
    
    rental_cost_in_gold = getTotalRentalCost(horses, tents)
    gear_cost_in_gold = getItemsValueInGold(gear) * amount_investors
    food_cost_in_gold = getJourneyFoodCostsInGold(amount_investors, horses)

    total_cost_in_gold = rental_cost_in_gold + gear_cost_in_gold + food_cost_in_gold

    return total_cost_in_gold

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    total_cost_inn = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT * people) + copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT * horses)
    max_amount_in_inn = leftoverGold // total_cost_inn
    
    return int(max_amount_in_inn)

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    cost_human_inn_in_gold = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT * people)
    cost_horse_inn_in_gold = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT * horses)

    total_cost_in_gold = round(nightsInInn * (cost_human_inn_in_gold + cost_horse_inn_in_gold), 2)
    
    return total_cost_in_gold
##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    lijst = []
    amount_investors = getInterestingInvestors(investors)

    for investor in amount_investors:
        cut_investor_in_gold = round(profitGold * (float(investor['profitReturn']) / 100.0), 2)
        lijst.append(cut_investor_in_gold)

    return lijst

def getAdventurerCut(profitGold: float, investorsCuts: list, fellowship: int) -> float:
    for cut in investorsCuts:
        profitGold -= float(cut)

    if fellowship > 0:
        adventurer_cut_each = round(profitGold / fellowship, 2)
        if adventurer_cut_each > 0:
            return adventurer_cut_each
    return 0.0

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
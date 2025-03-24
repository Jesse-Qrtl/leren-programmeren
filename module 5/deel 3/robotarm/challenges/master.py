from challenges.solutions import *
from random import randint, shuffle

allcolors = 'rgbypownl'
def rngclist(c,l):
    cs = list(c)
    shuffle(cs)
    return [cs[x] for x in range(l)]

challenges = {
    1 : {
        'name':'grab the color that is different',
        'start' : 'x,x,x,x,x,x,x,x,x,x', 
        'symbols': (lambda c: 'x-'+(c[0]*9)+c[1] )(rngclist(allcolors, 2))
    },
    2 : {
        'name':'at the left order from most to lowest',
        'start' : ',,,,x,x,x,x,x,x', 
        'symbols': (lambda c: 'x-'+(c[0]*3)+(c[1]*2)+c[2] )(rngclist(allcolors, 3))
    },
    3 : {
        'name':'sort the colors on the outside, 2 on each side',
        'start' : ',,,xxxx,xxxx,xxxx,xxxx', 
        'symbols': (lambda c: 'x-'+(''.join(c)*4))(rngclist(allcolors, 4))
    },
    4 : {
        'name':'create two the same stacks',
        'start' : 'xxxx,,,,,,y,y,y,y',
        'symbols': (lambda c: 'y-'+''.join(c)+',x-'+''.join(c) )(rngclist(allcolors, 4)) 
    },
    5 : {
        'name':'stack the double color',
        'start' : 'x,x,x,x,x,x,x,x,x,x', 
        'symbols': (lambda c: 'x-'+c+c[randint(0,len(c)-1)] )(allcolors)
    },
}
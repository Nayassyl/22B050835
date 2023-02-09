def solve( numheads, numlegs):
    chickens = 2 * numheads - numlegs / 2
    rabbits = numheads - chickens
    print( chickens, rabbits )
hd = int(input())
lg = int(input())
solve( hd, lg )

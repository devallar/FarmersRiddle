##Copyright 2020 Duval Weerakoone | The Nescius##

# The Farmer's Problem
# A Farmer goes to the market with $100 to spend. Cows cost $10/each, Pigs cost $3/each and sheep cost $0.5/each
# The farmer buys from the cattle dealer, pig dealer and the sheep dealer. She spends exactly $100 and returns with 100 animals.

#How many of each animal did he buy


## This is an example of Diophantic Equations, in mathematics there's a couple of ways to solve them, but since we have the horse power
## I went ahead and did recursive computing to solve the PROBLEM

prob = """     ********* THE FARMER'S PROBLEM **********

A Farmer goes to the market with $100 to spend.

Cows cost $10/each,
Pigs cost $3/each and
sheep cost $0.5/each

The farmer buys from the cattle dealer, pig dealer and the sheep dealer. She spends exactly $100 and returns with 100 animals.

How many of each animal did he buy?
"""
print(prob)

#Core variables
cash = 100

#Price of the Animals
pCow = 10
pPig = 3
pSheep = 0.5

# Starting Quantity of the Animals | Set to 0 for Zero type options
qCow = 1
qPig = 1
qSheep = 1

qTotal = 0

quantityCheck = False
priceCheck = False

#The checking function which evaluates whether its an option
def results():
    cash = (qCow *pCow) +(qPig * pPig) + (qSheep *pSheep)
    qTotal = qSheep + qPig + qCow

    if qTotal == 100 and cash == 100:
        priceCheck = True
        quantityCheck = True
        print("Cows: " + str(qCow) + "  |  Pigs: " + str(qPig) + "  |  Sheep: " + str(qSheep) + "    |   Quantity: " +str(quantityCheck)+ "    |   Price: " +str(priceCheck))

## This is the recursive section
while qCow <100 :
    while qPig < 100:
        while qSheep < 100 :
            qSheep += 1
            results()
        qPig +=1
        qSheep = 0
    qCow += 1
    qPig = 0

## Termination Screen
if quantityCheck == False and priceCheck == False:
    print("""
    *****************************************
           There are no more solutions
    *****************************************

    """)

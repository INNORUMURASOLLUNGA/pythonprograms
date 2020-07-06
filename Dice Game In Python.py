import random

a=''' _______\n|       |\n|   .   |\n|       |\n|_______|'''



b=''' _______\n|   .   |\n|       |\n|   .   |\n|_______|'''


  
c=''' _______\n|.      |\n|   .   |\n|      .|\n|_______|'''



d=''' _______\n|.     .|\n|       |\n|.     .|\n|_______|'''


 
e=''' _______\n|.     .|\n|   .   |\n|.     .|\n|_______|''' 



f=''' _______\n|.     .|\n|.     .|\n|.     .|\n|_______|''' 





lis=[a,b,c,d,e,f]


print('''{0} ____  ___  ____  ____        ____    ____    _    _    ____ 
{0}|    |  |  |     |           |       |    |  | \  / |  |
{0}|    |  |  |     |----       |  --|  |----|  |  \/  |  |----
{0}|____| _|_ |____ |____       |____|  |    |  |      |  |____'''.format("                               "))
print("{0}---------------***********************************************-----------------".format("                      "))
print ('''{0} _______    _______    _______    _______    _______    _______
{0}|       |  |   .   |  |.      |  |.     .|  |.     .|  |.     .|
{0}|   .   |  |       |  |   .   |  |       |  |   .   |  |.     .|
{0}|       |  |   .   |  |      .|  |.     .|  |.     .|  |.     .|
{0}|_______|  |_______|  |_______|  |_______|  |_______|  |_______|'''.format("                               "))
print("{0}---------------***********************************************-----------------".format("                      "))
  
turn=int(input("Enter how many times the dice to be rolled: "))
score =0
chturn=0
while(turn>chturn):
    n=int(input("Enter the no what the dice will rolled now: "))
    s=random.choice(lis)
    chturn=chturn+1
    print(s)
    if n==(lis.index(s)+1):
        print("******Hurry you are correct*******")
        print("\n")
        score=score+1
    else:
        print("******Oops! It is not correct Please Try again********")
        print("\n")
print("\n")
print("\n")
print("Your score is {0}".format(score))




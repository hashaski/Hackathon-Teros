#Maratona

#Fibbonacci

qtde = int(input())

nums = [0,1]
num1 = 0
num2 = 1


for i in range(qtde-2):
    num3 = num1 + num2
    nums.append(num3)
    num1 = num2
    num2 = num3

print(*nums)

#Brick Game

linhas = int(input())
captains= []

for i in range(linhas):
    team = list(map(int,input().split()))
    median = len(team)/2
    captain = team[int(median)]
    captains.append(captain)

for j in range(len(captains)):
    print("Case "+str(j+1)+":",captains[j])




#Busca na Internet

link3 = int(input())

link1 = (link3 * 2)*2

print(link1)
    

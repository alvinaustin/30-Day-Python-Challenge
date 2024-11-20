"""
Author:Aron Bobby Daniel
Date:20-11-2024
Python Programme of list
"""

#Creating a list

games=["Cricket","Football","Formula 1","Moto Gp"]
print(games)

#Acessing a list
games=["Cricket","Football","Formula 1","Moto Gp"]
print(games[3])
print(games[-3])

#Modifying a List
games=["Cricket","Football","Formula 1","Moto Gp"]
games[1]="Hockey"
games[0]="Baseball"
games[-2]="Cycling"
print(games)

games=["Cricket","Football","Formula 1","Moto Gp"]
games.append("Baseball")
games.remove("Moto Gp")
print(games)

#Slicing
games=["Cricket","Football","Formula 1","Moto Gp","Baseball","Hockey","Surfing"]
slice=games[1:5]
print(slice)



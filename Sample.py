games={
    "Cricket" : "A bat and a ball game",
    "Football" : "A game played using a ball and feet",
    "Chess" : "A board game played using chess pieces"
}

print("_____ Game Dictionary Menu -----")
print("1. Get Game description")
print("2. Add a new game")
print("3. Change game description")
print("4. Delete a game")

choice= input("Enter your choice (`1/2/3/4)")

if choice == "1":
    game=input("Enter game name:").lower()

    if game in games:
        print("Description:" ,games[game])
    else:
        print("Game Not Found!")

elif choice== "2":
    new_game=input("Enter the new game name:").lower()
    description=input("Enter game description:")

    games[new_game]=description
    print("Game added sucessfully!")
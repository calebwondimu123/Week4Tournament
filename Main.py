#############################################
# Name: Caleb
# Class: ICS3C
# Date: Monday Sept. 20
# Project Name: Week4Tournament
#
# Project Description: See the README file
#############################################

# THIS IS WHERE YOU CODE
# Initialize variables to track the top team
top_team_name = ""
top_points = -1

# Loop to read information for 6 teams
for i in range(6):
    print(f"\nTeam {i + 1}")
    name = input("Enter team name: Irish ")
    wins = int(input("Enter wins: "))
    losses = int(input("Enter losses: "))
    ties = int(input("Enter ties: "))

    # Calculate points using the required formula: Wins * 2 + Ties * 1
    points = (wins * 2) + (ties * 1)

    # Output team stats in the required format
    print(f"Team name: {name}  Wins: {wins}  Ties: {ties}  Losses: {losses}  Points: {points}")

    # Track the team at the top of the standings
    if points > top_points:
        top_points = points
        top_team_name = name

# Print the top team
print("\nTop of the standings:")
print(f"{top_team_name} with {top_points} points!")



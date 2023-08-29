import csv
def calculate_average():
   with open("Prem Data Set.csv" , "r") as p:
        csv_reader = csv.reader(p)
        next(csv_reader)
        for i in csv_reader:
            total_goals = int(i[5]) + int(i[7])
            total_matches = count =+1
            average_goals_per_match = total_goals/ total_matches
            print(f"Average goals per match:{average_goals_per_match:.2f}")


calculate_average()

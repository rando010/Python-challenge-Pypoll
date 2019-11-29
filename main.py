import os
import csv

candidate = ""
voter_id = ""
vote=""
total_votes=""
Correyvote = 0
Khanvote = 0
Livote = 0
OTooleyvote = 0
number_of_votes_cast = 0
file_to_open = "election_data.csv"

with open(file_to_open, 'r') as this_csv_file:
    csv_reader = csv.reader(this_csv_file, delimiter=',')

    # data = [l for l in csv_reader]
    data = list(csv_reader)
    number_of_votes_cast = len(data)

    for line in data:    
        voter_id = line[0]
        vote = line[2]
        if vote =="Correy":
            Correyvote=Correyvote + 1
        elif vote =="Khan":
            Khanvote = Khanvote + 1
        elif vote =="Li":
            Livote = Livote + 1
        elif vote =="O'Tooley": 
            OTooleyvote = OTooleyvote + 1
        correy_percent_of_vote=((Correyvote/number_of_votes_cast)*100)
        khan_percent_of_vote=((Khanvote/number_of_votes_cast)*100)
        li_percent_of_vote=((Livote/number_of_votes_cast)*100)
        otooley_percent_of_vote=((OTooleyvote/number_of_votes_cast)*100)
        correy_percent_of_vote_rounded="{:.3f}%".format(correy_percent_of_vote)        
        khan_percent_of_vote_rounded="{:.3f}%".format(khan_percent_of_vote)
        li_percent_of_vote_rounded="{:.3f}%".format(li_percent_of_vote)
        otooley_percent_of_vote_rounded="{:.3f}%".format(otooley_percent_of_vote)

print("Election Results")
print("-----------------------")
print("Total Votes:",(number_of_votes_cast))
print("-----------------------")  
print("Correy ",(correy_percent_of_vote_rounded),("({})".format(Correyvote)))
print("Khan ",(khan_percent_of_vote_rounded),("({})".format(Khanvote)))
print("Li ",(li_percent_of_vote_rounded),("({})".format(Livote)))
print("O'Tooley ",(otooley_percent_of_vote_rounded),("({})".format(OTooleyvote)))
print("-----------------------") 
if (Correyvote>Khanvote) and (Correyvote>Livote) and (Correyvote>OTooleyvote):
    print("Winner: Correy")
if (Khanvote>Correyvote) and (Khanvote>Livote) and (Khanvote>OTooleyvote):
    print("Winner: Khan")
if (Livote>Correyvote) and (Livote>Khanvote) and (Livote>OTooleyvote):
    print("Winner: Li") 
if (OTooleyvote>Correyvote) and (OTooleyvote>Khanvote) and (OTooleyvote>Livote):
    print("Winner: OTooley")           
output_path = os.path.join("election_results.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-----------------------'])
    csvwriter.writerow(['Total Votes: ', (number_of_votes_cast)])
    csvwriter.writerow(['-----------------------'])
    csvwriter.writerow(['Correy',(correy_percent_of_vote_rounded),(Correyvote)])
    csvwriter.writerow(['Khan',(khan_percent_of_vote_rounded),(Khanvote)])
    csvwriter.writerow(['Li',(li_percent_of_vote_rounded),(Livote)])
    csvwriter.writerow(['OTooley',(otooley_percent_of_vote_rounded),(OTooleyvote)])
    csvwriter.writerow(['-----------------------'])
    if (Correyvote>Khanvote) and (Correyvote>Livote) and (Correyvote>OTooleyvote):
        csvwriter.writerow(['Winner: Correy'])
    if (Khanvote>Correyvote) and (Khanvote>Livote) and (Khanvote>OTooleyvote):
        csvwriter.writerow(['Winner: Khan'])
    if (Livote>Correyvote) and (Livote>Khanvote) and (Livote>OTooleyvote):
        csvwriter.writerow(['Winner: Li'])
    if (OTooleyvote>Correyvote) and (OTooleyvote>Khanvote) and (OTooleyvote>Livote):
        csvwriter.writerow(['Winner: OTooley'])  
    csvwriter.writerow(['-----------------------'])

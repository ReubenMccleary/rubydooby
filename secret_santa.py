import random

family_members = ["Mum", "Dad", "Caleb", "Miah", "Reuben"]
random.shuffle(family_members)
for i in range(5):
	family_members[i].has  = family_members[i+1 % 5]
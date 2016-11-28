#soru maratonu 1
################
all_sums = 0 #butun toplamlarin sayisi 
equal_sums = 0 #esit olanlarin sayisi
#bulmak istedigimiz olasilik: equal sums / all sums

for x in range(10, 100):
	for y in range(10, 100): 
		for a in range(10, 100):
			for b in range(10, 100):
				if x!=y and a!=b:
					all_sums+=1
					if x+y==a+b:
						equal_sums+=1

print equal_sums
print all_sums
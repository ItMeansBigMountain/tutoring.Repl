#scores is a variable
#the variable type is an array[]
#arrays are boxes that hold information
scores = [20,75,23,23,76,54,31,21,11,90,50,68,20,75,98,23,76,14,31,21,11,90,50,68,20,75,99,23,76,54,31,21,11,90,50,4,20,75,98,23,76,54,31,21,11,90,50,68,20,75,98,23,76,100,31,21,11,90,50,68,20,75,98,23,76,54,61,21,11,90,50,68,20,75,98,23,76,54,31,21,11,90,50,68,20,75,98,23,76,54,31,21,11,90,58,68,20,10,98,23,76,54,37,21,11,90,50,68,20,75,98,23,16,54,1,21,11,90,50,68,20,75,98,23,76,54,31,21,11,90,50,68,20,75,98,23,76,54,31,21,11,90,50,68,20,75,98,23,76,34,31,21,11,90,50,68,20,75,98,23,76,54,31,21,11,90,50,68,20,75,98,23,76,54,31,21,11,90,50,68,0,75,98,23,76,54,31,21,11,90,50,68,20,75,98,23,76,54,31,71,11,90,50,68,20,75,98,24,76,54,31,21,11,90,50,68,20,75,98,23,76,54,31,21,11,90,58,68,20,75,98,23,76,54,31,21,11,90,50,68,20,75,98,23,76,54,31,21,11,90,50,68,20,75,36,23,76,54,47,21,91,90,50,68,20,75,98,23,76,54,31,21,11,90,50,68,20,75,98,23,76,54,31,21,11,90,50,68,20,75,74,23,76,54,31,21,11,90,50,68,20,75,98,23,76,54,31,21,11,90,68,20,75,98,23,76,54,31,21,9,90,50,68,20,75,98,23,76,54,31,21,11,90,50,68,20,75,98,23,76,54,31,21,11,90,50,68,20,75,98,59,76,54,31,21,11,90,50,68,20,75,77,23,76,54,31,21,11,90,50,68,20,75,45,23,76,54,31,21,11,90,50,68,20,75,98,0,76,54,31,21,11,90,50,68,20,75,98,23,76,54,31,21,11,90,50,68,20,75,98,23,76,54,31,21,11,90,50,68,20,75,98,23,76,54,31,21,11,90,5,80,98,50,41,83,45 ]




# how many items are in here?
print(  len(scores)  )


# how do i find tenth person who took this test?
print(  scores[400]  )



# i want to see them one by one
print("--------ONE BY ONE---------")
for x in range (0,  len( scores)   ,1):
  print( scores[x]  )
print('-------------------------')



# what is the average score?
total = 0
for x in range(0,  len(scores) , 1 ) :
  total = scores[x] + total

print('total: ',total)
average = total / len(scores) 
print(average)
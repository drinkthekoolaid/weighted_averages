"""
This is a program a professor friend, asked me to try to make. 
It calculates average grades using weighted averages.  

Things to work on:
take user input and append two lists, grades and weights.  

Code works with the given numbers. 

"""
grades = [100, 75.5, 90, 100, 80]
weights = [10, 15, 15, 20, 40]
weighted_totals = []

def weight():          #this is what is making my weighted list
  for m, n in zip(grades, weights):
    m = m / 100
    total = (m * n)
    weighted_totals.append(total)
  return weighted_totals 
  
  # this is where I want to sum all the items in the weighted_totals list together

def final_weights(weighted_totals):
  totalWeights = 0
  for final_mark in weighted_totals:
    totalWeights= totalWeights + final_mark
  return totalWeights
       

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(grades):
    variance = 0
    for number in grades:
        variance += (grades_average(grades) - number) ** 2
    return variance / len(grades)

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)


print ("Marks:")
for grade in grades:
   print (grade)
     
print ("-----------------")  
print ("Sum:", grades_sum(grades))
print ("Average:", grades_average(grades))
print ("Variance:", grades_variance(grades))
print ("Standard Deviation:", grades_std_deviation(variance))
print ("Weighted Marks:", weight())
print ("Final Weighted Average:", final_weights(weighted_totals))
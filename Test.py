# declaring a variable
Name = "My name is Jethro"
# calling a function
Name = Name.swapcase()
print(Name)

def findAverage(dictionary):
    for key in dictionary:
        sumArray = 0
        for i in dictionary[key]:
            sumArray = sumArray + i 
            avg = round(sumArray / len(dictionary[key]), 2)
            print(f'the average score for {key} is{str(avg)}')
dictionary = {
    'Valentine': [10, 10, 10],
    'Romeo' :[2,2,2],
    'Juliet':[2,3,3]
}
findAverage(dictionary)
            
        
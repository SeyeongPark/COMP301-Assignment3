'''
File Name : COMP301-Assignment3
Author's Name : Seyeong Park
Student Number : 301088175
File Description : This is 'payroll.py' file.
                  It keeps a list of employee information for each pay period in a text file called data.txt .
'''


# Print column table form
print("+-----------------+-----------------------+---------------+")
print("| Enployee Number |    Employee Name      | Hourse Worked |")
print("+-----------------+-----------------------+---------------+")

# Open 'data.txt' file, and named it as 'data'
with open('data.txt') as data:   
    # Print each lines of 'data'  
    for line in data:
        # Split 'data'
        line = line.strip().split(',')
        # Print contents of 'data' 
        print('|\t{:8s}  |   {}, {:8s}\t  |\t{}\t  |'.format(*line))
        print("+-----------------+-----------------------+---------------+")

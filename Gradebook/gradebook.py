# gradebook.py

# Display the average of each student's grade.

def display_student_averages(gradebook):
    print('\nStudent Averages:')

    for i in range(len(gradebook)):
        row = gradebook[i]
        row_count = len(row)
        row_sum = sum(row)
        row_average = row_sum / row_count
        print('Student ', i + 1, ': ', format(row_average, '.2f'), sep='')
        
# Display the average for each assignment.

def display_assignment_averages(gradebook):
    print('Assignment Averages:')

    for i in range(len(gradebook[0])):
        column = [row[i] for row in gradebook]
        column_count = len(column)
        column_sum = sum(column)
        column_average = column_sum / column_count
        print('Assignment ', i + 1, ': ', format(column_average, '.2f'), sep='')



def main():
    gradebook = [[61, 74, 69, 62, 72, 66, 73, 65, 60, 63, 69, 63, 62, 61, 64],
                 [73, 80, 78, 76, 76, 79, 75, 73, 76, 74, 77, 79, 76, 78, 72],
                 [90, 92, 93, 92, 88, 93, 90, 95, 100, 99, 100, 91, 95, 99, 96],
                 [96, 89, 94, 88, 100, 96, 93, 92, 94, 98, 90, 90, 92, 91, 94],
                 [76, 76, 82, 78, 82, 76, 84, 82, 80, 82, 76, 86, 82, 84, 78],
                 [93, 92, 89, 84, 91, 86, 84, 90, 95, 86, 88, 95, 88, 84, 89],
                 [63, 66, 55, 67, 66, 68, 66, 56, 55, 62, 59, 67, 60, 70, 67],
                 [86, 92, 93, 88, 90, 90, 91, 94, 90, 86, 93, 89, 94, 94, 92],
                 [89, 80, 81, 89, 86, 86, 85, 80, 79, 90, 83, 85, 90, 79, 80],
                 [99, 73, 86, 77, 87, 99, 71, 96, 81, 83, 71, 75, 91, 74, 72]]
    display_assignment_averages(gradebook)
    display_student_averages(gradebook)

main()

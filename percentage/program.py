student_marks ={
    'Luna': [24,25,24],
    'B': [30,40,50]
}

query_name = input()
if query_name in student_marks:
    # new_list = int(student_marks[query_name])
    # print(student_marks[query_name])
    #   new_list = list(map(, new_list))
    print(f'{sum(student_marks[query_name]) / len(student_marks[query_name]):.2f}')

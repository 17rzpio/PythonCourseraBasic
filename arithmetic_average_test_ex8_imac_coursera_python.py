n = int(input("\ntype n value of the student in the class: "))

approved_students=0
for k in range(n):
    test_grade_1 = float(input("\nDigite a primeira nota do aluno: "))
    test_grade_2 = float(input("\nDigite a segunda nota do aluno: "))
    test_grade_3 = float(input("\nDigite a terceira nota do aluno: "))
    average_test_grade = (test_grade_1+test_grade_2+test_grade_3)/3
    if average_test_grade >= 5:
        approved_students+=1

failed_students = n - approved_students
print("students approved: ",approved_students)
print("students failed: ",failed_students)

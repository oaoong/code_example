n = int(input())
students = [list(input().split()) for _ in range(n)]
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
[print(student[0]) for student in students]
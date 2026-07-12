with open("marks.txt","r") as f:
    top_marks=0
    top_name=""
    for student in f:
     name,marks=student.strip().split(",")
     marks=int(marks)
     if marks>top_marks:
        top_marks=marks
        top_name=name
    print("---toper---")
    print(top_name)
    print(top_marks)
 


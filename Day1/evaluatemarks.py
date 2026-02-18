def evaluate_marks(marks, attendance):
    if marks < 0 and marks > 100:
        raise ValueError("Value must be 0 - 100")
    if attendance < 0 and attendance > 100:
        raise ValueError("Value must be 0 - 100")
    
    if attendance > 75:
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B" 
        elif marks >= 50:
            return "C"
        else:
            return "F"
    else:
        return "C"


def main():
    marks = int(input("Enter Mark: "))
    attendance = int(input("Enter attendance: "))
    result = evaluate_marks(marks, attendance)
    print("Grade",result)
main()
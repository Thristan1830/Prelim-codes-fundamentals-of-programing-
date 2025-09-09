def get_valid_input(prompt, min_val=0, max_val=100, is_integer=False):
    while True:
        try:
            value = int(input(prompt)) if is_integer else float(input(prompt))
            if value < min_val or value > max_val:
                print(f"Invalid input! Please enter a value between {min_val} and {max_val}")
            else:
                return value
        except ValueError:
            print("Invalid number! Please enter a number.")

def required_grades(target, prelim):
    prelim_contribute = 0.2 * prelim   
    remaining = target - prelim_contribute

    mid_term = remaining / 0.8 * 0.3
    final = remaining / 0.8 * 0.5
    average_required = remaining / 0.8

    return mid_term, final, average_required

def main():
    print("Student Grade Calculation")

    absences = get_valid_input("Enter the number of absences: ", min_val=0, max_val=100, is_integer=True)

    if absences >= 4:
        print("\nFAILED, TOO MANY ABSENCES")
        return
    
    
    Prelim_exam = get_valid_input("Enter Prelim Exam grade (0-100): ", 0, 100)
    Quizzes = get_valid_input("Enter Quizzes grade (0-100): ", 0, 100)
    Requirements = get_valid_input("Enter Requirements grade (0-100): ", 0, 100)
    Recitation = get_valid_input("Enter Recitation grade (0-100): ", 0, 100)

    
    attendance = 100 - (absences * 10)
    class_record = (0.4 * Quizzes) + (0.3 * Recitation) + (0.3 * Requirements)
    Prelim = (0.6 * Prelim_exam) + (0.1 * attendance) + (0.3 * class_record)

    print(f"\nPrelim Grade: {Prelim:.2f}")

   
    mid_term_pass, final_pass, average_pass = required_grades(75, Prelim)
    midterm_dl, final_dl, average_dl = required_grades(90, Prelim)

    print(f"\nTo Pass (75%), you need an average of {average_pass:.2f} in midterms & finals")
    print(f"(Suggested: midterm ~{mid_term_pass:.2f}, finals ~ {final_pass:.2f})")

    print(f"\nTo be a Dean's Lister (90%), you need an average of {average_dl:.2f} in midterms & finals")
    print(f"(Suggested: midterm ~{midterm_dl:.2f}, finals ~ {final_dl:.2f})")

if __name__ == "__main__":
    main()

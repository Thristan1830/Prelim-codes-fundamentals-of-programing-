import streamlit as st

def required_grades(target, prelim):
    prelim_contribute = 0.2 * prelim   
    remaining = target - prelim_contribute

    if prelim >= target:
        return 0, 0, 0

    mid_term = remaining / 0.8 * 0.3
    final = remaining / 0.8 * 0.5
    average_required = remaining / 0.8

    return mid_term, final, average_required

def main():
    st.title("Student Grade Calculator")

    absences = st.number_input("Enter the number of absences:", min_value=0, max_value=100, step=1)

    if absences >= 4:
        st.error("FAILED, TOO MANY ABSENCES")
        return
    
    st.subheader("Enter Your Grades")
    Prelim_exam = st.number_input("Prelim Exam grade", 0.0, 100.0, 75.0)
    Quizzes = st.number_input("Quizzes grade", 0.0, 100.0, 75.0)
    Requirements = st.number_input("Requirements grade", 0.0, 100.0, 75.0)
    Recitation = st.number_input("Recitation grade", 0.0, 100.0, 75.0)

    if st.button("Calculate"):
        attendance = max(0, 100 - (absences * 10))
        class_record = (0.4 * Quizzes) + (0.3 * Recitation) + (0.3 * Requirements)
        Prelim = (0.6 * Prelim_exam) + (0.1 * attendance) + (0.3 * class_record)

        st.success(f"Prelim Grade: **{Prelim:.2f}**")

        mid_term_pass, final_pass, average_pass = required_grades(75, Prelim)
        midterm_dl, final_dl, average_dl = required_grades(90, Prelim)

        if Prelim >= 75:
            st.info("You are already passing based on your Prelim grade!")
        else:
            st.write(f"To Pass (75%): You need an average of **{average_pass:.2f}** in midterms & finals")
            st.write(f"(Suggested: midterm ~**{mid_term_pass:.2f}**, finals ~**{final_pass:.2f}**)")

        if Prelim >= 90:
            st.info("You already qualify as Dean's Lister based on Prelim!")
        else:
            st.write(f"To be a Dean's Lister (90%): You need an average of **{average_dl:.2f}** in midterms & finals")
            st.write(f"(Suggested: midterm ~**{midterm_dl:.2f}**, finals ~**{final_dl:.2f}**)")

if __name__ == "__main__":
    main()
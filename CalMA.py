import streamlit as st

# Function to calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

# Function to generate result cards for multiple students
def generate_result_cards():
    st.title("Student Result Card Generator")

    num_students = st.number_input("Enter the number of students:", min_value=1, step=1)
    
    students_results = []

    for i in range(num_students):
        st.header(f"--- Enter details for Student {i + 1} ---")
        student_name = st.text_input(f"Enter student's name {i + 1}: ", key=f"student_{i}")

        if student_name:  # Proceed if the name is provided
            total_marks = 175  # 7 subjects, each out of 25 marks
            obtained_marks = 0
            subjects = {}

            # Get marks for each subject
            for subject in ['English', 'Conversation', 'Islamiat', 'Urdu', 'Math', 'Science', 'SST']:
                marks = st.number_input(f"Enter marks obtained in {subject} (out of 25): ", min_value=0, max_value=25, key=f"{subject}_{i}")
                subjects[subject] = marks
                obtained_marks += marks

            # Calculate percentage and grade
            percentage = (obtained_marks / total_marks) * 100
            grade = calculate_grade(percentage)

            # Store each student's results in a list
            students_results.append((student_name, obtained_marks, percentage, grade))

    if students_results:
        # Sort students by percentage to determine rank
        students_results.sort(key=lambda x: x[2], reverse=True)

        # Display result cards with ranks
        st.header("\n--------- All Students Result Cards ---------")
        for rank, (name, obtained, percentage, grade) in enumerate(students_results, start=1):
            st.subheader("\n--------- Result Card ---------")
            st.write(f"**Student Name:** {name}")
            st.write(f"**Total Marks:** {total_marks}")
            st.write(f"**Obtained Marks:** {obtained}")
            st.write(f"**Percentage:** {percentage:.2f}%")
            st.write(f"**Grade:** {grade}")
            st.write(f"**Rank:** {rank}")
            st.write("--------------------------------")

# Run the app
if __name__ == "__main__":
    generate_result_cards()

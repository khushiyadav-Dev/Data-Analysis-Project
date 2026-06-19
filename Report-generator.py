def calculate_grade(marks):
    """Unit 1: Conditional Logic & Functions"""
    if marks >= 90: return 'A'
    elif marks >= 80: return 'B'
    elif marks >= 70: return 'C'
    elif marks >= 50: return 'D'
    else: return 'F'

def generate_report():
    # 1. Unit 1 Data Structures: List of Dictionaries (Nested Data)
    students_data = [
        {"name": "Rahul", "marks": [85, 92, 78], "branch": "AIML"},
        {"name": "Sneha", "marks": [89, 95, 91], "branch": "CSE"},
        {"name": "Amit", "marks": [45, 52, 48], "branch": "AIML"},
        {"name": "Priya", "marks": [72, 68, 74], "branch": "IT"},
        {"name": "Rohan", "marks": [95, 91, 88], "branch": "CSE"}
    ]
    
    # 2. Unit 1 Data Structure: Set (To find unique branches)
    unique_branches = set()
    
    # Final results store karne ke liye list
    processed_students = []

    # 3. Unit 1 Loops & String Formatting
    for student in students_data:
        name = student["name"]
        branch = student["branch"]
        unique_branches.add(branch) # Set operations
        
        # Built-in functions (sum, len) aur basic math
        total_marks = sum(student["marks"])
        avg_marks = round(total_marks / len(student["marks"]), 2)
        grade = calculate_grade(avg_marks)
        
        # Tuple use kar rahe hain immutable record ke liye
        student_record = (name, branch, avg_marks, grade)
        processed_students.append(student_record)

    # 4. Unit 1: File Handling (Writing data to a file)
    try:
        with open("student_report_summary.txt", "w") as file:
            file.write("=========================================\n")
            file.write("     B.TECH SECOND YEAR PERFORMANCE REPORT\n")
            file.write("=========================================\n\n")
            
            file.write(f"Total Branches Participating: {', '.join(unique_branches)}\n")
            file.write(f"Total Students Evaluated: {len(students_data)}\n")
            file.write("-" * 41 + "\n")
            file.write(f"{'Name':<10}{'Branch':<8}{'Average':<10}{'Grade':<5}\n")
            file.write("-" * 41 + "\n")
            
            # Unpacking tuples while iterating
            for name, branch, avg, grade in processed_students:
                file.write(f"{name:<10}{branch:<8}{avg:<10}{grade:<5}\n")
                
            file.write("-" * 41 + "\n")
            file.write("Report Generated Successfully.\n")
            
        print("Success: 'student_report_summary.txt' has been created!")
        
    except IOError:
        print("Error: Could not write to file.")

# Function Call
if __name__ == "__main__":
    generate_report()

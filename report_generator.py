import csv
from fpdf import FPDF

# Read data from CSV file
names = []
marks = []

with open("marks.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        names.append(row["Name"])
        marks.append(int(row["Marks"]))

# Analyze data
total_students = len(marks)
average_marks = sum(marks) / total_students
highest_marks = max(marks)
lowest_marks = min(marks)

# Create PDF
pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Student Performance Report", ln=True, align="C")

pdf.ln(10)
pdf.set_font("Arial", size=12)

# Add student data
for i in range(total_students):
    pdf.cell(0, 8, f"{names[i]} : {marks[i]} marks", ln=True)

# Add summary
pdf.ln(10)
pdf.cell(0, 8, f"Total Students: {total_students}", ln=True)
pdf.cell(0, 8, f"Average Marks: {average_marks:.2f}", ln=True)
pdf.cell(0, 8, f"Highest Marks: {highest_marks}", ln=True)
pdf.cell(0, 8, f"Lowest Marks: {lowest_marks}", ln=True)

# Save PDF
pdf.output("student_report.pdf")

print("PDF Report Generated Successfully!")
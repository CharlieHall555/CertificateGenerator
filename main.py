import os
import imgkit

# --- 1. User input interface ---
semester_name = input("📘 Enter the semester name (e.g. SPRING SEMESTER): ").strip()

print("\n👥 Enter student names one by one. Type 'end' when done:")
student_names = []
while True:
    name = input("➤ Student name: ").strip()
    if name.lower() == "end":
        break
    if name:
        student_names.append(name)

instructor_name = input("\n✍️ Enter instructor name: ").strip()
instructor_name_upper = instructor_name.upper()

# --- 2. Paths & template ---
output_folder = "certificates"
os.makedirs(output_folder, exist_ok=True)

logo_path = os.path.abspath("logo.png").replace("\\", "/")
medal_path = os.path.abspath("medal.png").replace("\\", "/")

with open("template.html", "r", encoding="utf-8") as file:
    template_html = file.read()

# Replace static image paths with absolute ones
html_template = template_html.replace('src="logo.png"', f'src="file:///{logo_path}"')
html_template = html_template.replace('src="medal.png"', f'src="file:///{medal_path}"')

# --- 3. WKHTML settings ---
options = {
    'format': 'png',
    'quality': '100',
    'encoding': 'UTF-8',
    'width': '1000',
    'enable-local-file-access': '',
    # 'crop-h': '700',
    # 'crop-w': '960',
    'crop-x': '0',
    'crop-y': '0',
}

# --- 4. Certificate Generation ---
for student in student_names:
    personalized_html = html_template
    personalized_html = personalized_html.replace("GRIFFIN", student.upper())
    personalized_html = personalized_html.replace("SPRING SEMESTER", semester_name.upper())
    personalized_html = personalized_html.replace("Charlie Hall", instructor_name)
    personalized_html = personalized_html.replace("CHARLIE HALL", instructor_name_upper)

    output_path = os.path.join(output_folder, f"{student}.png")
    imgkit.from_string(personalized_html, output_path, options=options)
    print(f"✅ Generated: {output_path}")
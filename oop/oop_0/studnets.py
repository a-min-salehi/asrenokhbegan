class Student:
    def __init__(self, full_name, age, semester):
        self.full_name = full_name
        self.age = age
        self.semester = semester
        self.scores = []
    
    def add_score(self, score):
        self.scores.append(score)

    def calculate_avg_score(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def get_letter_grade(self):
        avg_score = self.calculate_avg_score()

        if avg_score >= 90:
            return "A+"
        elif avg_score >= 85:
            return "A"
        elif avg_score >= 80:
            return "A-"
        elif avg_score >= 75:
            return "B+"
        elif avg_score >= 70:
            return "B"
        elif avg_score >= 65:
            return "B-"
        elif avg_score >= 60:
            return "C+"
        elif avg_score >= 55:
            return "C"
        elif avg_score >= 50:
            return "C-"
        else:
            return "F"


# Example usage:
student1 = Student("John Doe", 18, "Spring")
student1.add_score(85)
student1.add_score(92)
student1.add_score(78)
student1.add_score(95)
student1.add_score(88)

print(f"Student Name: {student1.full_name}")
print(f"Age: {student1.age}")
print(f"Semester: {student1.semester}")
print(f"Scores: {student1.scores}")
print(f"Average Score: {student1.calculate_avg_score()}")
print(f"Letter Grade: {student1.get_letter_grade()}")

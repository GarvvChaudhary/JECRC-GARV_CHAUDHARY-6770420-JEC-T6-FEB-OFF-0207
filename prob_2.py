# Student Marks Performance Tracker

class Solution:

    def subject_average(self, students):
        subject_total = {}
        subject_count = {}
        
        for student in students:
            for subject, marks in student["marks"].items():
                
                if subject in subject_total:
                    subject_total[subject] += marks
                    subject_count[subject] += 1
                else:
                    subject_total[subject] = marks
                    subject_count[subject] = 1
        
        subject_average = {}
        for subject in subject_total:
            subject_average[subject] = subject_total[subject] / subject_count[subject]
        
        highest_subject = max(subject_average, key=subject_average.get)
        
        return subject_average, highest_subject
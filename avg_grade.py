#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 20:36:15 2023

@author: giannidiarbi

Gianni Diarbi
DS2000
Spring 2023
HW 3 Problem 1
avg_grade.py

Test case:
    HW grades - 85, 70, 95. Avg = 83.33
    Quiz grades - 80, 100. Avg = 90
    Viz grade = 95
    Overall average = (.75)(83.33) + (.20)(90) + (.05)(95) = 85.25
    
"""
GRADE_FILE = "ds2000_grades.txt"

HW_SCALE = 0.75
QUIZ_SCALE = 0.20
VIZ_SCALE = 0.05


def main():
    
    # Gather data -- initialize variables & read in the file contents
    number_hw = 0
    number_quiz = 0
    
    hw_score = 0
    quiz_score = 0
    viz_score = 0
    
    with open(GRADE_FILE, "r") as infile:
        while True:
            assignment_type = infile.readline().strip()
            assignment_score = (infile.readline().strip())
            
            if assignment_type == "":
                break
            
            # Computations - convert to float            
            assignment_score = float(assignment_score)
            
            # Collect data on the number of assignments in each category, and 
            # the total sum of scores of each category
            if assignment_type == "HW":
                number_hw += 1
                hw_score = hw_score + assignment_score
                
            elif assignment_type == "Quiz":
                number_quiz += 1
                quiz_score = quiz_score + assignment_score
                
            else:
                viz_score = assignment_score

        # Compute the average homework and quiz scores
        hw_avg = hw_score / number_hw
        quiz_avg = quiz_score / number_quiz

        # Compute the average DS2000 score
        ds_avg = (HW_SCALE * hw_avg) + (QUIZ_SCALE * quiz_avg) + \
                (VIZ_SCALE * viz_score)

    # Communication - report the calculated values!
    print("The average homework score is: ", round(hw_avg, 2), ".", sep = "")
    print("The average quiz score is: ", round(quiz_avg, 2), ".", sep = "")
    print("The overall DS2000 score is: ", round(ds_avg, 2), ".", sep = "")

main()

from list_utils import (
    get_top_n_marks,
    count_mark_occurrence,
    get_high_scorers
)

marks = [78, 45, 90, 66, 90, 88]

print("Original Marks:", marks)

top_marks = get_top_n_marks(marks, 3)
print("Top 3 Marks:", top_marks)

count_90 = count_mark_occurrence(marks, 90)
print("Count of 90:", count_90)

high_scorers = get_high_scorers(marks, 70)
print("High Scorers (>=70):", high_scorers)

print("Original Marks After Function Calls:", marks)

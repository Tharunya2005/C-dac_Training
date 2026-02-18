Assignment 3: Copy Investigation

This module demonstrates shallow and deep copy behavior in Python lists.

Functions implemented in list_utils.py:
1. create_shallow_copy(data) - Returns a shallow copy of the given list.
2. create_deep_copy(data) - Returns a deep copy using the copy module.
3. append_to_nested_list(data, value) - Appends a value to the first nested list found.

Testing:
- test_list_utils.py imports the functions.
- Creates a nested list (e.g., ["Vinod", ["Mumbai", "Delhi"]]).
- Demonstrates shallow copy vs deep copy behavior.
- Prints IDs using id() to verify differences.
- Shows how modifications affect original vs copied lists.

Learning Objectives:
- Understanding shallow vs deep copy.
- Using the copy module.
- Observing list mutation behavior.

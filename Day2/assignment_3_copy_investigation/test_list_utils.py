from list_utils import create_shallow_copy, create_deep_copy, append_to_nested_list

student_data = ["Vinod", ["Mumbai", "Delhi"]]
shallow_copy = create_shallow_copy(student_data)
append_to_nested_list(shallow_copy, "Chennai")
print("Shallow Copy:", shallow_copy)
print("Original after shallow modification:", student_data)
deep_copy = create_deep_copy(student_data)
append_to_nested_list(deep_copy, "Bangalore")
print("Deep Copy:", deep_copy)
print("Original after deep modification:", student_data)
print("Original ID:", id(student_data))
print("Shallow Copy ID:", id(shallow_copy))
print("Deep Copy ID:", id(deep_copy))

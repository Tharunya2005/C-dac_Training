def calculate_stipend_bonus(stipend, rating):
    """
    Docstring for calculate_stipend_bonus
    
    The Stipend must be a positive number
    The Rating must between 1 and 5
    Bonus Rules:
    Rating 5 → 30%
    Rating 4 → 20%
    Rating 3 → 10%
    Rating < 3 → 0%
    """
    if stipend <= 0:
        raise ValueError("Invalid Input")
        
    if rating < 0 or rating > 5:
        raise ValueError("The Rating must be between 1 and 5")

    if rating == 5:
        bonus = stipend*0.30
    elif rating == 4:
        bonus = stipend*0.20
    elif rating == 3:
        bonus = stipend*0.10
    else:
        bonus = 0
    return bonus     

def main():
    stipend = int(input("Enter Stipend: "))
    rating = int(input("Enter Rating: "))
    print("Stipend id : ",id(stipend))
    print("Rating id : ",id(rating))
    result = calculate_stipend_bonus(stipend, rating)

main()
def growthAnalyzer(principal, YearlyRate):
    da = principal * 2

    if YearlyRate <= 0:
        raise ValueError("Rate must be Greater than 0")
    
    camount = principal
    years = 0

    while (camount < da):
        interest = camount * (YearlyRate / 100)
        camount = camount + interest
        years += 1
        print("Year", years, "Amount:", camount)

    return years


def main():
    principal = int(input("Principal Amount: "))
    YearlyRate = int(input("Yearly Rate: "))
    result = growthAnalyzer(principal, YearlyRate)
    print("Total years required to double:", result)

main()

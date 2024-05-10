def adjusted_winner(valuation_A, valuation_B):
    n = len(valuation_A)

    allocation_A = [0] * n
    allocation_B = [0] * n

    for i in range(n):
        if valuation_A[i] / valuation_B[i] >= 1:
            allocation_A[i] = 1
        else:
            allocation_B[i] = 1

    points_A = sum(valuation_A[i] * allocation_A[i] for i in range(n))
    points_B = sum(valuation_B[i] * allocation_B[i] for i in range(n))
    
    # split the object with the lowest valuation discrapency between a and b! not the first that belongs to a!
    if points_A != points_B:
        for i in range(n - 1, -1, -1):
            if allocation_A[i] == 1 and valuation_A[i] / valuation_B[i] >= 1:
                p = (points_B - points_A + valuation_A[i]) / (valuation_A[i] + valuation_B[i])
                allocation_A[i] = p
                allocation_B[i] = 1 - p
                break

    return allocation_A, allocation_B

valuation_A = [10, 65, 25]  # A valuation of goods G1, G2, G3, sum should equal 100
valuation_B = [7, 43, 50]   # B valuation of the same goods with equal order

if sum(valuation_A) != 100 or sum(valuation_B) != 100:
    print("Invalid valuation input")
else:
    allocations = adjusted_winner(valuation_A, valuation_B)
    print("Allocation for Ann:", allocations[0])
    print("Allocation for Bob:", allocations[1])

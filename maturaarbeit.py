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
    if points_A == points_B:
        return allocation_A, allocation_B

    split_in_favour_of_A = points_A > points_B
    good_to_split = None
    best_ratio = float('inf')

    for i in range(0, n):
        if allocation_A[i] == (1 if split_in_favour_of_A else 0) and valuation_A[i] / valuation_B[i] < best_ratio:
            good_to_split = i
            best_ratio = valuation_A[i] / valuation_B[i]

    p = (points_B - points_A + valuation_A[good_to_split]) / (valuation_A[good_to_split] + valuation_B[good_to_split])
    allocation_A[good_to_split] = p * -1
    allocation_B[good_to_split] = 1 + p

    return allocation_A, allocation_B

valuation_A = [10, 65, 25]  # A valuation of goods G1, G2, G3, sum should equal 100
valuation_B = [7, 43, 50]   # B valuation of the same goods with equal order

if sum(valuation_A) != 100 or sum(valuation_B) != 100:
    print("Invalid valuation input")
else:
    allocations = adjusted_winner(valuation_A, valuation_B)
    print("Allocation for Ann:", allocations[0])
    print("Allocation for Bob:", allocations[1])

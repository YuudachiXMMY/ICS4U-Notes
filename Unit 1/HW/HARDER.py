def find_maximum(A):
    #Base case:
    if len(A) == 1:
        return A[0]
    # Recursive case
    else:
        return max(A[0], find_maximum(A[1:]))

def main():
    print(find_maximum([1,2,3,4,5]))

main()
    
def radixSort(a):

    # Create Buckets (1 bucket for each digit) -> Row index# of 2D list matches the digit
    buckets = []
    for i in range(0, 10):
        buckets.append([])

    # Need the number with the maximum number of digits to determine how many sweeps of the list
    maxNum = max(a)
    maxDigits = len(str(maxNum))

    # Sort the list
    for d in range(0, maxDigits):

        # Take from the list and put into the buckets
        for i in range(0, len(a)):
            number = a[i]
            currentDigit = number // 10 ** d % 10
            buckets[currentDigit].append(number)
        a.clear()

        # Take From the buckets and put back into the list
        for i in range(0, len(buckets)):
            digit = buckets[i]
            for j in range(0, len(digit)):
                number = digit[j]
                a.append(number)
            digit.clear()

#Testing
import random
def main():
    # Generate a random list
    myList = []
    for i in range(0, 20):
        myList.append(random.randint(0, 100000))
    #myList = [7055, 847, 3531, 1943, 8297, 182, 28, 1812, 2861, 5608]
    radixSort(myList)
    print(myList)

main()
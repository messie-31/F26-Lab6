# Author: Mehtaash Kaur
# Date: 2026-11-04
# TO DO 1: Complete the functions below.
def buildtheSet(divisor):
    # Returns a set of numbers between 0 and 100 divisible by divisor
    return {n for n in range(0, 101) if n % divisor == 0}

def main():
    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")

    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")

    s7 = buildtheSet(7)
    print("s7: ", s7)
    print("----------------------------------------")

    s11 = buildtheSet(11)
    print("s11: ", s11)

main()
# TO DO 2: Run the script. Take screenshot of only buildtheSet() function. No need to capture main() in the screenshot. 

# Author: Mehtaash Kaur
# Date: 2026-11-04

# TO DO 1: Copy the code from lab5b.py and paste here.
# TO DO 2: Create the function s3_and_s5_not_s7().
# TO DO 3: Run the script. Take screenshot of only s3_and_s5_not_s7() function. No need to capture main() in the screenshot. Make sure you show the output in the screenshot.
def buildtheSet(divisor):
    return {n for n in range(0, 101) if n % divisor == 0}
 
def s3_or_s5(s3, s5):
    return s3.union(s5).difference(s3.intersection(s5))
 
def s3_and_s5_not_s7(s3, s5, s7):
    # Elements in s3 and s5, but not in s7
    return s3.intersection(s5).difference(s7)
 
def main():
 
    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("-----------------------------------------")
 
    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("-----------------------------------------")
 
    s7 = buildtheSet(7)
    print("s7: ", s7)
    print("-----------------------------------------")
 
    result = s3_and_s5_not_s7(s3, s5, s7)
    print("s3 and s5 not s7: ", result)
 
main()
# Author: Mehtaash Kaur
# Date: 2026-11-04
# TO DO 1: Copy the code from lab6a.py and paste here.
# TO DO 2: Create the function s3ors5().
# TO DO 3: Run the script. Take screenshot of only s3ors5() function. No need to capture main() in the screenshot. Make sure you show the output in the screenshot.
def buildtheSet(divisor):
    return {n for n in range(0, 101) if n % divisor == 0}
 
def s3_or_s5(s3, s5):
    # Elements in s3 or s5, but not both (symmetric difference)
    return s3.union(s5).difference(s3.intersection(s5))

def main():
 
    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("-----------------------------------------")
 
    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("-----------------------------------------")
 
    s3ors5 = s3_or_s5(s3, s5)
    print("s3ors5: ", s3ors5)
 
main()
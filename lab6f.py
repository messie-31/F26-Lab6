# Author: Mehtaash Kaur
# Date: 2026-11-04

# TO DO 1: Create function histogram() as instructed in readme.md file. 
# TO DO 2: Create main() function and call histogram(). Call the main() function.
# TO DO 3: Run the script. Take screenshot of code showing the functions histogram() and main(). Also show output in the screenshot.
def histogram(text):
    counts = {}
    for ch in text:
        if ch == " ":
            continue
        counts[ch] = counts.get(ch, 0) + 1
    for letter, count in counts.items():
        print(letter, "*" * count)
 
def main():
    histogram("hello amma")
 
main()
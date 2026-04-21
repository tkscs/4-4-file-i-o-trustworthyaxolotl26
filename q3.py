# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)


with open("romeo_and_juliet.txt", "r") as f:
    rj_text = f.read()
    
js = rj_text.lower().count("juliet")

print(js)

# Count how many times the word "Juliet" appears

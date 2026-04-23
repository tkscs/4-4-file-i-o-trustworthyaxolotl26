# Read and print the contents of the file "q1.txt"

with open("q1.txt", "r") as f:
    text = f.read()

print(text)



with open("qfox.txt", "w") as f:
    f.write("""foxes

  /\-/\                _____
< •    \         _____/   __]
  \       \_____/  _____/
   \              /
   |   _______   |
   | |  |     || |
  [_|_|      [_|_|

            

            
                        dont forget to save yous filesesessss
            
 


  /\_____/\
            
  |      |
  |      |
 <\______/>
 < • V  • >
 <________>

            
            """)

with open("qfox.txt", "r") as f:
    foxread = f.read()

print(foxread)
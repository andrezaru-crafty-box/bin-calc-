i = input('bit tools or addition ') 
if i == ("addition"):
   #input first number
   c = input("first number ")
   # #input second number
   d = input("second number ")
   #addition of numbers
   add = int(c) + int(d)
   #prints the equation in binary
   print(bin(int(c))[2:],"+",bin(int(d))[2:])
   #prints the total
   print (bin(add)[2:])
else:
 #input the subject of the equation or the base ex decimal or binary (binary glitches with using the base as a display)
 #a = input('subject ')
 #or pure binary
 a = 2
 #input the power of the subject or bits like 8
 b = input('bits ')
 #b = 1 + int(input('power '))
 #answer is calculated in variable ans using a to the power of b
 ans = int(a) ** int(b)
 #it prints the different codes possible within the chosen bits 
 print("different codes",ans)
 #it prints the largest possible number within the chosen bits
 print("largest int",ans-1)
 #it prints the range of numbers possible within the chosen bits
 print(0,"to",ans-1) 
 #prints the range in binary
 print(bin(0)[2:],"to",bin(ans-1)[2:])
 #two's compliment max negative number in both decimal and binary
 twoc = int(a) ** (int(b)-1)
 print(-twoc,"=",twoc-1)
 print(-twoc,"=",str(bin(-twoc)[3:]))
 #Developed in Malta By Andre Micallef 


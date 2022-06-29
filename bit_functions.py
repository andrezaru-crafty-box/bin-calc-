# does the same bit calculations as original projects
def bitnumbers(b):
 p = 2
 #answer is calculated in variable ans using a to the power of b
 ans = int(p) ** int(b)
 #it prints the different codes possible within the chosen bits 
 print("different codes",ans)
 #it prints the largest possible number within the chosen bits
 print("largest int",ans-1)
 #it prints the range of numbers possible within the chosen bits
 print(0,"to",ans-1) 
 #prints the range in binary
 print(bin(0)[2:],"to",bin(ans-1)[2:])
 #two's compliment max negative number in both decimal and binary
 twoc = int(p) ** (int(b)-1)
 print(-twoc,"=",twoc-1)
 print(-twoc,"=",str(bin(-twoc)[3:]))
#shows minimum number in a two's compliment binary register
def twoc(b):
   p = 2 #defines base
   tc = int(p) ** (int(b)-1) #calculates two's compliment
   return(-tc)
#shows the amount of codes in a regular binary register
def bitstrut(b):
   p = 2
   ans = int(p) ** int(b)
   return(ans)
#shows largest possible integer in a regular binary register
def largestint(b):
   a = bitstrut(b)
   a = a - 1
   return(a)

#all demo's of functions are in 8 bit
ans = twoc(8)
print (ans)
ans = bitstrut(8)
print (ans)
ans = largestint(8)
print (ans)
#Developed in Malta By Andre Micallef 
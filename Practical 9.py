fh = open("prac 9.txt",'w')
def GenerateTable(num):
   i = 0
   k = 1
   while k <= 10:
        fh.write(str(num)+"x"+str(k)+"="+str(num*k)+"\n")
        k = k + 1
Table=int(input("enter number:"))
GenerateTable(Table)
fh.close()
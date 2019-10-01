def MaxWord(p):
   #Step-1:To Open the file 
   f=open(p,"r")
   
   #Step-2:To Read the file
   str2=f.read()

   #Step-3:Convert the file to list through split()
   l=str2.split()

   #Step-4:count the length
   m=len(l)

   #Step-5:Create a empty dictionary to store the values
   dict={}
   t=True
   i=0
   j=i+1
   #Step-6:Start a while loop to loop the values of list
   while t:

       counter=1
       #Step-7:Start another loop to loop the values for compare
       while t:
        
           #Step-8:To check if the list is empty
           if j==m:
               break

           #Step-9:Sarch the values to get the no. of element
           elif l[i]==l[j]:

               #Step-10:if search found increase the counter no.
               counter+=1

               #Step-11:delete the searched element because it again repeat the searched element
               del l[j]
               #Step-12:Decrease the length to overcome the list index out of bound exception.
               m=m-1
           else:

               #Step-13: If not found then increase the value j
               j+=1
       #End of 2nd while loop

       #Step-14: After get the counter value store the element as key with counter as value 
       dict[l[i]]=counter
       i+=1
       j=i+1

       #Step-15: Check if the i is in end of list
       if i==m:
           break
   print(dict)
   #Step-16: Sort the dictionary to get the highest value
   li=sorted(dict.items(), key=lambda x:x[1],reverse=True)

   #Step-17: iteration to get the all values
   for x in range(5):
       print(li[x])
#MaxWord("NewT.txt")
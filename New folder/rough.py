
#printing bsdu 10 times by method 1
"""
n=0
while(n<10):
    a="BSDU"
    b = a.lower()
    print "{}  <->  {}".format(a,b)
    n+=1
"""

#printing bsdu 10 times by method 2
"""   n=0
while(True):
    a="BSDU"
    b = a.lower()
    print "{}  <->  {}".format(a,b)
    if(n<=5):
        n+=1
    else:
        break
"""

#printing first 10 natural numbers method 1
"""
n=0
while(n<10):
    print n
    n+=1
"""

#printing first 10 natural numbers method 2
"""
n=0
while(True):
    print n
    if (n<10):
        n+=1
    else:
        break
"""

#printing even numbers from 1 to 10
"""
n=1
while(n<10):
    if (n%2==0):
        print n
    n+=1
"""
    
#printing odd numbers from 1 to 10
"""
n=1
while(n<10):
    if (n%2!=0):
        print n
    n+=1
"""

n=2
while(n<10):
   i=1
   while i < n:
       print "i = ",i
       i+=1
       if(n%i==0):
           if i == n:
               i-=1
           break
       print  " n = ",n

   if(i == n-1):
       print " prime number is =",n
   n+=1    

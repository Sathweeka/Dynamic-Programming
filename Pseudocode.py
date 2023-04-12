'''
1. What will be the output of the following pseudocode for a = 3, b = 8?
Integer funn(Integer a, Integer b)
  if(b mod a <2)
     b=b>> 1
     return a
  End if
  if(a mod b < 2)
     b=b+12
     return b
  end if
  return a + b + 5
End function funn()
ans=16

3. What will be the value of the following pseudocode?:

Integer j, m
Set m = 1, j = 1
Integer a[3] = {0,1,4}
if (a[m1] || (a[-1] && a[1]))
a[j] = 5
End if
m = m + a[j]
Print m

a. 3 b. 4 c. 6 d.
ans= 6

4. What will be the value of the following pseudocode for x = 27?

Integer fun (Integer x)
  if (x > 9)     //  27    3>9
    fun(x/9)      //fun(3)
    Print x - 1
    fun(x/3)    //27/3=fun(9)
  else
    print x - 2    //9-2=7
  end if
end function fun()

a. 1 26 7 b. 26 7 1 c. 9 8 2 d. 7 80 1
ans = 1 26 7

6. What will be the value of the following pseudocode? Input f = 6, g = 9
and set sum = 0

Integer n
if (g> f)
   for (n= f; n<g; n=n+1)
       sum = sum + n
   End for loop
else
   Print Error Message
Print sum
ans=21

7.What will be the value of the following pseudocode?

Integer j, m
Set m = 1, j=1
Integer a[3]={0, 1, 0}
a[0]= a[0]+a[1]
a[1] = a[1] + a[2]
a[2] a[2]+ a[0]
if(a[0])
     a[j] = 5
End if
m = a[j]+1
Print m

a. 3 b. 2 c. 6 d. 4
ans= 6

8. Which of the following options is correct for the given code for
n = 39 and r = 13?

Integer f1(Integer n, Integer r)//n=39    13   4 r=13
  if(n > 0)
    return (n-r + f1(n/3, 13))//13   4  //4-13+(-12)   //39-13-21=5
  else
    return 0
  end if
End function f1 ()
a. 3 b. 0 c. 5 d. 1
//39 13---->5
//13 13---> -21
//4 13---> -21
//1 13---> -12
//0 13
ans= 5

9.What will be the value of the following pseudocode for k=150 ?
fun(integer k)
     if(k>155)
        return
     end if
     print k
     fun(k+2)
     print k
End of function fun()
a.150 152 154 b.150 152 154 154 152 150 c.150 d.None of these
ans= 150 152 154 154 152 150

10.Which of the following is the most appropriate option for the output of the
given pseudocode for n = 25?

Integer foo(Integer n)
  if(n EQUALS 1)
    return 1
  else if((n MOD 2) EQUALS 0)
    return n*2
  else
    return foo(n - 10/3)
  end if
End function foo()

a.20 b. 44 c. 15 d. 25.
ans=44

11.What will be the output of the following pseudocode?

Integer a[5], b[5], c[5], k, 1
Set a[5]= (5, 9, 7, 3, 1}
Set b[5] = {2, 4, 6, 8, 10)
for(each k from 0 to 4)
  c[k]= a[k] - b[k]
end for
for (each i from 0 to 4)
  Print c[i]
end for
a. 7 13 13 11 11  b. 3 5 1 -5 -9  c. -3 -5 -1 59  d. Non
ans= b. 3 5 1 -5 -9

12. 15. What will be the output of the following pseudocode?

Integer p, q r
Set q = 13
for (each p from 1 to 4)
  r = q mod p //13mod1=0  
  P = p + 5 //p=1+5=6
  q = p + r //q=6+0=6
end for
r = q/5  //6/5=1
Print q, r  //6 1

a. 64 b. 13 c. 7 2 d. 6 1
ans= 6 1

16. What will be the output of the following pseudocode?

Integer x
Set x = 259
if(x EQUALS 0)
  Print "0"
otherwise if(x MOD 9 EQUALS 0)
  Print "9"
otherwise
  Print x MOD 9
end if
a. 8
b. 16
c. 7
d. None

ans=7

18. Which of the following output is correc for the given code if n = 64?

Integer large (Intger n)
  if(n <=1)
    return 1
  end if
  if(n mod 4 EQUALS 8)
    return large (n/4)
  end if
  return large (n/4) + large (n/4+ 1)
End function large()

a. 1
b.0
c. 6 
d. 4

ans= 1

22. What will be the output of the following pseudocode a=2,

b=2?

Integer funn (Integer a, Integer b)
  if(a & b > 0)
    return 1+ funn (a - 1, b) + funn(a, b - 1)
  End if
  return 0
End function funn()
a. 1 b. 2 c. 4 d. 9

ans = 1

24. What will be the output of the following pseudocode?

Integer i
Set i = 0
Start: i = 12
Print i
if(i<60)
  goto Start
else
  Print i + 1
end if
a. 0 12 0 12 13         c. 12 infinite times 

b. 12 24 36 48 60 61     d. 0 12 24 25

ans = 12 infinite times

29. What will be the output of the following pseudocode for a=5, b=1

Integer funn(Integer a, Integer b)
  if((b+a||a-b) && (b>a) && 1)
    a=a+b+b-2
    return 3-a
  else
    return a-b+1
  end if
  return a+b
End function fun()
a.0  b.5 c.16 d.11

ans= 5

32. What will be the output of the following pseudocode a = 1, b = 3?

Integer funn (Integer a, Integer b)
  if (a&1 && 1)
    return funn (a-1, a+a) + funn (a-1, b+b)
  Else
    return b^a
  End if

a. 8 b. 26 c. 1 d. 15
ans=8



'''

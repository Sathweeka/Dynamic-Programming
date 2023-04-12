'''
1. What will be the output of the following pseudocode?

Integer a, b, c
Set a = 5, b = 5, c = 9
if((b && (c >> 1)) || (b && (c << 1)))
  a = a^1   //4
End if
Print a + b + c  //4+5+9=18

a. 18 b. 27 c. 14 d. 19

ans=18

2. What will be the output of the following pseudocode?

Integer a, b, c
Set a= 4, b = 1, c = 2
if(b^(c & a) && a ^ (c & b)) //true
  c=a+a //8
  a=c+C //8+8=16
Else
  c= b + b
  b = c + c
End if
Print a+b+c   //8+16=25

a. 22 b. 31 c. 34 d. 25
ans=25

3. What will be the output of the following pseudocode?

Integer a, b, c
Set a= 1, b = 2
for (each c from 4 to 6)
  a = a^ b  //3
  if(c-a < b + a) //true
    b = 2
    a = 1
    Jump out of the loop
  End if
  a = a ^ c
End for
Print a + b //1+2=3

a. 2 b. 8 c. 3 d. 16
ans = 3

4. What will be the output of the following pseudocode?

Integer a, b, c
Set a = 2, b = 1
for (each c from 1 to 5)
  if(c> 3 || b >3)
    a = a + c
  End if
  b = b - 1
  b = b + a
End for
b = b+1
Print a + b

a. 30 b. 33 c. 31 d. 37
ans = 31

9. What will be the value of s if n = 127?
Read n
i=0,s=0
Function Sample(int n)
  while (n>0)
    r = n%10
    p = 8^i
    s = s+p*r
    i++
    n = n/10
  End While
return s;
End Function

a. 27 b. 187 c. 84 d. 12

ans=84

10. What will be the value of s if N=20?

Read N
Function sample (N)
  s = 0, F = 1, i=1;
  Do Until i <= N
    f = f*i;
    s = s +(i / f);
    i = i+1
    End Do
    return(s);
End Function
a. 666667 b. infinite loop c. 708333 d. 716667
ans= 2
'''

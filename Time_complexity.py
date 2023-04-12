'''
Time Complexity: Thetime complexity of an algorithm quantifies the amount of
time taken by an algorithm to run as a function of the length of the input.
Note that the the time to run is a function of the length of the input and not
the actual execution time of the machine on which the algorithm is running on.

Asymptotic notation is a way to describe the running time or space
1. Big-O Notation(Worst case)
2. Omega Notation(Best case)
3. Theta Notation(Average case)

     Big-O Notation(Worst case)
Ex-1:for(int i=0;i<n;i++){}
     loop run 'n' times
     hence time complexity = O(n)
Ex-2:for(int i=0;i<n;i+2){}
     loop run 'n' times
     hence time complexity = O(n)
Ex-3:for(int i=n;i>1;i--){}
     loop run 'n' times
     hence time complexity = O(n)
Ex-4:for(int i=1;i<n;i++){}
     for(int j=1;j<n;j++){}
     two individual loops run 'n+n=2n' times which is still linear
     hence time complexity = O(n)
Ex-5:for(int i=0;i<n;i++){}
       for(int j=0;j<n;j++){}
     }
     Nested loop run 'nxn = n^2' times which is non-linear
     hence time complexity = O(n^2)
Ex-6:for(int i=1;i<n;i=i*2){}
    values of 'i' in 'for' loop
    1
    2
    2^2
    2^3
    2^4
    .
    2^k

    The loop will terminate when:-
    i>=n
    2^k>=n
    k>=log2(n)
    so log2(n) is total unit of time taken by the loop
    hence time complexity = O(log2(n))

Ex-7:for(int i=n;i<n;i=i*3){}
    calculation:
    similar to the last example,
    values of 'i' in 'for' loop is i =3^k

    The loop will terminate when:-
    i>=n
    3^k>=n
    k>=log3(n)
    so log3(n) is total unit of time taken by the loop
    hence time complexity = O(log3(n))

Ex-8:for(int i=n;i>1;i=i/2){}
    calculation:
    values of 'i' in 'for' loop
    n
    n/2
    n/2^2
    n/2^3
    .
    .
    n/2^k

    The loop will terminate when:-
    i<=1
    n/2^k<=1
    2^k>=n
    k>=log2(n)
    so log2(n) is total unit of time taken by the loop
    hence time complexity = O(log2(n))

Ex-9:for(int i=0;i<n;i++){}
       for(int j=0;j<n;j=j*2){}
     }
     calculation:
     outer loop complexity = O(n)
     inner loop complexity = O(log2(n))
     hence time complexity = O(nlog2(n))

Ex-10:int p=0;
      for(int i=1;p<=n;i++){
         p=p+i;
      }
    calculation:
    values of 'i' and 'p' in 'for' loop:-
    -----------------------------------------------
    i  p
    ---------------------------------------------------------
    1  0+1=1
    2  1+2=3
    3  1+2+3=6
    4  1+2+3+6
    .   .
    .   .
    k  1+2+3+4+....+k
    k  k(k+1)/2
    ---------------------------------------------------------
    The loop will terminate when:-
    p>n
    k(k+1)/2>n
    k^2 > n
    k >n^(1/2)
    so n^(1/2) is total unit of time taken by the loop
    hence time complexity = O(n(1/2))

Ex-11:int p=0;
      for(int i=1;i<n;i=i*2){
         p++;
      }
      for(int j=1;j<pa;j=j*2){
        //statement
      }
      calculation:
    values of 'i' and 'p' in 'for' loop:-
    -----------------------------------------------
    i  p          condition
    ---------------------------------------------------------
    1  0           1<10
    2  1           2<10
    4  2           4<10
    8  3           8<10
    

     2^k               p
     ---------------------------------
    The loop will terminate when:-
    i>=n               
    2^k>=n
    k=log2(n)         p=log2(n)
    log2(p)= log2(log2(n))
    
    so log2(log2(n)) is total unit of time taken by the loop
    hence time complexity = O(log2(n))
'''

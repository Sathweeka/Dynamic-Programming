'''
while loop

If you understand how to calculate the time complexity of for loop then while
loop is piece of cake.
Example 1
int i=1;
while(i<n){

//statement
 i=i*2

Time Complexity=(log2(n)

Example 2

int i=n;
while(i>1){
 //statement
  i=i/2;
}
Time Complexity (log2(n))

Example 3

int i=1;
int k=1.
while(k<n){
  //statement
  k=k+i;
  i++;
}
Time Complexity O(n^(1/2))

Question 1

method (n, m){
  while(n!=m)
 {
   if(n>m){
     n =n-m;
   }else{
     m = m-n;
   }
  }
}
Time Complexity : if n>m then O(n)
                  if m>n then O(m)

Question 2

method(n){
  if(n<5){
    //statement
  }else{
    for(i=0;i<n;i++){
      //statement
    }
  }
}
Time Complexity :O(n)

Question 3

test(int n){
  if(n>0){
    //statement
    test(n-1);
  }
}
Time Complexity :O(n)
//T(n) = T(n-1) + 1 = O(n)

Question 4

test(int n){
  if(n>0){
      for(int i=0; i<n; i++){
    //statement
    }
    test(n-1);
  }
}
Time Complexity :O(n^2)
//T(n) = T(n-1) + 1 = O(n^2)
Base case:
T(0) = 1
Time taken by nth task:-
T(n)=T(n-1) + n
T(n-1)=T(n-2) + n-1
T(n-2)=T(n-3) + n-2
...
...
T(n)=T(n-3) +(n-2) + (n-1) + n
T(n)=T(n-k) +(n-(k-1)) + (n-(k-2)) + ....+(n-1) + n

)

Question 5

test(int n){
  if(n>0){
      for(int i=0; i<n; i=i*2){
    //statement
    }
    test(n-1);
  }
}
Time Complexity :O(nlog2(n))
Question 6
test(int n){
  if(n>0){
     
    //statement
    
    test(n-1);
    test(n-1);
  }
}

T(n-1)=2T(n-2)+1
T(n-2)=2T(n-3)+1
...
...
T(n)=2[2[2T(n-3)+1]+1]+1
T(n)=2^3T(n-3)+2^2+2+1
T(n)=2^k T(n-k)+2^(k-1)+2^(k-2)+... +2^2+2+1

Assume (n-k)th is Oth task means n=k
T(n)=2^nT(0)+(2^n-1)
T(n)=2^n+(2^n-1)=2^n

Time Complexity :O(2^n)



Example 7

test(int n){
  if (n>0){
   //statement
   test(n/ 2):
   }
  } 

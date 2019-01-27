// factorial(a)

// C Counterpart:
// int v = 5; // fac(v)
// int c = 1;// current value
// for (int i=v;i> 0 ;i--){
//  // c=c*i    
//  int k =0;
//    while(k<i){
//        c=c+c   
//  k++
// }   
// } 

// @5
// D=A
// @v
// M=D  // value to take the factorial of 
// D=M
// @i  // increment variable
// M=D
// @c  // answer variable
// M=1

// (LOOP)
// @v
// D=M
// @i
// D=D-M
// @END
// D;JLT       // if ( i < 0) break; if ((v-i) < 0)
// // Now C = C*i

@k  // temp counter variable to calculate the multiplication
M=0

(MULT)
@6
D=A
@d // temp variable to calculate the multiplication
M=D+M
@k  
M=M+1 // k++
// if (k < i )Keep Multiplying
D=M
@5
D=D-A
@MULT
D;JLT

// // else
// @d
// D=M
// @c
// M=D

// @i
// M=M-1 // i--

// (END)
//     @END
//     0;JMP
// Adds 1 + .....+ 100

// C Counterpart:
//  int sum = 0;
//  for (int i=0;i<100;i++) {
//      sum+= i;
//  }

//(initializing) 

    @i      // our counter
    M=1     // RAM[i]=1
    @sum
    M=0     //sum=0

(LOOP)
    @i
    D=M     //D=RAM[i]
    @100    //              <-- Number
    D=D-A   //D=i-100
    @END
    D;JGT   // if (i > 100) > 0 goto END else Continue to the next line
    @i
    D=M     //D=i
    @sum
    M=D+M   // sum += RAM[i](stored in D register)
    @i
    M=M+1   // incrementing the counter
    @LOOP
    0;JMP   // goto LOOP
(END)
    @END
    0;JMP   // infinite loop so that the machine dosnt exacute program byound this point.

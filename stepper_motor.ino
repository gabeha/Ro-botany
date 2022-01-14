
#define A 2
#define B 3
#define C 4
#define D 5

#define F 6
#define G 7
#define H 8
#define I 9

#define J 22
#define K 24
#define L 26
#define M 28

#define N 32
#define O 34
#define P 36
#define Q 38

#define NUMBER_OF_STEPS_PER_REV 512

const int timeout = 1;

void setup()
{
  pinMode(A,OUTPUT);
  pinMode(B,OUTPUT);
  pinMode(C,OUTPUT);
  pinMode(D,OUTPUT);
  
  pinMode(F,OUTPUT);
  pinMode(G,OUTPUT);
  pinMode(H,OUTPUT);
  pinMode(I,OUTPUT);
  
  pinMode(J,OUTPUT);
  pinMode(K,OUTPUT);
  pinMode(L,OUTPUT);
  pinMode(M,OUTPUT);
  
  pinMode(N,OUTPUT);
  pinMode(O,OUTPUT);
  pinMode(P,OUTPUT);
  pinMode(Q,OUTPUT);
}

void write(int a,int b,int c,int d)
{
  digitalWrite(A,a);
  digitalWrite(B,b);
  digitalWrite(C,c);
  digitalWrite(D,d);
  digitalWrite(F,a);
  digitalWrite(G,b);
  digitalWrite(H,c);
  digitalWrite(I,d);

  digitalWrite(J,a);
  digitalWrite(K,b);
  digitalWrite(L,c);
  digitalWrite(M,d);
  digitalWrite(N,a);
  digitalWrite(O,b);
  digitalWrite(P,c);
  digitalWrite(Q,d);
}

void onestep()
{
  write(1,0,0,0);
  delay(timeout);
  write(1,1,0,0);
  delay(timeout);
  write(0,1,0,0);
  delay(timeout);
  write(0,1,1,0);
  delay(timeout);
  write(0,0,1,0);
  delay(timeout);
  write(0,0,1,1);
  delay(timeout);
  write(0,0,0,1);
  delay(timeout);
  write(1,0,0,1);
  delay(timeout);
}

void loop(){
  int i;
  i=0;
  while(i<NUMBER_OF_STEPS_PER_REV)
  {
    onestep();
    i++;
  }
}

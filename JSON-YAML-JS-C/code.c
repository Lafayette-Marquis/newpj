#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h> 
#include <unistd.h>
#include <conio.h> 

int main() {
  printf("Hello World!\n"); // Print message
  printf("\n"); // New Line
  printf("I am learning C!\n"); // second messsge
  printf("\n"); // New Line
  
  int myNum = 15;

  int myOtherNum = 23;
  printf("%d", myNum, "\n");

  // Assign the value of myOtherNum (23) to myNum
  myNum = myOtherNum;
  // myNum is now 23, instead of 15
  printf("%d", myNum, "\n");
  // Create boolean variables
  bool isProgrammingFun = true;
  bool isFishTasty = false;

  // Return boolean values
  printf("%d", isProgrammingFun);   // Returns 1 (true)
  printf("%d", isFishTasty);        // Returns 0 (false)
  return 0;
}
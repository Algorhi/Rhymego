#include <sys/ipc.h>
#include <sys/msg.h>
#include <stdio.h>
#include <string.h>

struct msgbuffer{
  char text[24];
} message;

int main(){
  int msqid = 32764;
  strcpy(message.text,"opensource.com");
  msgsnd(msqid, &message, sizeof(message), 0);
  printf("Message: %s\n",message.text);
  printf("Queue: %d\n",msqid);
  return 0;

}



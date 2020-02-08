#include <sys/ipc.h>
#include <sys/msg.h>
#include <stdio.h>

struct msgbuffer{
  char text[24];
} message;

int main(){
  int msqid = 32764;
  msgrcv(msqid, &message, sizeof(message),0,0);
  printf("nQueue: %d\n",msqid);
  printf("Got this message: %s\n",message.text);
  msgctl(msqid, IPC_RMID, NULL);
  return 0;

}



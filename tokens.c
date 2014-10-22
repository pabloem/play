#include <stdlib.h>
#include <stdio.h>
#include <strings.h>
#define TRUE 1
#define FALSE 0

int write_token(char *buffer, int buf_len, const char *str, int *start, 
                 char delimiter){
  const char *copy_head = str+*start;
  memset(buffer,0,buf_len);
  while(*copy_head != '\0' && *copy_head != delimiter){
    *buffer = *copy_head;
    buffer += 1;
    copy_head += 1;
    *start += 1;
  }
  if(buffer[0] == '\0' && *copy_head == '\0') return FALSE;
  *start += 1;
  return TRUE;
}

bool write_token_v2(char **t_start, int *len, char *str, int *p_start, 
                 char delimiter){
  *t_start = str+*p_start;
  *len = 0;
  while(*(*t_start+*len) != '\0' && *(*t_start+*len) != delimiter){
    *len += 1;
    *start += 1;
  }
  if(**t_start == '\0' && *(str+*p_start) == '\0') return FALSE;
  *start += 1;
  return TRUE;
}

int main(){
#define BUFF_SIZE 255
  char pass_buffer[BUFF_SIZE];
  int buff_parser = 0;
  int a = 0;
  while(1){
    a = write_token(pass_buffer,BUFF_SIZE, "adsasd;asd;tecv;fdg;9rao1", &buff_parser, ';');
    printf("A is: %d | Buffer is: %s\n",a,pass_buffer);
    if (a == 0) return 1;
  }
}

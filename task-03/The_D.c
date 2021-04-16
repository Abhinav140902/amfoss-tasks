#include <stdio.h>
#include <math.h>
#include <string.h>
int main() 
{
    int n;
    scanf("%d",&n);
    int b=(n-1)/2;
    int c=1;
    for(int a=1;a<=(n-1)/2;a++){
        for(int k=1;k<=b;k++)
        {
            printf("*");
        }
        for (int k=1;k<=c;k++)
        {
            printf("D");
        }
         for(int k=1;k<=b;k++)
          {
            printf("*");  
          }
        printf("\n");
         b--;
         c+=2;
    }
      for (int a=1;a<=n;a++)
      {
          printf("D");
      }
      printf("\n");
       b+=1;
       c-=2;
    for(int a=1;a<=(n-1)/2;a++){
        for(int k=1;k<=b;k++)
        {
            printf("*");
        }
        for (int k=1;k<=c;k++)
        {
            printf("D");
        }
         for(int k=1;k<=b;k++)
          {
            printf("*");
          }
        printf("\n");
         b++;
         c-=2;
    }
    return 0;
}

#include <stdio.h>
int main()
{
    int n, j=2;
    
    printf("n="); scanf("%i",&n);
    while(j<=n)
    {
        int count=1,i=2;
        while(i<=j/2)
        {
            if(j%i==0)
            {
                count=0;
                break;
            } 
            i++;  
        }
        if(count==1)
        {
            printf("%i ",j);
        }
        j++;
    }

    return 0;
}
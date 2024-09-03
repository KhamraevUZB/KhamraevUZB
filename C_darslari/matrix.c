// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>
// int main()
// {
//     int A[100][100],n,m;
//     printf("n=");
//     scanf("%i",&n);
//     printf("m=");
//     scanf("%i",&m);
//     for(int i=0; i<n; i++)
//     {
//         for(int j=0; j<m; j++)
//         {
//             A[i][j]=rand()%31;
//         }
        
//     }
//     for(int i=0; i<n; i++)
//     {
//         for(int j=0; j<m; j++)
//         {
//             printf("%2i ",A[i][j]);
//         }
//         printf("\n");
//     }
    
//     return 0;
// }





// #include <stdio.h>
// int main()
// {
//     int A[3][3]={1,2,3,4,5,6,7,8,9};
//     printf("Asosiy diogalanal elementlari: ");
//     for(int i=2; i>=0; i--)
//     {
//         for(int j=3-1; j>=0; j--)
//         {
//             if(i==j)
//             {printf("%i ",A[i][j]);}
//         }
//     }
//     printf("\nTeskari dioganal elementlari: ");
//     for(int i=0; i<3; i++)
//     {
//         for(int j=0; j<3; j++)
//         {
//             if(i+j==3-1)
//             {printf("%i ",A[i][j]);}
//         } 
//     }       
//     return 0;
// }



// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>
// int main()
// {
//     srand(time(NULL));
//     int A[100][100],n,m;
//     printf("n="); scanf("%i",&n);
//     printf("m="); scanf("%i",&m);
//     for(int i=0; i<n; i++)
//     {
//         for(int j=0; j<m; j++)
//         {
//             A[i][j]=rand()%11-5;
//             printf("%2i ",A[i][j]);
//         }
//         printf("\n");
//     }
//     int sum=0, fact=1;
//     for(int i=0; i<n; i++)
//     {
//         for(int j=0; j<m; j++)
//         {
//             sum+=A[i][j];
//             fact*=A[i][j];
//         }
//     }
//     printf("SUMMA: %i\nFACT: %i\n",sum,fact);
//     return 0;
// }



// #include <stdio.h>
// int main()
// {
//     int A[100][100],n,m;
//     printf("n va m qiymatlarini kiriting: ");
//     scanf("%i%i",&n,&m);
//     for(int i=0; i<n; i++)
//     {
//         for(int j=0; j<m; j++)
//         {
//             scanf("%i",&A[i][j]);
//         }
//     }
//     int max=A[0][0],min=A[0][0];
//     int imax=0, jmax=0;
//     for(int i=0; i<n; i++)
//     {
//         for(int j=0; j<m; j++)
//         {
//             if(A[i][j]>max)
//             { max=A[i][j]; imax=i; jmax=j; }
//             if(A[i][j]<min)
//             { min=A[i][j]; }

//         }
//     }
//     printf("Max=%i\tMin=%i\n",max,min);
//     printf("Max %i- qatorda va %i- ustunda",imax,jmax);
// }



#include <stdio.h>
#include <stdlib.h>
int main()
{
    int a[3][3];
    
    for(int i=0; i<3; i++)
    {
        for(int j=0; j<3; j++)
        {
            scanf("%i",&a[i][j]);
        }
    }
    printf("\n");
    int max=a[0][0];
    for(int i=0; i<3; i++)
    {
         for(int j=0; j<3; j++)
         {
            if(a[i][j]>max)
            {
                max=a[i][j];
            } 
         }
    }
    printf("%i",max);


    return 0;
}
// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>
// int main()
// {
//     srand(time(0));
//     int n, num[100];
//     printf("n="); scanf("%i",&n);
//     for(int i=0; i<n; i++)
//     {
//         num[i]=rand()%10;
//         printf("%i ",num[i]);
//     }
//     printf("\n");
//     return 0;
// }


// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>
// int main()
// {
//     srand(time(0));
//     int A[100],n;
//     printf("n="); scanf("%i",&n);
//     for(int i=0; i<n; i++)
//     {
//         A[i]=rand()%21-10;
//         printf("%i ",A[i]);
//     }
//     int juft[100],k=0,toq[100],h=0;
//     for(int i=0; i<n; i++)
//     {
//         if(A[i]%2==0)
//         {
//             juft[k]=A[i];k++;
//         }
//         else
//         {
//             toq[h]=A[i];h++;
//         }
//     }
//         printf("\nJuft seria: ");
//         for(int i=0; i<k; i++)
//         {
//             printf("%i ",juft[i]);
//         }
//         printf("\nToq seria: ");
//         for(int i=0; i<h; i++)
//         {
//             printf("%i ",toq[i]);
//         }
    
//     return 0;
// }



// #include <stdio.h>
// int main()
// {
//     int nums[100],n;
//     printf("n="); scanf("%i",&n);
//     for(int i=0; i<n; i++)
//     {
//         scanf("%i",&nums[i]);
//     }
//     int temp;
//     for(int i=0; i<n; i++)
//     {
//         for(int j=i+1; j<n; j++)
//         {
//             if(nums[i]>nums[j])
//             {
//                 temp=nums[i];
//                 nums[i]=nums[j];
//                 nums[j]=temp;
//             }
//         }
//     }
//     printf("After sorting: \n");
//     for(int i=0; i<n; i++)
//     {
//         printf("%i ",nums[i]);
//     }
//     printf("\n");
// }


#include <stdio.h>
int main()
{
    int n=5;
    char A[100]={1,2,3,4,5};
    int m,l;
    printf("Kiritiladigan sonni yozing: "); scanf("%i",&m);
    printf("Qaysi indexga qo'shilsin: "); scanf("%i",&l);
    printf("%i-indexga %i raqamini qo'shildi: ",l,m);
    printf("\nInput: ");
    for(int i=0; i<n; i++)
    {
        printf("%i ",A[i]);
    }
    printf("\n");
    printf("Output: ");
    for(int i=n; i>l; i--)
    {
        A[i]=A[i-1];
    }
    A[l]=m;
    for(int i=0; i<=n; i++)
    {
        printf("%i ",A[i]);
    }
    return 0;
}



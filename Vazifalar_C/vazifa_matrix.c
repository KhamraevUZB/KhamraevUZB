// 4-mavzu: Ikki o’lchovli seriya(Matrix)

// Uyga vazifa:
// 1) n ta qator va n ta ustundan iborat ikki o'lchovli seriya berilgan va
//  ushbu seriyadagi har bir qatordagi elementlar yig'indisini chiqaring.
// Input: n=3
// 1 2 3
// 4 5 6
// 7 8 9
// Output: 
// 1-qatorda 6
// 2-qatorda 15
// 3-qatorda 24


// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>
// int main()
// {
//     srand(time(NULL));
//     int A[100][100],n,m;
//     printf("Qatorlar soni="); scanf("%i",&n);
//     printf("Ustunlar soni="); scanf("%i",&m);
//     for(int i=0; i<n; i++)
//     {
//         for(int j=0; j<m; j++)
//         {
//             A[i][j]=rand()%9+1;
//             printf("%2i ",A[i][j]);
//         }
//         printf("\n");
//     }
//     int sum=0;
//     for(int i=0; i<n; i++)
//     {
//         for(int j=0; j<m; j++)
//         {
//             sum+=A[i][j];
//         }
//         printf("%i-Qatorda %i\n",i+1,sum);
//         sum=0;
//     }
//     return 0;
// }




// 2) n ta qator va n ta ustundan iborat ikki o'lchovli seriya 
// berilgan va ushbu seriyadagi har bir ustundagi maximum elementlarni chiqaring.
// Input: n=3
// 1 2 3
// 4 5 6
// 7 8 9
// Output: 
// 1-ustunda 7
// 2-ustunda 8
// 3-ustunda 9


// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>
// int main()
// {
//     srand(time(0));
//     int A[100][100],n,m;
//     printf("Qatorlar soni= ");
//     scanf("%i",&n);
//     printf("Ustunlar soni= ");
//     scanf("%i",&m);
//     for(int i=0; i<n; i++)
//     {
//         for(int j=0; j<m; j++)
//         {
//             A[i][j]=rand()%9+1;
//             printf("%2i ",A[i][j]);
//         }
//         printf("\n");
//     }
//     int max=A[0][0],min=A[0][0];
//     int imax=0, jmax=0;
//     for(int j=0; j<m; j++)
//     {
//         for(int i=0; i<n; i++)
//         {
//             if(A[i][j]>max)
//             { max=A[i][j]; imax=i; jmax=j; }

//         }
//         printf("%i-Ustunda %i Max\n",j+1,max);
//         max=0;

//     }
//     return 0;
// }


// 3) n ta qator va n ta ustundan iborat ikki o'lchovli seriya berilgan 
// va ushbu seriyadagi asosiy diagonal elementlarini teskari diagonal 
// elementlari bilan almashtiring va chiqaring.
// Input: n=3
// 1 2 3
// 4 5 6
// 7 8 9
// Output:
// 3 2 1
// 4 5 6
// 9 8 7




// #include <stdio.h>

// int main() 
// {
//     int n=3, m=3;
//     int A[3][3] = {1,2,3,4,5,6,7,8,9};
//     printf("Input:\n");
//     for(int i=0; i<n; i++) 
//     {
//         for(int j=0; j<m; j++)
//         {
//             printf("%i ",A[i][j]);
//         }
//         printf("\n");
//         int temp=A[i][i];
//         A[i][i]=A[i][n-2-i];
//         A[i][n-2-i]=temp;
//     }
//     printf("Output:\n");
//     for(int i=0; i<n; i++) 
//     {
//         for (int j = 0; j < n; j++) 
//         {
//             printf("%d ",A[i][j]);
//         }
//         printf("\n");
//     }

//     return 0;
// }



// 4) Ikki o'lchovli seriyani zikzak ko'rinishida 1dan boshlanadigan sonlar bilan 
// programmani o’zi to'ldirib bersin.
// Input: n=3          Input: n=4
// Output:            Output:
// 1 2 3             1  2  3  4
// 6 5 4             8  7  6  5
// 7 8 9             9 10 11 12
//                  16 15 14 13



// #include <stdio.h>
// int main()
// {
//     int n,count=0;
//     int A[100][100];printf("Input: ");
//     printf("n=");
//     scanf("%i",&n);
//     for(int i=0; i<n; i++)
//     {
//         for(int j=0; j<n; j++)
//         {
//             count++;
//             A[i][j]=count;
//         }
//         if(i%2!=0)
//         {
//             for(int j=0;j<n/2; j++)
//             {
//                 int temp=A[i][j];
//                 A[i][j]=A[i][n-1-j];
//                 A[i][n-1-j]=temp;
//             }
//         }
//     }
//     printf("Output: \n");
//     for(int i=0; i<n; i++)
//     {
//         for(int j=0; j<n; j++)
//         {
//             printf("%2i ",A[i][j]);
//         }
//         printf("\n");
//     }
//     return 0;
// }



// 5) n ta qator va m ta ustundan iborat ikki o'lchovli seriya berilgan. Ushbu seriyada birinchi manfiy elementigacha bo'lgan sonlarning yig’indisini (son+son+..) ko'rinishida chiqaring.
// Input: n=3 m=4
//  1  2  3  4
// -5  6  7  8
// -9 10 11 12
// Output: 1+2+3+4=10



// #include <stdio.h>
// int main()
// {
//     int n=3,m=4;
//     int A[100][100]={{1,2,3,4},{-5,6,7,8},{-9,10,11,12}};
//     for(int i=0; i<n; i++)
//     {
//         for(int j=0; j<m; j++)
//         {
//             printf("%2i ",A[i][j]);
//         }
//         printf("\n");
//     }
//     printf("Output: ");
//     int caunt=0;
//     for(int i=0; i<n; i++)
//     {
//         for(int j=0; j<m; j++)
//         {
//             if(A[i][j]>0)
//             {
//                 printf("%i ",A[i][j]);
//                 caunt+=A[i][j];
//             }
//             else if(A[i][j]<0)
//             {
//                break;
//             }
            

//         }
//     }
//     printf("= %i",caunt);

//     return 0;
// }


// 6) n ta qator va n ta ustundan iborat ikki o'lchovli seriya berilgan. Ushbu seriyada barcha qator elemenlarini 
// ustun elementlari bilan almashtiring va natijani ekranga chiqaring.
// Input: n=3
// 1 2 3
// 4 5 6
// 7 8 9
// Output: 
// 1 4 7
// 2 5 8
// 3 6 9



// #include <stdio.h>

// int main() 
// {
//     int n=3, m=3;
//     int A[3][3] = {1,2,3,4,5,6,7,8,9};
//     printf("Input:\n");
//     for(int i=0; i<n; i++) 
//     {
//         for(int j=0; j<m; j++)
//         {
//             printf("%i ",A[i][j]);
//         }
//         printf("\n");
        
//     }
//     printf("Output:\n");
//     for(int i=0; i<n; i++) 
//     {
//         for (int j = 0; j < n; j++) 
//         {
//             printf("%d ",A[j][i]);
//         }
//         printf("\n");
//     }

//     return 0;
// }


// 7) Ikki o'lchovli seriya berilgan. Ushbu seriyadagi max va min orasida (max bilan min kirmaydi) nechta element borligini aniqlang.
// Input: n=3
// 1 2 3
// 4 5 6
// 7 8 9
// Output: 7ta


// #include <stdio.h>

// int main() 
// {
//     int n=3, m=3;
//     int A[3][3] = {7,22,3,4,10,6,11,8,1};
//     printf("Input:\n");
//     for(int i=0; i<n; i++) 
//     {
//         for(int j=0; j<m; j++)
//         {
//             printf("%i ",A[i][j]);
//         }
//         printf("\n");
        
//     }
//     printf("Output: ");
//     int max=A[0][0], min=A[0][0];
//     int imin=0, imax=0;
//     int hisob=0;
//     for(int i=0; i<n; i++) 
//     {
//         for (int j=0; j<m; j++) 
//         {
//             hisob++;
//             if(A[i][j]<min){
//             min=A[i][j]; imin=hisob-1;}
//             if(A[i][j]>max){
//             max=A[i][j]; imax=hisob-1;}
//         }
//     }
//     int count=0, count2=0;
    
//     for(int i=imax+1; i<imin; i++)
//     {
//         count++;
//     }
//     for(int i=imin+1; i<imax; i++)
//     {
//         count2++;
//     }
//     if(count>0)
//     {
//         printf("%i ",count);
//     }
//     else
//     {
//         printf("%i ta",count2);
//     }
//     return 0;
// }


// 8) Ikki o'lchovli seriya berilgan. Ushbu seriyadagi maxgacha nechta element borligini aniqlang.
// Input: n=3
// 1 2 3
// 4 5 6
// 7 8 9
// Output: 8ta



// #include <stdio.h>
// int main()
// { 
//     int n=3;
//     char A[3][3]={{1,2,3},{4,5,6},{7,8,9}};
//     int max=A[0][0];
//     int count=0,imax=0;
//     for(int i=0; i<n; i++)
//     {
//         for(int j=0; j<n; j++)
//         {
//             if(A[i][j]>max)
//             {   
//                 count++;
//                 max=A[i][j];
//                 imax=count;
//             }
//         }
//     }
//     printf("Output %i ta",imax);
//     return 0;
// }
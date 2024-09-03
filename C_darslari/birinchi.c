// #include <stdio.h>
// int maxsimum(int a, int b){
// if(a>b)
// { return a;}
// else
// { return b;}}
// int main()
// {
//     printf("Ikkita sonni kiriting: "); scanf("%i%i",&son1,&son2);
//     int son1, son2;
//     printf("%i,%i SHU IKKI SONLAR ICHIDA KATTASI %i",son1,son2,m); 
//     int m=maxsimum(son1,son2);
// }
//     return 0;
  


// #include <stdio.h>
// int maxsimum(int a, int b)
// {
//   return a>b ? a : b;
// }
//   int main()
//   {
//       int son1, son2,son3,son4;
//       printf("Sonlarni kiriting:  "); scanf("%i%i%i%i",&son1,&son2,&son3,&son4);
//       printf("Kiritilgan sonlarning kattasi: ");
//       int m=maxsimum(maxsimum(son1,son2),maxsimum(son3,son4));
//       printf("%i ",m);
//       return 0;
//   }




// #include <stdio.h>
// int maximum(int a,int b)
// {
//   return a>b ? a : b;
// }
// float bolish(int a, int b)
// {
//   return (float) a/b;
// }
// int main()
// {
//   int son1, son2;
//   printf("Ikkita sonni kiriting: "); scanf("%i%i",&son1,&son2);
//   printf("Javoblar: ");
//   printf("\n%i",maximum(son1,son2));
//   printf("\n%f",bolish(son1,son2));
//   return 0;
// }



// #include <stdio.h>
// int main()
// {
//   int a=10, b=3;
//   double m=(double)a/b;
//   printf("%e\n",m);
//   float n=(float)a/b;
//   printf("%f",n);
//   return 0;
// }



// #include <stdio.h>
// int main()
// {
//   int son, hisob=1;
//   printf("Sonni kiriting: "); 
//   scanf("%i",&son);

//   for(int i=2; i*i<=son; i++)
//   {
//       if(son%i==0)
//       {
//         hisob=0;
//         break;
//       }
//   }

//   if(hisob==1)
//   {
//     printf("Tub son:");
//   }
//   else
//   {
//     printf("Son tub emas:");
//   }
//   return 0;
// }



// #include <stdio.h>
// int main()
// {
//   int n,m;
//   printf("Boshlanish="); scanf("%i",&n);
//   printf("Tugashi="); scanf("%i",&m);
//   printf("\n%i dan %i gacha bo'lgan tub sonlar:\n\n",n,m);
//   for(int j=n; j<=m; j++)
//   {        
//     int  hisob=1; 
//     for(int i=2; i*i<=j; i++)
//         {
//             if(j%i==0)
//             {
//               hisob=0;
//               break;
//             }
//         }       
//         if(hisob==1)
//         {
//           printf("%i ",j);
//         }
//  } 
//   printf("\n");                                
//   return 0;
// }
// #include <stdio.h>

// int main() {
//     for (int j = 10; j <= 100; j++) {
//         int prime = 1; 
//         for (int i = 2; i * i <= j; i++) {
//             if (j % i == 0) {
//                 prime = 0;
//                 break;
//             }
//         }
//         if (prime == 1) {
//             printf("%d ", j);
//         }
//     }
//     return 0;
// }



// #include<stdio.h>
// int main()
// {
//   int son,hisob=1;
//   printf("Sonni kiriting: "); scanf("%i",&son);
//   for(int i=2;i<=son; i++)
//   {
//     for(int j=i; j*j<=son; j++)
//     {
//       if(son%j==0)
//       {
//         hisob=0;
//         break;
//       }
//       else if(hisob==1)
//       {printf("%i ",j);}
//     }
//     printf("\n");
//   }
//   return 0;
// }


// #include <stdio.h>
// int main()
// {
//   for(int i=1; i<=4; i++)
//   {
//     if(i==1)
//     {
//       printf("      *              *  *  *  *");
//     }
//     else if(i==2)
//     {
//       printf("    *   *            *        *");
//     }
//     else if(i==3)
//     {
//       printf("  *       *          *        *");
//     }
//     else if(i==4)
//     {
//       printf("*   *   *   *        *  *  *  *");
//     }
//     printf("\n");
//   }
//   return 0;
// }


// #include <stdio.h>
// int main()
// {
//   int son;
//   printf("Sonni kiriting: "); scanf("%i",&son);
//   while(son!=0)
//   {
//     printf("%i ",son%10);
//     son/=10;
//   }
//   printf("\n");
//   return 0;
// }



// #include <stdio.h>
// int main(){
//   int son;
//   printf("Sonni kiriting: "); 
//   scanf("%i",&son);
//   if(son%2==0)
//   {
//     for(int i=0; i<=son; i+=2)
//     {
//       printf("%i ",i);
//     }
//   }
//   else
//   {
//     for(int i=0; i<=son; i+=2)
//     {
//       printf("%i ",i);
//     }
//     printf("\n");
//   }
//   return 0;
// }



// #include <stdio.h>
// int main()
// {
//     //int count=0;
//     for(int i=100; i<=1000; i++)
//      {   
//         if(i>0)
//         {
//            if(i%10==5)
//            {
//                 printf("%i ",i);
//            }
//            else if(i%100==5)
//            {
//                printf("%i ",i);
//            }
//            else if(i/100==5)
//            {
//             printf("%i ",i);
//            }
//         }
//      }
//     return 0;
// }



// #include <stdio.h>
// int main()
// {
//     int n=3;
//     int A[3][3] = {1,2,3,4,5,6,7,8,9};
//     for(int i=0; i<n; i++)
//     {
//         printf("%i ",A[i][n-1-i]);
//     }

    
//     return 0;
// }


// #include <stdio.h>
// #include <string.h>
// int main()
// {
//     char myList[100] = {1,3,4,6,7,8,10,12,23,45,56,78,99};
//     int javob=23;
//     int count=0;
//     if(javob==)
//     if(count==0)
//     {
//         printf("None");
//     }
        
//     return 0;
// }


// #include <stdio.h>

// int main() {
//   int n = 5;

//   for (int i = 1; i <= n; i++) {
    
//     for (int j = i; j < n; j++) {
//       printf(" ");
//     }

//     for (int k = 1; k <= 2 * i-1; k++) {
//       if (k == 1 || k == 2 * i-1 || i == n) {
//         printf("*");
//       } else {
//         printf(" ");
//       }
//     }

//     printf("\n");
//   }

//   return 0;
// }


// #include <stdio.h>
// int main()
// {
//    for(int i=2; i<10; i++)
//    {
//         for(int j=2; j<10; j++)
//         {
//             printf("%i * %i = %i\n",i,j,i*j);
//         }
//         printf("\n");
//    }
//     return 0;
// }






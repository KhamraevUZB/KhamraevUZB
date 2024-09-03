// Uyga vazifa:
// 1) 10talik uzunlikdagi int seriya elementlari orasida ikkinchi eng kichik qiymatni aniqlovchi dastur tuzing.
// Input: A[]={1,2,3,4,5,6,7,8,9,10}
// Output: second_min=2

// #include <stdio.h>

// int main() 
// {
//     int A[] = {5, 1, 91, 2, 59, 3, 45, 18};
//     int B = sizeof(A) / sizeof(A[0]);
    
//     for (int i = 0; i < B; i++) 
//     {
//         for (int j = i + 1; j < B; j++) 
//         {
//             if (A[i] > A[j]) 
//             {
//                 int max = A[i];
//                     A[i] = A[j];
//                     A[j] = max;
//             }
//         }
//     }
    
//     printf("%d\n", A[1]);
    
//     return 0;
// }



// 2) n ta butun sondan iborat int seriya berilgan va maxdan 
//(maxni o'zi inobatga olinmasin) keyin nechta son borligini aniqlaydigan dastur tuzing.
// Input: n=5 A[5]={2,9,3,-4,5}
// Output: maxdan keyin 3ta son bor


// #include <stdio.h>
// int main() 
// {
//     int A[10] = {5, -4, 1, -7, 91, -2, 59, -3, 45, -18};
//     int max=A[0];
//     int count=0,count1=0;
//     for (int i = 1; i < 10; i++) 
//     {  
//         if(A[i]>max)
//         {
//             max=A[i];
//         }
//     }
//     for(int i=0; i<10; i++)
//     {
//         if(A[i]==max)
//         {
//             count=1;
//         }
//         else if(count)
//         {
//             count1++;
//         }  
//     }
//     printf("%i",count1);
    
    
//     return 0;
// }



// 3) n ta butun sondan iborat int seriya berilgan va ulardagi max va min 
// qiymatlar(max va min inobatga olinmasin) orasida nechta son borligini 
// aniqlaydigan dastur tuzing.
// Input: n=5 A[5]={2,9,3,-4,5}
// Output: max va min orasida 1ta son bor


// #include <stdio.h>
// int main() {
//     int n=5, A[5]={28,9,3,4,-5};
//     int max=A[0], min=A[0];
//     int count_max_min=0,max1=0,min1=0;
//     for(int i=1; i<n; i++) 
//     {
//         if(A[i]>max)
//         {
//             max=A[i];
//         }
//         if(A[i]<min) 
//         {
//             min=A[i];
//         }
//     }
//     for (int i=0; i<n; i++) 
//     {
//         if(A[i]==max) 
//         {
//             max1=1;
//         } 
//         else if(A[i]==min) 
//         {
//             min1=1;
//         } 
//         else if(max1 && !min1) 
//         {
//             count_max_min++;
//         }
//     }
//     printf("%d", count_max_min);
//     return 0;
// }


// 4) n ta butun sondan iborat int seriya berilgan 
//va undagi max va min elementlarini almashtiring.
// Input: n=5 A[5]={2,9,3,-4,5}
// Output: A[5]={2,-4,3,9,5}


// #include <stdio.h>
// int main()
// {
//     int n=5, A[5]={-7,3,5,4,9};
//     int max=A[0],min=A[0], temp;
//     int MAX=0, MIN=0;
//      for(int i=1; i<n; i++) 
//     {
//         if(A[i]>max)
//         {
//             max=A[i];
//             MAX=i;
//         }
//         if(A[i]<min) 
//         {
//             min=A[i];
//             MIN=i;
//         }
//     }
//     temp=A[MAX];
//     A[MAX]=A[MIN];
//     A[MIN]=temp;
//     for(int i=0; i<n; i++)
//     {
//         printf("%i ",A[i]);
//     }
// }   



// 5) n ta sondan iborat int seriyani 1dan 10gacha random sonlar bilan 
// to'ldiring va ushbu seriya elementlarini faqat 2 marta va undan ortiq 
// takrorlanadigan elementlarini chiqaring.
// Input: n=10 array=4 2 1 4 2 6 3 4 2 1
// Output: 1 2 4

// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>
// int main()
// {
//     srand(time(0));
//     int A[100], n, count[10]={0};
//     printf("n= "); scanf("%i",&n);
//     printf("Input: n=%i array=",n);
//     for(int i=0; i<n; i++)
//     {
//         A[i]=rand()%9+1;
//         count[A[i]]++;
//         printf("%i ",A[i]);
//     }
//     printf("\n");
//     printf("Output: ");
//     for(int i=0; i<n; i++)
//     {
//         if(count[i]>1)
//         {
//             printf("%i ",i);
//         }        
//     }

//     return 0;
// }








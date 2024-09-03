// #include <stdio.h>
// #include <stdbool.h>
// int main()
// {
//     int son=123;
//     printf("son=%i\n",son);
//     printf("Salom dasturchilar\n");
//     float fson=3.1415;
//     printf("fson=%f\n",fson);
//     printf("fson=%.3f\n",fson);
//     double dson=12e-30;
//     printf("dson=%E\n",dson);
//     char symvol='A';
//     printf("symvol=%c\n",symvol);
//     bool bson=true;
//     printf("bson=%i\n",bson);

//     return 0;
// }



// #include <stdio.h>
// #include "kutubxona.h"

// int main()
// {   
//     int son=5;
//     int s1=23, s2=536, s3=65, s4=13;
//     xona(0, 100);
//     printf("%i!=%i\n",son,fact(son));
//     salomlashuv("Ergashbek");
//     hayrlashuv("Ergashbek");
//     int max=taqqoslash(taqqoslash(s1,s2),taqqoslash(s3,s4));
//     printf("%i\n",max);
//     printf("%f",bolish(1,3));
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     int sonlar[5]={111,2,83,74,5};
//     int summ=0, kop=1;
//     for(int i=0; i<5; i++)
//     {
//         summ+=sonlar[i];
//         kop*=sonlar[i];
//     }
//     printf("%i\n",summ);
//     printf("%i",kop);
//     return 0;
// }


// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>
// int main()
// {
//     srand(time(0));
//     int num[100],n;
//     printf("Sonni kiriting: "); scanf("%i",&n);
//     for(int i=0; i<n; i++)
//     {
//         num[i]=rand()%90+10;
//         printf("%i ",num[i]);
//     }
//     printf("\n");
//     int max=num[0],min=num[0],indx=0,indx1=0;
//     for(int i=1; i<n; i++)
//     {
//         if(num[i]>max)
//         {
//             max=num[i];
//             indx=i;
//         }
//     }
//     for(int i=1; i<n; i++)
//     {
//         if(num[i]<min)
//         {min=num[i];
//         indx1=i;}
//     }
//     printf("Eng katta son %i\t",max);
//     printf("Va u %i-indexda joylashgan \n",indx);
//     printf("Eng kichik son %i\t",min);
//     printf("Va u %i-indexda joylashgan \n",indx1);
//     int temp;
//     for(int i=0; i<n; i++){
//         for(int j=i+1; j<n; j++){
//             if(num[i]>num[j]){
//                 temp=num[i];
//                 num[i]=num[j];
//                 num[j]=temp;
//             }
//         }
//     }
//     for(int i=0; i<n; i++){
//         printf("%i ",num[i]);
//     }

//     return 0;
// }





// #include <stdio.h>

// int main() {
//     int x = 10;    // Oddiy o'zgaruvchi
//     int *p = &x;   // x o'zgaruvchisining manzilini saqlovchi pointer

//     printf("x ning qiymati: %d\n", x);       // x ning asl qiymatini chiqarish
//     printf("x ning manzili: %p\n", p);       // x ning manzilini chiqarish
//     printf("p orqali ko'rsatilgan qiymat: %d\n", *p); // p orqali ko'rsatilgan qiymatni chiqarish

//     // p orqali qiymatni o'zgartiramiz
//     *p = 20;
//     printf("x ning yangi qiymati: %d\n", x); // x ning yangi qiymatini chiqarish
//     printf("%i",&p);

//     return 0;
// }




// #include <stdio.h>
// #include <string.h>
// int isPalindrome(char str[]){
//     int l=0;
//     int h=strlen(str)-1;
//     while(h>1){
//         if(str[l++]!=str[h--]){
//             return 0;
//         }
//     }
//     return 1;
// }
// int main()
// {
//     char str[100];
//     printf("So'zni kiriting: "); scanf("%s",str);
//     if(isPalindrome(str)){
//         printf("%s Palindrom\n",str);
//     }
//     else{
//         printf("%s Palindrom emas\n",str);
//     }
//     return 0;
// }


// #include <stdio.h>

// int fibonacci(int n) {
//     if (n <= 1)
//         return n;
//     else
//         return fibonacci(n - 1) + fibonacci(n - 2);
// }

// int main() {
//     int n;
//     printf("n qiymatini kiriting: ");
//     scanf("%d", &n);
    
//     printf("%d-son Fibonacci qiymati: %d\n", n, fibonacci(n));
//     return 0;
// }



#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main()
{
    char matn[100];
    printf("So'zni kiriting: "); scanf("%[^\n]s",matn);
    int n=0;
    for(int i=0; i<strlen(matn);i++){
        if(isalpha(matn[i])){
            matn[i]=toupper(matn[i]);
            n++;
        }
    }
    printf("%s\n",matn);
    printf("%i",n);
    return 0;
}
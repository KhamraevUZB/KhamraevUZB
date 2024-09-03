// #include <stdio.h>
// #define butun int
// #define bosh int main()
// bosh
// {
//     butun a, b;
//     printf("a va b sonlarini kiriting ");
//     scanf("%i%i",&a,&b);
//     printf("%i+%i=%i",a,b,a+b);
//     return 0;
// }


// #include <stdio.h>
// #include "kutubxona.h"
// int main()
// {
//     int sonlar[10]={1,-2,-3,4,-5,-6,7,8,-9,10};
//     int son;
//     sum(sonlar,10);
//     printf("son="); scanf("%i",&son);
//     printf("%i!=%i\n",son,fact(son));
//     xona(0,50);
//     return 0;
// }

// int fact(int n)
// {
//     if(n>1)
//     {return n*fact(n-1);}
//     else
//     {return 1;}
// }


// #include <stdio.h>
// int main()
// {
//     printf("Barcha 1 xonali sonlarni:\n");
//     for(int i=0;i<10;i++)
//     {
//         printf("%i ",i);
//     }
//     printf("\nBarcha ikki xonali sonlar:\n");
//     for(int i=10;i<100;i++)
//     {
//         printf("%i ",i);
//     }
//     printf("\nBarcha uch xonali sonlarni kiriting:\n");
//     for(int i=100;i<1000; i++)
//     {
//         printf("%i ",i);
//     }
// }



// #include <stdio.h>
// void xona(int a, int b)
// {
//     for(int i=a; i<b; i++)
//     {
//         printf("%i ",i);
//     }
//     printf("\n");
// }
// int main()
// {
//     printf("Barcha bir xonali sonlar: \n");
//     xona(0,10);
//     printf("Barcha ikki xonali sonlar:\n");
//     xona(10,100);
//     printf("Barcha uch xonali sonlar:\n");
//     xona(100,1000);
//     return 0;
// }

//void  QIYMAT QAYTARMAYDIGAN FUNKSIYALAR

// #include <stdio.h>
// void salomlashish(char ism[])
// {
//     printf("Assalomu alaykum %s\n",ism);
// }
// void hayrlashish(char ism[])
// {
//     printf("Hayr salomat bo'ling %s\n",ism);
// }
// int main()
// {
//     salomlashish("Anvar");
//     hayrlashish("Anvar");
//     return 0;
// }

//QIYMAT QAYTARADIGAN FUNKSIYALAR
// #include <stdio.h>
// #include <stdbool.h>
// int maximum(int a, int b)
// {
//     if (a>b)
//     {return true;}
//     else 
//     {return false;}
// }
// int main()
// {
//     int son1=9, son2=6;
//     printf("%i ",maximum(son1,son2));
// }


// #include <stdio.h>
// int main()
// {
//     float son1;
//     int son;
//     printf("Haqiqiy sonni kiriting: ");scanf("%f",&son1);
//     printf("Butun sonni kiriting: ");scanf("%i",&son);
//     printf("%f ",son1^son);
//     return 0;
// }
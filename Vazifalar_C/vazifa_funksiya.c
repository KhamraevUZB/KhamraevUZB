// 1 savolning javobi.
// #include <stdio.h>
// int f(int a, int b, int c)
// {
//     if(a>b && a<c || a>c && a<b)
//     {
//         printf("Uchta sonni ichida %i o'rtacha ",a);
//     }
//     else if(b<c && b>a||b<a && b>c)
//     {
//         printf("Uchta sonni ichida %i o'rtacha ",b);
//     }
//     else
//     {
//         printf("Uchta sonni ichida %i o'rtacha ",c);
//     }
// }
// int main()
// {
//     int m, n, l;
//     printf("Uchta sonni kiriting: "); scanf("%i%i%i",&m,&n,&l);
//     f(m,n,l);
//     return 0;
// }


//2) Funksiya parametri sifatida ikki xonali butun son va char 
//seriyasi berilgan. Agar ushbu ikki xonali son char seriyasidagi
// so'z ko'rinishiga teng bo'lsa 1ni qaytaradigan, aks holda esa
// 0ni qaytaradigan funksiya tuzing.
// Input: funct(20,"yigirma")
// Output: 1
// Input: funct(30,"yigirma")
// Output: 0


// #include <stdio.h>
// #include <string.h>
// int funct(int number, const char *char_series) 
// {
//     char *number_words[] =
//     {
//         "nol", "bir", "ikki", "uch", "to'rt", "besh", "olti", "tetti", "sakkiz", "to'qqiz",
//         "o'n", "o'n bir", "o'n ikki", "o'n uch", "o'n to'rt", "o'n besh", "o'n olti",
//         "o'n yetti", "o'n sakkiz", "o'n to'qqiz", "yigirma", "yigirma bir", "yigirma ikki","yigirma uch", "yigirma to'rt",
//         "yigirma besh", "yigirma olti", "yigirma yetti", "yigirma sakkiz", "yigirma to'qqiz", "o'ttiz"
//     };
//     int i;
//     for (i = 0; i < 100; i++) 
//     {
//         if (number == i && strcmp(char_series, number_words[i]) == 0) 
//         {
//             return 1;
//         }
//     }
//     return 0;
// }
// int main() {
//     printf("%d\n", funct(20, "yigirma"));
//     printf("%d\n", funct(30, "yigirma"));
//     return 0;
// }

// 3) Funksiya parametri sifatida int seriya va butun son N (seriya uzunligi) berilgan.
// Ushbu seriyaning ikkinchi manfiy va to'rtinchi manfiy elementlar orasidagi sonlar yig'indisini qaytaradigan funksiya tuzing.
// Input: n=10 array=1 -2 3 -4 5 -6 7 -8 9 -10
// Output: 6(ya'ni, 5-6+7=6)





// 4) Funksiya parametri sifatida butun son kiritiladi va ushbu sonning raqamlar yig'indisi juft bo'lsa true qaytaradigan va toq bo'lsa false qaytaradigan funksiya tuzing.
// Input: f(1234)
// Output: true
// Input: f(456)
// Output: false


// #include <stdio.h>
// int nom(int a)
// { 
//     int count=0;
//     while(a!=0)
//     {
//         a%=10;
//         count+=a;
//         a/=10;
//     }
//     if(count%2==0)
//     {
//         return 1;
//     }
//     else
//     {
//         return 0;
//     }
// }
// int main()
// {
//     int son=1234;
//     printf("%i",nom(son));
//     return 0;
// }



// 5) Funksiya parametri sifatida haqiqiy son va butun son berilgan. Ushbu haqiqiy sonni butun son darajasini topadigan funksiya tuzing.
// Input: f(1.1 , 2)
// Output: 1.21
// Input: f(0.5 , 4)
// Output: 0.0625


// #include <stdio.h>
// #include <math.h>
// double funk(double son, int son2) 
// {
//     return pow(son, son2);
// }
// int main() {
//     double son = 1.1;
//     int son2 = 2;
//     printf("Output: %.2lf\n", funk(son, son2));
//     return 0;
// }
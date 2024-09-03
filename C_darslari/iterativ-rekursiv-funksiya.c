// 6-mavzu: Rekursiv va iterativ funksiya

// Uyga vazifa:
// 1) Matritsa sonlarini zinapoya ko'rinishida chiqarib beruvchi funksiya tuzing.
// Input: n=4
// Output:
// 1 1 1 1 1 1 1
// 1 2 2 2 2 2 1
// 1 2 3 3 3 2 1
// 1 2 3 4 3 2 1
// 1 2 3 3 3 2 1
// 1 2 2 2 2 2 1
// 1 1 1 1 1 1 1


// #include <stdio.h>
// int main()
// {
//     int A[100][100];
//     int n=4 ,m=0;
//     for(int i=0; i<n+n-1; i++)
//     {
//         for(int j=0; j<n+n-1; j++)
//         {
//             if(i ==0 || j == 0 || i==n+n-2 || j==n+n-2)
//             {
//                 printf("%i ",m+1);
//             }
//             else if(i==n-n+1 || j==n-n+1 ||i==n+n-3 || j==n+n-3)
//             {
//                 printf("%i ",m+2);
//             }
//             else if(i==n-n+2 || j==n-n+2 ||i==n+n-4 || j==n+n-4)
//             {
//                 printf("%i ",m+3);
//             }
//             else
//             {
//                 printf("%i ",n);
//             }
//         }
//         printf("\n");
//     }
//     return 0;
// }






// 2) Kiruvchi ma'lumot sifatida int seriya va uning uzunligi berilgan (random sonlar bilan to'ldirsa bo'ladi). Sizning vazifangiz ushbu seriyada eng ko'p takrorlangan sonni chiqaruvchi funksiya tuzish.
// Input: sonlar[7]={1, 3, 2, 2, 2, 3, 0}
// Output: 2




// #include <stdio.h>
// void katta(int s[], int n)
// {
//     int caunt=0, caunt1=0, temp=0;
//     for(int i=0; i<n; i++)
//     {
//         for(int j=0; j<n; j++)
//         {
//             if(s[i]==s[j])
//             {
//                 caunt++;
//             }
//         }
//         if(caunt1<caunt)
//         {
//             caunt1=caunt;
//             temp=s[i];
//         }
//         caunt=0;
//     }
//     printf("%i ",temp);
// }
// int main()
// {
//     int n=7;
//     int sonlar[7]={1, 1, 1, 2, 2, 3, 0};
//     katta(sonlar,n);
// }





// 3) Kiruvchi ma'lumot sifatida int seriya va uning uzunligi berilgan(random sonlar bilan to'ldirsa bo'ladi). Sizning vazifangiz ushbu seriyadagi ikkita sonning eng katta qiymatli ko'paytmasini chiqaruvchi funksiya tuzish.
// Input: sonlar[6]={1, 3, 2, 2, 3, 0}
// Output: 9



// #include <stdio.h>
// void kopaytma(int A[], int n)
// {
//     int m=A[0];
//     for(int i=1; i<n; i++)
//     {
//         if(m<A[i])
//         {
//             m=A[i];
//         }
//     }
//     printf("%i",m*m);
// }
// int main()
// {
//     int n=6;
//     int sonlar[6]={1, 3, 2, 7, 3, 0};
//     kopaytma(sonlar,n);
//     return 0;
// }



// 4) Kiruvchi ma'lumot sifatida gap berilgan va ushbu seriyadagi so'zlarni teskari tartibda chiqaruvchi funksiyani yasang.
// Input: a = "hello world salom dunyo"
// Output: "dunyo salom world hello"



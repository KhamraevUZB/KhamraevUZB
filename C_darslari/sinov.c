// // // 1-mavzu: Funksiya
// // // Uyga vazifa:
// // // 1) Funksiya parametri sifatida 3ta butun son berilgan va ushbu sonlarni eng kichik va eng katta qiymatlar orasidagi sonni chiqaruvchi funksiya tuzing.
// // // Input: func(4,3,1)
// // // Output: 3
// // // Input: func(2,0,1)
// // // Output: 1


// // // #include <stdio.h>
// // // int ortacha(int e,int r,int t)
// // // {
// // //     return e>r && e<t || e<r && e>t ? e : r>e && r<t || r<e && r>t ? r : t;
// // // }
// // // int main()
// // // {
// // //   int a, b, c;
// // //   printf("Uchta sonni kiriting: "); scanf("%i%i%i",&a,&b,&c);
// // //   int m=ortacha(a,b,c);
// // //   printf("%i",m);
// // //   return 0;
// // // }


// // // 2) Funksiya parametri sifatida ikki xonali butun son va char seriyasi berilgan. Agar ushbu ikki xonali son char seriyasidagi so'z ko'rinishiga teng bo'lsa 1ni qaytaradigan, aks holda esa 0ni qaytaradigan funksiya tuzing.
// // // Input: funct(20,"yigirma")
// // // Output: 1
// // // Input: funct(30,"yigirma")
// // // Output: 0



// // #include <stdio.h>

// // int main(){
// //     int a=20;
// //     long char ch[];
// //     printf("Yigirma sozini yozing:"); scanf("%c",&ch);
   
// //     if(ch=='yigirma'){
// //         printf("1");
// //     }
// //     else{
// //         printf("0");
// //     }

// //     return 0;
// // }




// // #include <stdio.h>
// // int main()
// // {
// //     int i=100;
// //     while(i<=1000)
// //      {  
// //         for(int son=i; son!=0; son/=10)
// //         {
// //            if(son%10==5)
// //             {
// //                 printf("%i ",i);
// //             }
// //         }
// //         i++;
// //     }
// //     return 0;
// // }




// #include <stdio.h>

// int main() {
//     int son;
    
//     printf("100 dan 1000 gacha bo'lgan sonlar ichidan 5 raqami ishtirok etgan sonlar:\n");
    
//     for(son = 100; son <= 1000; son++) {
//         int a = son; 
//         while(a > 0) {
//             if(a % 10 == 5) {
//                 printf("%d ", son);
//                 break;
//             }
//             a /= 10; 
//         }
//     }
    
//     return 0;
// }



// #include <stdio.h>
// #include <stdbool.h>
// int main()
// {
//     int a,b;
//     printf("a va b ni kiriting: "); scanf("%i%i",&a,&b);
//     int result = a<b;
//     if(result)
//     {
//         printf("%i",result);
//     }
//     else
//     {
//         printf("%i",result);
//     }
    
    
// }



#include <stdio.h>
int main()
{
    int son, hisob=16;
    printf("s="); scanf("%i",&son);
    for(int i=2; i<son; i++)
    {
        if(son%i==0)
        {
            hisob=7;
    
        }
    }
    if(hisob==16)
    {
        printf("tub son");
    }
    else
    {
        printf("tub emas");
    }
    return 0;
}
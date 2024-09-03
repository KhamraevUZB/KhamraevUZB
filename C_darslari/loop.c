// #include <stdio.h>
//1) Istalgan xonali sonning raqamlarini teskari tartibda chiqarib beruvchi dastur tuzing
//(ham while, ham do while da ishlashi kerak).

// int main()
// {   int son;
//     printf("Istalgan xonali sonni kiriting:");
//     scanf("%i",&son);
//     while(son>=0)
//     {
//         printf("%i ",son);
//         son--;
//     }
//     return 0;
// }



// 2) Istalgan xonali sonning raqamlarini to'g'ri tartibda chiqarib beruvchi dastur tuzing
// (ham while, ham do while da ishlashi kerak)



// #include <stdio.h>
// int main()
// {
//     int son, boshqa, sikl;
//     int yiguvchi=0;
//     int digits[10];
//     printf("Istalgan xonali sonni kiritang: ");
//     scanf("%i",&son);
//     printf("OUTPUT; ");
//     if(son==0){
//         printf("0");
//     }else{
//         sikl=son;
    
//         do{
//             boshqa=sikl%10;
//             digits[yiguvchi]=boshqa;
//             yiguvchi++;
//             sikl/=10;
//         }while(sikl!=0);
//         while(yiguvchi>0)
//         {
//             yiguvchi--;
//             printf("%i ",digits[yiguvchi]);
//         }
//     }
//     return 0;
// }



// 3) For orqali barcha ikki xonali sonlar orasida tub sonlarni chiqaruvchi dastur tuzing.



// #include <stdio.h>
// int main()
// {
//   for(int j=10; j<=77; j++)
//   {        
//       int  hisob=1; 
//       for(int i=2; i*i<=j; i++)
//           {
//               if(j%i==0)
//               {
//                 hisob=0;
//                 break;
//               }
//           }       
//           if(hisob==1)
//           {
//             printf("%i ",j);
//           }
//   }
//   return 0;
// }


// 4) For orqali 1dan n gacha sonlar orasida juftlarni kamayish tartibida chiqaring.



// #include <stdio.h>
// int main()
// {
//     int son;
//     printf("Sonni kiriting: "); scanf("%i",&son);
//     for(int i=son; i>=0; i--)
//     {
//         if(i%2==0)
//         {
//             printf("%i ",i);
//         }
//     }
//     return 0;
// }


// 5) For orqali 1dan n gacha sonlar orasida toqlarni o’sish tartibida chiqaring.



// #include <stdio.h>
// int main()
// {
//     int son;
//     printf("Sonni kiriting: "); scanf("%i",&son);
//     printf("Toqlar ");
//     for(int i=1; i<=son; i+=2)
//     {
//         printf("%i ",i);
//     }
//     return 0;
// }




// 6) Barcha uch xonali sonlar orasidagi raqamlari 2 marta takrorlanadigan sonlarni chiqaruvchi dastur tuzing.


// Buni bajara olmadim


// 7) Uchburchak va to’rtburchakni quyidagi ko’rinishda chiqaring:
//        *                       *  *  *  *  *
//       * *                     *             *
//      *   *                    *             *
//     *     *                   *             *
//    *       *                  *             *
//   * * * * *                  *  *  *  *  *

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

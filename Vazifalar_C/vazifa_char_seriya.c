// Uyga vazifa:
// 1) char seriyadagi ishlatiladigan funksiyalardan foydalanib, ismingizning 1-yarmini familiyangizning 2-yarmiga almashtiring va familiyaning 1-yarmini ismingizning 2-yarmiga almashtiring.
// Input:     ism=Abdulla, fam=Abdullayev 
// Output:  ism=layevlla, fam=llalayev

// #include <stdio.h>
// // #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text1[20]=" Abdulla",text2[20]=" Abdullayev";
//     printf("Input:\t");
//     printf("Ism =%s\t",text1);
//     printf("Fam =%s\n",text2);
//     printf("Output:\t");
//     strncpy(text1,text2+6,5);
//     printf("Ism = %s\t",text1);
//     strcpy(text2,text1);
//     strcpy(text2,text2+5);
//     strncpy(text2+3,text1,5);
//     printf("Fam = %s\n",text2);
//     return 0;
// }




// 2) gap nomli char seriyasini va ushbu seriyadan gap hosil qiling. Ya'ni 1-chi harf katta bilan boshlanishi kerak va gapni oxiri nuqta bilan tugashi kerak.
// Input: salom bolalar
// Output: Salom bolalar.


// #include <stdio.h>
// #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char gap[30];
//     printf("Textni kiriting: ");
//     scanf("%[^\n]s",gap);
//     int k=0;
//     for(int i=0; i<1; i++)
//     {
//         gap[i]=toupper(gap[i]);
//     }
//     printf("%s.",gap);
//     return 0;
// }


// 3) char seriyasini scanf orqali kiriting va ushbu kiritilgan char seriyada har bir belgi nechi marta ishtirok etganligini aniqlang.
// Input: text[]="SalomBolalar"
// Output: 
// 'S' 1ta, 'a' 3ta, 'l' 3ta, 'o' 2ta, 'm' 1ta, 'B' 1ta, 'r' 1ta


// #include <stdio.h>
// #include <string.h>

// int main() {
//     char text[100];
//     printf("Iltimos, satrni kiriting: ");
//     scanf("%s", text);

//     int len = strlen(text);

//     // Har bir harfning necha marta ishtirok etganligini hisoblash uchun char jadvallarni ishlatamiz
//     int harflar[256] = {0};

//     // Har bir belgi uchun ishtirok etish sanagini hisoblaymiz
//     for (int i = 0; i < len; i++) {
//         harflar[text[i]]++;
//     }

//     // Natijalarni chiqarish
//     for (int i = 0; i < len; i++) {
//         if (harflar[text[i]] != 0) {
//             printf("'%c' %dta, ", text[i], harflar[text[i]]);
//             // Belgi o'zgarib ketish uchun ishlatilgan sanani nolga tenglash
//             harflar[text[i]] = 0;
//         }
//     }

//     return 0;
// }



// 4) char seriyasi berilgan va ushbu char seriyasidagi so'zlarni chiqaruvchi dastur tuzing.
// Input: matn[]="This is a book. It is very intresting!"
// Output:
// This
// is
// a
// book
// It
// is
// very
// intresting


// #include <stdio.h>
// #include <string.h>
// int main()
// {
//     char matn[]="This is a book. It is very intresting!";
//     int len=strlen(matn);
//     for(int i=0; i<len; i++)
//     {
//         if(matn[i]==' ')
//         {
//             printf("\n");
//         }
//         printf("%c",matn[i]);
//     }

//     return 0;
// }



// 5) scanf orqali textni faqat kichik lotin harflar bilan kiriting. Agar kiritilgan harflar Tab qatoridagi harflarga to'g'ri keladigan bo'lsa "Tab" so'zini xotiraga joylashtiring yoki Shift qatoridagi harflarga to'g'ri keladigan bo'lsa "Shift" so'zini xotiraga joylashtiring yoki CapsLock qatoridagi harflarga to'g'ri keladigan bo'lsa "CapsLock" so'zini xotiraga joylashtiring va natijani chiqaring.(qo'shimcha char seriyasi ishlatsa bo'ladi)
// Input: text[]="qazplm"
// Output: text1[]="TabCapsLockShiftTabCapsLockShift"


// #include <stdio.h>
// #include <string.h>
// int main()
// {
//     char text[100];
//     int len=strlen(text);
//     printf("Textni kiriting: "); scanf("%s",text);
//     for(int i=0; i<len; i++)
//     {
//         if(text[i]=='q' || text[i]=='w' || text[i]=='e' || text[i]=='r'|| text[i]=='t' || text[i]=='y' || text[i]=='u' || text[i]=='i' || text[i]=='o' || text[i]=='p')
//         {printf("Tab");}
//         else if(text[i]=='a' || text[i]=='s' || text[i]=='d' || text[i]=='f' || text[i]=='g' || text[i]=='h' || text[i]=='j' || text[i]=='k' || text[i]=='l')
//         {printf("CapsLock");}
//         else
//         {printf("Shift");}
//     }
//     return 0;
// }



// 7) char seriyani scanf orqali kiriting va harf, raqam va probellardan boshqa belgilar soni nechtaligini aniqlang.
// Input: text[]="qwerty @#$%Hello world%^&"
// Output: spets belgilar soni: 7ta



// #include <stdio.h>
// #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text[30];
//     printf("Textni kiriting: ");
//     scanf("%[^\n]s",text);
//     //puts(text);
//     int k=0;
//     for(int i=0; i<strlen(text); i++)
//     {
//         if(ispunct(text[i]))
//         {
//             k++;
//         }
//     }
//     printf("Textda %i ta maxsus belgilar mavjud",k);
//     return 0;
// }

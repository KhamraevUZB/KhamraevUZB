 //[^\n]   probellarni hisobga olish
 //<string.h> kutubhonasi char seriya bn ishlovchi kutubhona va strlen satrlarni uzunligini o'lchovchi funksiya
 //satrlarni solishtirish funksiyasi strcmp va 2 satr teng bo'lsa 0 ni if birinchisi ikkinchisidan katta bo'lsa  1 va birinchisi kichik bo'lsa -1 ni va ikkisida uzunlik bo'yicha farq bo'lsa harflar sonini korsatadi
 //strcpy satrlarni nusxalash  funksiyasi q1,q2+2 ikkinchi indexdan nusxalashni boshlaydi if q1+2,q2 desak ikkinchi indexga nusxa bo'shlanadi
 //strncpy soniga qarab nusxa oladi yani nechta indexni nusxalash kerakligini beramiz q1,q2,2
 //strcat funksiyasi birinchi satr oxiriga ikkinchi satrni qo'shadi \n ni oraliqda qoldirmaydi
 //ctype.h kutubhonasi
 //isalnum Barcha lotin harflari va raqamlarni tekshirish
 //int isalpha barcha lotin harflarini tekshirish katta kichikmi farqi yoq faqat lotin xarflarini
 //int isdigit raqamlarni tekshirish (0,9)
 //int islower kichik lotin harflarini tekshirish
 //int ispunct maxsus belgilarn tekshirish
 //int isspace ajratish belgilarni tekshirish
 //int isupper katta lotin harflarini tekshirish
 //int tolower katta lotin harflarni kichigiga almashtirish
 //int toupper kichik lotin xarflarni kattasiga alishtirish


//ctype.h kutubxonasidagi funcsiyalar

// #include <stdio.h>
// #include <string.h>
// int main()
// {
//    /* char text[10]="Salom";//'\0'-qator yakuni (oxiri)
//     printf("text=%s",text);
//     int n=strlen(text);
//     printf("Size of text=%i\n",n);
//     for(int i=0; i<10; i++)
//     {
//         //if(text[i]=='\0') //tekshirish \0 ni
//         //{puts("teskari slesh nol");}
//         printf("%c ",text[i]);
//     }*/
//     char matn[30];
//     printf("MATINNI KIRITING: ");
//     scanf("%[^\n]s",matn);
//     printf("Matn=%s\n",matn);
//     return 0;
// }

// nechta harf borligini bilish


// #include <stdio.h>
// #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text[30];
//     printf("Textni kiriting: ");
//     scanf("%[^\n]s",text);
//     puts(text);
//     int k=0;
//     for(int i=0; i<strlen(text); i++)
//     {
//         if(isalpha(text[i]))
//         {
//             k++;
//         }
//     }
//     printf("Textda %i ta lotin harfi mavjud",k);
//     return 0;
// }



//raqamlarni tekshirish

// #include <stdio.h>
// #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text[30];
//     printf("Textni kiriting: ");
//     scanf("%[^\n]s",text);
//     puts(text);
//     int k=0;
//     for(int i=0; i<strlen(text); i++)
//     {
//         if(isdigit(text[i]))
//         {
//             k++;
//         }
//     }
//     printf("Textda %i ta raqam mavjud",k);
//     return 0;
// }

//xam raqam xam harflarni teksirish isalnum

// #include <stdio.h>
// #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text[30];
//     printf("Textni kiriting: ");
//     scanf("%[^\n]s",text);
//     puts(text);
//     int k=0;
//     for(int i=0; i<strlen(text); i++)
//     {
//         if(isalnum(text[i]))
//         {
//             k++;
//         }
//     }
//     printf("Textda %i ta raqam va lotin harfi mavjud",k);
//     return 0;
// }



//katta lotin harfini isupper

// #include <stdio.h>
// #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text[30];
//     printf("Textni kiriting: ");
//     scanf("%[^\n]s",text);
//     puts(text);
//     int k=0;
//     for(int i=0; i<strlen(text); i++)
//     {
//         if(isupper(text[i]))
//         {
//             k++;
//         }
//     }
//     printf("Textda %i ta lotin katta harfi mavjud",k);
//     return 0;
// }


// kichik harflarni tekshiradi islower


// #include <stdio.h>
// #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text[30];
//     printf("Textni kiriting: ");
//     scanf("%[^\n]s",text);
//     puts(text);
//     int k=0;
//     for(int i=0; i<strlen(text); i++)
//     {
//         if(islower(text[i]))
//         {
//             k++;
//         }
//     }
//     printf("Textda %i ta lotin kichik harfi mavjud",k);
//     return 0;
// }

//hotirada harflarni kichikdan kattaga almashtirish
//toupper kichikdan katta qilish
//tolower katta harfni kichikka alishtirish xotirada
//if puts ni o'rniga forni ichiga printf yozilsa va %c quyilsa xotirada almashmaydi


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
//         text[i]=tolower(text[i]);
//     }
//     puts(text);
//     return 0;
// }

//probellarni sanash isspace

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
//         if(isspace(text[i]))
//         {
//             k++;
//         }
//     }
//     printf("Textda %i ta ajratuvchi belgilar mavjud",k);
//     return 0;
// }

//maxsus belgilarni tekshirish ispunct

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
//         if(isspace(text[i]))
//         {
//             k++;
//         }
//     }
//     printf("Textda %i ta ajratuvchi belgilar mavjud",k);
//     return 0;
// }

//string.h kutubhonasi amallari


// #include <stdio.h>
// // #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text1[20]="abcdef",text2[20]="012345";
//     strcpy(text1,text2);
//     puts(text1);
//     puts(text2);
//     return 0;
// }


// #include <stdio.h>
// // #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text1[20]="abcdef",text2[20]="012345";
//     strcpy(text1,text2+2);
//     puts(text1);
//     puts(text2);
//     return 0;
// }


// #include <stdio.h>
// // #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text1[20]="abcdef",text2[20]="012345";
//     strcpy(text1+2,text2);
//     puts(text1);
//     puts(text2);
//     return 0;
// }



// #include <stdio.h>
// // #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text1[20]="abcdef",text2[20]="012345";
//     strcpy(text1+2,text2+2);
//     puts(text1);
//     puts(text2);
//     return 0;
// }



// #include <stdio.h>
// // #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text1[20]="abcdef",text2[20]="012";
//     strcpy(text1+2,text2+2);
//     puts(text1);
//     puts(text2);
//     return 0;
// }


// #include <stdio.h>
// // #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text1[20]="abcdef",text2[20]="012345";
//     strncpy(text1,text2,2);
//     puts(text1);
//     puts(text2);
//     return 0;
// }


// #include <stdio.h>
// // #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text1[20]="abcdef",text2[20]="012345";
//     strcat(text2,text1);//1 va 2 ni almashtiradi
//     puts(text1);
//     puts(text2);
//     return 0;
// }


// #include <stdio.h>
// // #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text1[20]="abcdef",text2[20]="012345";
//     strcat(text2,text1);
//     puts(text1);
//     puts(text2);
//     return 0;
// }


// #include <stdio.h>
// // #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text1[20]="abcdef",text2[20]="012345";
//     strncat(text2,text1,3);
//     puts(text1);
//     puts(text2);
//     return 0;
// }

//TEXTLARNI SOLISHTIRISH


// #include <stdio.h>
// // #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text1[20]="abcd",text2[20]="abce";
//     int n=strcmp(text1,text2);
//     if(n==0)
//     {
//         puts("text1 teng text2 ga");
//     }
//     else if(n>0)
//     {
//         puts("text1>text2 dan");
//     }
//     else
//     {
//         puts("text1<text2 dan");
//     }
//     return 0;
// }


// n nimaga teng 
// #include <stdio.h>
// // #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text1[20]="abcd",text2[20]="abcd";
//     int n=strcmp(text1,text2);
//     if(n==0)
//     {
//         puts("text1 teng text2 ga");
//         printf("n=%i\n",n);
//     }
//     else if(n>0)
//     {
//         puts("text1>text2 dan");
//         printf("n=%i\n",n);
//     }
//     else
//     {
//         puts("text1<text2 dan");
//         printf("n=%i\n",n);
//     }
//     return 0;
// }


// #include <stdio.h>
// // #include <ctype.h>
// #include <string.h>
// int main()
// {
//     char text1[20]="abcd",text2[20]="dcba";
//     int n=strncmp(text1,text2,2);
//     if(n==0)
//     {
//         puts("text1 teng text2 ga");
//         printf("n=%i\n",n);
//     }
//     else if(n>0)
//     {
//         puts("text1>text2 dan");
//         printf("n=%i\n",n);
//     }
//     else
//     {
//         puts("text1<text2 dan");
//         printf("n=%i\n",n);
//     }
//     return 0;
// }


//bular text ko'rinisidagi malumotlarni birlashtirish tekshirish va nusxalash amallari




//              POINTER VA CHAR SERIYASI

// #include <stdio.h>
// #include <string.h>
// void reverse(char *s)
// {
//     int n=strlen(s);
//     char temp;
//     for(int i=0; i<n/2; i++)
//     {
//         temp=s[i];
//         s[i]=s[n-1-i];
//         s[n-1-i]=temp;
//     }
    
// }
// int main()
// {
//     char text[100];
//     printf("Textni kiriting:");
//     scanf("%[^\n]s",text);
//     printf("tect after reversing:\n");
//     reverse(text);
//     puts(text);
// }



// #include <stdio.h>
// #include <string.h>
// void kiritish(int *a)
// {
//     printf("son= ");
//     scanf("%i",a);
    
// }
// void chiqarish(int a)
// {
//     printf("son= %i\n",a);
// }
// int main()
// {
//     int son;
//     kiritish(&son);
//     chiqarish(son);
//     return 0;
// }



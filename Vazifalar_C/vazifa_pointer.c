// Uyga vazifa:
// 1) Butun toifali pointer orqali int seriyaning maksimal qiymatini toping.
//  (FAQAT POINTER(YA'NI QO'SHIMCHA O'ZGARUVCHISISIZ) VA
//   BITTA SERIYA ISHLARISH KERAK VA SERIYANING ELEMENTLARI O'ZGARMASLIGI KERAK)
// Input: A[5]={1,2,3,4,5}
// Output: 5

// #include <stdio.h>
// int main()
// {
//     int son[5]={1,2,8,4,5};
//     int *ptr;
//     ptr=son;
//     for(int i=1; i<5; i++)
//     {
//         if(son[i]>*ptr)
//         {
//             *ptr=son[i];
//         }
//     }
//     printf("%i ",*ptr);
//     return 0;
    
// }


// 2)  Haqiqiy son toifali pointer orqali float tipidagi sonning 
// butun qismini chiqaring. (FAQAT POINTER(YA'NI QO'SHIMCHA O'ZGARUVCHISISIZ) 
// VA BITTA O'ZGARUVCHI ISHLARISH KERAK)
// Input: son=12.345
// Output: 12


// #include <stdio.h>
// int main()
// {
//     float son=1888.122;
//     float *ptr;
//     *ptr=son;
//     int son1=*ptr;
//     printf("%i ",son1);
//     return 0;
// }




// 3) Butun toifali pointer orqali int seriya elementlarining 
// yig'indisini toping. (FAQAT POINTER
//  (YA'NI QO'SHIMCHA O'ZGARUVCHISISIZ) VA BITTA SERIYA 
//  ISHLARISH KERAK VA SERIYANING ELEMENTLARI O'ZGARMASLIGI KERAK)
// Input: A[5]={1,2,3,4,5}
// Output: 15


// #include <stdio.h>
// int main()
// {
//     int A[5]={1,2,3,4,5};
//     int *ptr;
//     ptr=A;
//     for(int i=1; i<5; i++)
//     {
//         *ptr+=A[i];
//     }
//     printf("%i ",*ptr);

//     return 0;
// }


 
// 4) Butun toifali pointer orqali int seriyaning birinchi va oxirgi 
// qiymatlarini almashtiring. (FAQAT POINTER(YA'NI QO'SHIMCHA O'ZGARUVCHISISIZ) 
// VA BITTA SERIYA ISHLARISH KERAK)
// Input: A[5]={1,2,3,4,5}
// Output: A[5]={5,2,3,4,1}


// #include <stdio.h>
// int main()
// {
//     int A[6]={7,2,3,4,5,3};
//     int *ptr;
//     printf("Input:  ");
//     for(int i=0; i<6; i++)
//     {printf("%i ",A[i]);}
//     printf("\nOutput: ");

//     ptr=A;
//     ptr+=5;
//     printf("%i ",*ptr);
//     ptr-=4;
//     printf("%i ",*ptr);
//     ptr++;
//     printf("%i ",*ptr);
//     ptr++;
//     printf("%i ",*ptr);
//     ptr++;
//     printf("%i ",*ptr);
//     ptr-=4;
//     printf("%i ",*ptr);
    
//     return 0;
// }


// 5) Butun toifali pointer orqali int seriyaning maksimal va minimal
//  qiymatlarini almashtiring. (FAQAT POINTER(YA'NI QO'SHIMCHA O'ZGARUVCHISISIZ) 
//  VA BITTA SERIYA ISHLARISH KERAK)
// Input: A[5]={1,2,3,4,5}
// Output: A[5]={5,2,3,4,1}



// #include <stdio.h>

// void swap(int *a, int *b) {
//     int temp = *a;
//     *a = *b;
//     *b = temp;
// }

// void max_min_swap(int *arr, int size) {
//     int *max_ptr = arr;
//     int *min_ptr = arr;
    
//     for (int i = 1; i < size; i++) {
//         if (*(arr + i) > *max_ptr) {
//             max_ptr = arr + i;
//         }
//         if (*(arr + i) < *min_ptr) {
//             min_ptr = arr + i;
//         }
//     }
    
//     swap(max_ptr, min_ptr);
// }

// int main() {
//     int A[5] = {1, 2, 3, 4, 5};
    
//     printf("Input: A[5]={");
//     for (int i = 0; i < 5; i++) {
//         printf("%d", A[i]);
//         if (i < 4) {
//             printf(",");
//         }
//     }
//     printf("}\n");
    
//     max_min_swap(A, 5);
    
//     printf("Output: A[5]={");
//     for (int i = 0; i < 5; i++) {
//         printf("%d", A[i]);
//         if (i < 4) {
//             printf(",");
//         }
//     }
//     printf("}\n");
    
//     return 0;
// }
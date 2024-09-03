// #include <stdio.h>
// int main()
// {
//     int son=15;
//     int *pson=&son;
//     printf("sonning manzili %p  sonning qiymati %i\n ", &son ,son);
//     printf("psonning manzili %p psonning qiymati %p psonning qiymatining qiymati %i ",&pson, pson, *pson);
//     return 0;
// }



// #include <stdio.h>
// int main()
// {
//     int sonlar[5]={11,22,33,44,55};
//     int *ptr;
//     ptr=sonlar; // ptr=&sonlar[0]
//     printf("ptr=%p\t*ptr=%i\n",ptr,*ptr);
//     ptr++;
//     printf("ptr=%p\t*ptr=%i\n",ptr,*ptr);
//     ptr+=4;
//     printf("ptr=%p\t*ptr=%i\n",ptr,*ptr);
//     ptr-=5;
//     printf("ptr=%p\t*ptr=%i\n",ptr,*ptr);
//     return 0;
// }





// #include <stdio.h>
// void swap(int *a,int *b)
// {
//     int c=*a;
//     *a=*b;
//     *b=c;
// }
// int main()
// {
//     int son1, son2;
//     printf("Ikkita sonni kiriting:"); 
//     scanf("%i%i",&son1,&son2);
//     printf("son1=%i\t son2=%i\n",son1,son2);
//     swap(&son1,&son2);
//     printf("son1=%i\t son2=%i\n",son1,son2);
// }
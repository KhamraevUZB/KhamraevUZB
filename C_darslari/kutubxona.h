// void sum(int A[],int n)
// {
//     int s=0;
//     for(int i=0; i<n; i++)
//     {s+=A[i];}
//     printf("SUMM=%i\n",s);
// }
// int fact(int n)
// {
//     if(n>1)
//     {return n*fact(n-1);}
//     else
//     {return 1;}
// }
// void xona(int a, int b)
// {
//     for(int i=a; i<=b; i++)
//     {
//         if(i%2==0){
//             printf("%i ",i);
//         }
//         else
//         {
//             printf("* ");
//         }
//     }
//     printf("\n");
// }
// int sum1(int n)
// {
//     if(n>0)
//     {
//         return n+sum1(n-1);
//     }
//     else
//     {return 0;}
// }
void xona(int a, int b)
{
    for(int i=a; i<=b; i++)
    {
        printf("%i ",i);
    }
    printf("\n");
}
int fact(int n)
{
    if(n>1)
    { return n*fact(n-1);}
    else
    { return 1;}
}
void salomlashuv(char ism[])
{
    printf("Assalom alaykum %s\n",ism);
}
void hayrlashuv(char ism[])
{
    printf("Hayr salomat bo'ling %s\n",ism);
}

int taqqoslash(int a, int b)
{
    return a>b ? a : b;
}
float bolish(int a, int b)
{
    return (float) a/b;
}




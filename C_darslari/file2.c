#include <stdio.h>
#include <stdlib.h>
int main()
{
    FILE *read=fopen("file","r");
    if(read==NULL)
    {
        puts("File not exists.");
        exit(1);
    }
    char str;
    while(!feof(read))
    {
        fscanf(read,"%c",&str);
        printf("%c",str);
    }
    fclose(read);
    return 0;
}
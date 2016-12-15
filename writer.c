

#include <stdio.h>
#include <stdlib.h>

typedef struct nested_s {
    int a;
    int b;
    float c;
} nested_t;


typedef struct test_s {
    int number;
    nested_t *nested;
} test_t;




int main(int argc, char *argv[]) {
    int size = 2;
    test_t *test = (test_t *)calloc(2, sizeof(test_t));

    test[0].number = 1;
    test[0].nested = (nested_t *)calloc(1, sizeof(nested_t));
    test[0].nested[0].a = 1;
    test[0].nested[0].b = 2;
    test[0].nested[0].c = 3.3f;

    test[1].number = 2;
    test[1].nested = (nested_t *)calloc(2, sizeof(nested_t));
    test[1].nested[0].a = 2;
    test[1].nested[0].b = 3;
    test[1].nested[0].c = 4.4f;

    test[1].nested[1].a = 3;
    test[1].nested[1].b = 4;
    test[1].nested[1].c = 5.4f;


    FILE *fp = fopen("./test.bin", "wb");

    printf("size: %d", size);
    fwrite(&size, sizeof(size), 1, fp);

    for(int i = 0; i < size; i++) {
        printf("out: %d\n", test[i].number);
        fwrite(&test[i].number, sizeof(int), 1, fp);
        fwrite(test[i].nested, sizeof(nested_t), test[i].number, fp);
    }

    fclose(fp);







    printf("hello\n");

    free(test[0].nested);
    free(test[1].nested);

    free(test);

}

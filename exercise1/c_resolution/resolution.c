#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double *spawn_random_vector(int size)
{
    double *vector = (double *)malloc((size) * sizeof(double));
    for (int i = 0; i <= size; i++)
    {
        vector[i] = rand() % size;
    }
    return vector;
}

double **spawn_random_matrix(int size)
{
    double **matrix = (double **)malloc((size) * sizeof(double));
    for (int i = 0; i <= size; i++)
    {
        matrix[i] = spawn_random_vector(size);
    }
    return matrix;
}

double *multiply_first_i(double **matrix, double *vector, int size)
{
    double *result_vector = (double *)malloc((size) * sizeof(double));
    for (int i = 0; i <= size; i++)
    {
        result_vector[i] = 0;
        for (int j = 0; j <= size; j++)
        {
            result_vector[i] = result_vector[i] + vector[j] * matrix[i][j];
        }
    }
    return result_vector;
}

double *multiply_first_j(double **matrix, double *vector, int size)
{
    double *result_vector = (double *)malloc((size) * sizeof(double));
    for (int j = 0; j <= size; j++)
    {
        result_vector[j] = 0;
        for (int i = 0; i <= size; i++)
        {
            result_vector[i] = result_vector[i] + vector[j] * matrix[i][j];
        }
    }
    return result_vector;
}

int main(int argc, char *argv[])
{

    srand(time(NULL));
    clock_t before, after;
    int number_of_rows = atoi(argv[1]);
    double **matrix = spawn_random_matrix(number_of_rows);
    double *vector = spawn_random_vector(number_of_rows);

    before = clock();
    double *result_vector = multiply_first_i(matrix, vector, number_of_rows);
    after = clock();
    free(result_vector);
    double difference_ij = ((double)(after - before)) / CLOCKS_PER_SEC;

    before = clock();
    result_vector = multiply_first_j(matrix, vector, number_of_rows);
    after = clock();
    free(result_vector);
    double difference_ji = ((double)(after - before)) / CLOCKS_PER_SEC;
    printf("%d,%.8f,%.8f\n", number_of_rows, difference_ij, difference_ji);
    return 0;
}
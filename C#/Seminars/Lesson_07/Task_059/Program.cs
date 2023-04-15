// Task 59
/*
Задайте двумерный массив из целых чисел. Напишите программу,
которая удалит строку и столбец, на пересечении которых расположен
наименьший элемент массива.

1 4 7 2
5 9 2 3
8 4 2 4
5 2 6 7
наименьший элемент 1

Итог
9 4 2
2 2 6
3 4 7
*/

Console.Clear();

void InputMatrix(int[,] matrix)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
            matrix[i, j] = new Random().Next(1, 10);
    }
}
void PrintMatrix(int[,] matrix)
{
    Console.WriteLine();
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
            Console.Write(matrix[i, j] + " \t");

        Console.WriteLine();
    }
}
void ReleaseMatrix(int[,] matrix)
{
    int minValue = matrix[0, 0], row = 0, column = 0;
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            if (minValue >= matrix[i, j])
            {
                minValue = matrix[i, j];
                row = i;
                column = j;
            }
        }
    }
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            if (i != row && j != column)
                Console.Write(matrix[i, j] + " \t");
        }
        Console.WriteLine();
    }
}
Console.Write("Введите кол-во строк: ");
int n = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите кол-во столбцов: ");
int m = Convert.ToInt32(Console.ReadLine());
int[,] matrix = new int[n, m];
int[] array = new int[n * m];
InputMatrix(matrix);
Console.WriteLine("Исходный двумерный массив: ");
PrintMatrix(matrix);
Console.WriteLine();
ReleaseMatrix(matrix);

// Task 55
/*
Задайте двумерный массив. Напишите программу, которая 
заменяет строки на столбцы. В случае если это не возможно, 
программа должна вывести сообщение для пользователя.
*/
Console.Clear();


void InputMatrix(int[,] matrix)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
            matrix[i, j] = new Random().Next(-10, 11);
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
    if (matrix.GetLength(0) != matrix.GetLength(1))
        Console.WriteLine("Процедура невозможна!");
    else
    {
        for (int i = 0; i < matrix.GetLength(0); i++)
        {
            for (int j = i + 1; j < matrix.GetLength(1); j++)
            {
                int x = matrix[i, j];
                matrix[i, j] = matrix[j, i];
                matrix[j, i] = x;
            }
        }
        Console.WriteLine("Конечный двумерный массив: ");
        PrintMatrix(matrix);
    }
}


Console.Write("Введите кол-во строк: ");
int n = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите кол-во столбцов: ");
int m = Convert.ToInt32(Console.ReadLine());
int[,] matrix = new int[n, m];
InputMatrix(matrix);
Console.WriteLine("Исходный двумерный массив: ");
PrintMatrix(matrix);
ReleaseMatrix(matrix);
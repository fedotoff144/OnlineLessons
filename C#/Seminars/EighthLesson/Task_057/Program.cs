// Task 57
/*
Составить частотный словарь элементов двумерного массива. 
Частотный словарь содержит информацию о том, сколько раз встречается 
элемент входных данных.
*/

Console.Clear();


void InputMatrix(int[,] matrix, int[] array)
{
    int k = 0;
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            int x = new Random().Next(1, 11);
            matrix[i, j] = x;
            array[k] = x;
            k++;
        }
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
void ReleaseMatrix(int[] array)
{
    int[] helpArray = new int[array.Length];
    for (int i = 0; i < array.Length; i++)
    {
        int count = 1;
        bool flag = true;
        foreach (int el in helpArray)
        {
            if (array[i] == el)
                flag = false;
        }
        if (flag)
        {
            for (int j = i + 1; j < array.Length; j++)
            {
                if (array[i] == array[j] && i != j)
                    count++;
            }
            Console.WriteLine($"Число {array[i]} встретилоcь {count} раз");
            helpArray[i] = array[i];
        }
    }
}


Console.Write("Введите кол-во строк: ");
int n = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите кол-во столбцов: ");
int m = Convert.ToInt32(Console.ReadLine());
int[,] matrix = new int[n, m];
int[] array = new int[n * m];
InputMatrix(matrix, array);
Console.WriteLine("Исходный двумерный массив: ");
PrintMatrix(matrix);
ReleaseMatrix(array);
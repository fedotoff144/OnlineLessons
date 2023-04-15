// Task 31

/*Задайте массив из 12 элементов, заполненный случайными числами 
из промежутка [-9, 9] .Найдите сумму отрицательных и положительных элементов чисел.
Например, в массиве [3, 9, -8, 1, 0, -7, 2, -1, 8, -3, -1, 6] 
сумма положительных чисел равна 29, а сумма отрицательных чисел равна -20.
*/

void InputArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    array[i] = new Random().Next(-9, 10);
}

void PositiveNumber(int[] array)
{
    int summa_p = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] > 0)
        summa_p += array[i];
    }
    Console.WriteLine("Сумма положительных элементов равна: " + summa_p);
}

void NegativeNumber(int[] array)
{
    int summa_n = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] < 0)
        summa_n += array[i];
    }
    Console.WriteLine("Сумма положительных элементов равна: " + summa_n);
}

int[] matrix = new int[12];
InputArray(matrix);
Console.WriteLine("[" + string.Join(", ", matrix) + "]");
PositiveNumber(matrix);
NegativeNumber(matrix);
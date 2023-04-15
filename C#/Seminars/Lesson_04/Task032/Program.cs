//Task 32
/*
Напишите программу по замене элементов массива: положительные элементы 
замените на соответствующие отрицательные, и наоборот.
*/

void InputArray(int[] array)
{
    for(int i = 0; i < array.Length; i++)
        array[i] = new Random().Next(-9, 10);
}

void ReplaceArray()
{
    int[] array = new int[12];
    InputArray(array);
    Console.WriteLine("[" + string.Join(", ", array) + "]");
    for (int i = 0; i < array.Length; i++)
        array[i] = array[i] * (-1);

    Console.WriteLine("[" + string.Join(", ", array) + "]");
}

ReplaceArray();
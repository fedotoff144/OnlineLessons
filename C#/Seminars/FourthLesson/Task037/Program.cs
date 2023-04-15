// Task 37

/*
Найдите произведение пар чисел в одномерном массиве. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
Результат запишите в новом массиве. [1 2 3 4 5] -> 5 8 3 [6 7 3 6] -> 36 21 
*/

void InputArray(int[] array) 
{ 
    for (int i = 0; i < array.Length; i++) 
    array[i] = new Random().Next(1, 15); 
} 
Console.Write("Введите кол-во элементов массива: "); 

int n = Convert.ToInt32(Console.ReadLine()); 
int[] array = new int[n]; 

InputArray(array); 
Console.WriteLine("[" + string.Join(", ", array) + "]"); 

int len_number; 
    if (n % 2 == 0) len_number = n / 2; 
    else len_number = n / 2 + 1; 

int[] result_array = new int[len_number]; 
    for (int i = 0; i < len_number; i++) 
    
result_array[i] = array[i] * array[array.Length - i - 1]; 
Console.WriteLine("[" + string.Join(", ", result_array) + "]"); 
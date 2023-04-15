// Fourth Lesson

/*
// 31 void InputArray(int[] array) 
{ 
    for (int i = 0; i < array.Length; i++) 
    array[i] = new Random().Next(-9, 10); 
} void PositiveNumber() 
{ 
    int[] array = new int[12]; 
    InputArray(array); 
    Console.WriteLine("[" + string.Join(", ", array) + "]"); 
    int summa_p = 0, summa_n = 0; 
    for (int i = 0; i < array.Length; i++) 
    { 
        if (array[i] > 0) summa_p = summa_p + array[i]; 
        else if (array[i] < 0) summa_n = summa_n + array[i]; 
    } 
    Console.WriteLine("Сумма положительных элементов равна: " + summa_p); 
    Console.WriteLine("Сумма отрицательных элементов равна: " + summa_n);
    PositiveNumber(); 
*/

void InputArray(int[] array) 
{ 
    for (int i = 0; i < array.Length; i++) 
    array[i] = new Random().Next(-9, 10);

} void ReplaceArray() 
    { 
    int[] array = new int[12]; 
    InputArray(array); 
    Console.WriteLine("[" + string.Join(", ", array) + "]"); 
    for (int i = 0; i < array.Length; i++) 
    array[i] = array[i] * (-1); 
    Console.WriteLine("[" + string.Join(", ", array) + "]"); 
    } 
    ReplaceArray(); 
    


void PositiveNumber(int[] array) 
{ 
    int summa_p = 0; 
    for (int i = 0; i < array.Length; i++) 
    {
         if (array[i] > 0) summa_p = summa_p + array[i]; 
    } 
    Console.WriteLine("Сумма положительных элементов равна: " + summa_p); 
} 

void NegativeNumber(int[] array) 
{ 
    int summa_n = 0; for (int i = 0; i < array.Length; i++) 
    { 
        if (array[i] < 0) summa_n = summa_n + array[i]; 
    } 
    Console.WriteLine("Сумма отрицательных элементов равна: " + summa_n); 
} 
    int[] matrix = new int[12]; 
    InputArray(matrix); 
    Console.WriteLine("[" + string.Join(", ", matrix) + "]"); 
    PositiveNumber(matrix); NegativeNumber(matrix); 
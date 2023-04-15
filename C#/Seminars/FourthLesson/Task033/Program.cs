// Task 33
/*
Задайте массив. Напишите программу, которая определяет, 
присутствует ли заданное число в массиве. Например:
4; массив [6, 7, 19, 345, 3] --> no
3; массив [6. 7. 19. 345. 3] --> yes
*/

void InputArray(int[] array) 
{ 
    for (int i = 0; i < array.Length; i++) 
    array[i] = new Random().Next(-9, 10); 
} 
string FindNumberInArray(int[] massiv, int whatFind) 
    { 
        int counter = massiv.Length; 
        int indexs = 0; 
        while (indexs < counter) 
        { 
        if (massiv[indexs] == whatFind) 
            { 
        return "yes"; 
            } 
            indexs++; 
        } 
        return "no"; 
    } 

int[] array = new int[10]; 
InputArray(array); 
Console.WriteLine("[" + string.Join(", ", array) + "]"); 
Console.Write("Введите число, которое Вы хотите найти: "); 
int n = Convert.ToInt32(Console.ReadLine()); 
Console.WriteLine(FindNumberInArray(array, n)); //мы не указали что whatFind = n но программа работает...
                                                // КАК??

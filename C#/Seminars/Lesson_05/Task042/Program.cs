// Task 42
/*
Напишите программу, которая будет преобразовывать
десятичное число в двоичное
*/

Console.Clear(); 
int n = Convert.ToInt32(Console.ReadLine()); 
string result = ""; 
while (n > 0) 
{ 
    result = Convert.ToString(n % 2) + result; 
    n = n / 2; 
} 
Console.WriteLine(result); 

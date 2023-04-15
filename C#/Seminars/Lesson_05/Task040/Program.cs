// Task 40
/*
Напишите программу, которая принимает на вход три числа
и проверяет, может ли существовать треугольник со сторонами 
такой длины
*/
Console.WriteLine("Ведите длину первой стороны треугольника: ");
int a = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Ведите длину второй стороны треугольника: ");
int b = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Ведите длину третьей стороны треугольника: ");
int c = Convert.ToInt32(Console.ReadLine());
int max = 0;

if(a > max)
max = a;
if(b > max)
max = b;
if(c > max)
max = c;
if( a + b + c - max > max)
Console.WriteLine("Yes");

/*
Console.Clear(); 
int a = Convert.ToInt32(Console.ReadLine()); 
int b = Convert.ToInt32(Console.ReadLine()); 
int c = Convert.ToInt32(Console.ReadLine()); 
if (a + b > c && c + a > b && b + c > a) 
Console.WriteLine("yes"); 
else Console.WriteLine("no"); 
*/
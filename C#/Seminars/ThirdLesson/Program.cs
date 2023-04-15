/*задача 1

Console.WriteLine("Введите координату Х: ");
int x = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите координату Y: ");
int y = Convert.ToInt32(Console.ReadLine());

if (x > 0 && y > 0)
    Console.WriteLine("Координата находится в 1 четверти");
if (x < 0 && y > 0)
    Console.WriteLine("Координата находится в 2 четверти");
if (x < 0 && y < 0)
    Console.WriteLine("Координата находится в 3 четверти");
if (x > 0 && y < 0)
    Console.WriteLine("Координата находится в 4 четверти");
*/

/*
Console.WriteLine("Введите четверть координат: ");
int x = Convert.ToInt32(Console.ReadLine());

if (x == 1)
    Console.WriteLine("Координаты в пределах х + ~, y + ~");
if (x == 2)
    Console.WriteLine("Координата находится в 2 четверти");
if (x == 3)
    Console.WriteLine("Координата находится в 3 четверти");
if (x == 4)
    Console.WriteLine("Координата находится в 4 четверти");
*/


/*
Console.WriteLine("Введите координаты первой точки: ");
int a = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите координаты второй точки: ");
int b = Convert.ToInt32(Console.ReadLine());

int diff = (a[0]- b[0]) * (a[0]- b[0]) + (a[1] - b[1]) * (a[1] - b[1])


Console.Write("Введите x1: "); 
int x1 = Convert.ToInt32(Console.ReadLine()); 
Console.Write("Введите y1: "); 
int y1 = Convert.ToInt32(Console.ReadLine()); 
Console.Write("Введите x2: "); 
int x2 = Convert.ToInt32(Console.ReadLine()); 
Console.Write("Введите y2: "); 
int y2 = Convert.ToInt32(Console.ReadLine()); 
Console.Write(Math.Sqrt(Math.Pow(x1 - x2, 2) + Math.Pow(y1 - y2, 2))); 
*/


Console.WriteLine("Введите число: ");
int n = Convert.ToInt32(Console.ReadLine());
for (int i = 1; i <= n; i++)
Console.WriteLine(i + "2 = " + i * i);
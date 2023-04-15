// Числа Фибоначчи

Console.Write("Введите число для вычисления: ");
int n = Convert.ToInt32(Console.ReadLine());

int Fibonachi(int n)
{
    if (n == 1 || n == 2) return 1;
    else return Fibonachi(n - 1) + Fibonachi(n - 2);
}
for (int i = 1; i < n; i++)
{
    Console.WriteLine($"f{i} = {Fibonachi(i)}");
}

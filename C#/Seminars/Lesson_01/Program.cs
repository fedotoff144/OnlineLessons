/*

Console.Write("Enter number: ");
int n = Convert.ToInt32(Console.ReadLine());
Console.WriteLine(n * n);



Console.Write("Enter first number: ");
int a = Convert.ToInt32(Console.ReadLine());
Console.Write("Enter second number: ");
int b = Convert.ToInt32(Console.ReadLine());
if (a / b == b)
  Console.WriteLine("yes");
else
   Console.WriteLine("no");



Console.Write("Enter number please: ");
int n = Convert.ToInt32(Console.ReadLine());
while (n < 1 || n > 7)
 {
    Console.Write("Miss! Try again: ");
    n = Convert.ToInt32(Console.ReadLine);
 }
 // [1, 7]
if (n == 1)
    Console.WriteLine("Ponedel'nik");
if (n == 2)
    Console.WriteLine("Vtornik");
if (n == 3)
    Console.WriteLine("Sreda");
if (n == 4)
    Console.WriteLine("Chetverg");
if (n == 5)
    Console.WriteLine("Pyatnica");
if (n == 6)
    Console.WriteLine("Subbota");
if (n == 7)
    Console.WriteLine("Voskresenie");



Console.Write("Enter number please:");
int n = Convert.ToInt32(Console.ReadLine());
int i = (-1) * n;
while (i <= n)
{
    Console.Write(i + " ");
    i++;
}
for (int i = (-1) * n; i <= n; i++)
//Console.Write(i +" ");

Console.Write("Enter number please: ");
int n = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("The last digit of namber: " + n % 10 );






//Задача 2
Console.WriteLine("Enter first number please: ");
int a = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Enter second number please: ");
int b = Convert.ToInt32(Console.ReadLine());
if (a == b){
    Console.WriteLine("Both numbers are equal!");
} else if (a > b){
    Console.WriteLine(a + " is more numbers");
    Console.WriteLine(b + " is lesser numbers");
} else if (a < b){
    Console.WriteLine(b + " is more numbers");
    Console.WriteLine(a + " is lesser numbers");
}



//Задача 4
Console.WriteLine("Enter first number please: ");
int a = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Enter second number please: ");
int b = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Enter third number please: ");
int c = Convert.ToInt32(Console.ReadLine());
int max = 0;
if (a < b){
    max = b;
} else {
    max = a;
}
if (max < c){
    max = c;
}
Console.WriteLine("Maximum is " + max);



//Задача 6
Console.WriteLine("Enter number please: ");
int x = Convert.ToInt32(Console.ReadLine());
if (x % 2 == 0){
    Console.WriteLine(x + " is even");
}else {
    Console.WriteLine(x + " is not even");
}



//Задача 8
Console.WriteLine("Enter number please: ");
int x = Convert.ToInt32(Console.ReadLine());
if (x > 1){
    for (int i = 2; i <= x; i += 2){
        Console.Write(i + " ");
    }
} else {Console.Write("Четных чисел нет!"); }
*/
/*
// Task aboute ice cream

Console.WriteLine("Ведите количество шариков мороженого: ");
int icecream = Convert.ToInt32(Console.ReadLine());

if (icecream % 3 == 0 || 
    icecream % 5 == 0 || 
    icecream % 8 == 0 || 
    icecream % 8 % 3 == 0 ||
    icecream % 8 % 5 == 0){
    Console.WriteLine("Yes");
} else {
    Console.WriteLine("No");
}


//A Task about train


// A Task about stairs
*/

/*
Convert.ToInt32(Console.ReadLine()); 
Console.WriteLine(((n + 1) / 2) * n); 
*/
/*
Console.WriteLine("Enter number: ");
int n = Convert.ToInt32(Console.ReadLine());
int count = 0;
while (n > 0)
{
    n = n / 10;
    count++;
}
*/

/*
int n = Convert.ToInt32(Console.ReadLine()); 
int res = 1; 
for (int i = 1; i <= n; i++) res = res * i; 
Console.Write(res); 
*/

int[] array = new int[8];

for (int i = 0; i < array.Length; i++)
    array[i] = new Random().Next(0, 2);

Console.WriteLine("[" + string.Join(", ", array) + "]");

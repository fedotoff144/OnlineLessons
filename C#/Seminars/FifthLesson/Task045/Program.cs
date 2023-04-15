// 

Console.Clear(); 
int[] a = {1, 2, 3, 4, 5}; 
int[] b = new int[a.Length]; 
for (int i = 0; i < a.Length; i++) 
{ 
    b[i] = a[i]; 
} 
    b[0] = 10; 
    Console.WriteLine("[" + string.Join(", ", a) + "]"); 
    Console.WriteLine("[" + string.Join(", ", b) + "]"); 

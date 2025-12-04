var lines = File.ReadAllLines("input.txt");

int dial = 50;
double res = 0;

foreach (var line in lines)
{
	string dir = line.Substring(0, 1);
	int value = int.Parse(line.Substring(1));

	if (dir == "L")
	{
		dial -= value;
	}
	else
	{
		dial += value;
	}
	dial = ((dial % 100) + 100) % 100;
	if (dial == 0) res++;
}

Console.WriteLine($"result: {res}");
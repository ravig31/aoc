var lines = File.ReadAllLines("input.txt");

double dial = 50;
double res = 0;

foreach (var line in lines)
{
	string dir = line.Substring(0, 1);
	double distance = double.Parse(line.Substring(1));

	res += Math.Floor(distance / 100);
	distance %= 100;

	if (dir == "L")
	{
		dial -= distance;
		if (dial == 0 && distance != 0) res++;
		else if (dial < 0)
		{
			if (dial + distance != 0) { res++; }
			dial += 100;
		}
	}
	else
	{
		dial += distance;
		if (dial > 99)
		{
			dial -= 100;
			res++;
		}
	}
}

Console.WriteLine($"result: {res}");
#include<stdlib.h>
#include<stdio.h>
#include<locale.h>
#include<math.h>

int main()
{
	char *locale = setlocale(LC_ALL, "");
	double d[5] = { 14.85, 14.8,14.79,14.84,14.81 };
	int n = 5;
	double delta[5], deltaSq[5], dSum = 0, deltaSqSum = 0;
	double d0 = 14.8;
	for (int i = 0; i < 5; i++) {
		delta[i] = d[i] - d0;
		deltaSq[i] = delta[i] * delta[i];
		dSum += d[i];
		deltaSqSum += deltaSq[i];
	};
	double koefStud = 2.57;
	double average = dSum / n;
	double dispersion = (1. / (n * (n - 1)))*(deltaSqSum - n * (average - d0)*(average - d0));
	double standDelt = sqrt(dispersion), absDelt = koefStud * standDelt, otnDelt = absDelt / average;

	for (int i = 0; i < 5; i++) {
		if (i == 2) {
			printf("-----------------------------------------\n");
			printf("| %lf | %.8lf | %.8lf  |\n", d[i], delta[i], deltaSq[i]);
		}
		else {
			printf("-----------------------------------------\n");
			printf("| %lf | %.8lf  | %.8lf  |\n", d[i], delta[i], deltaSq[i]);
		}
	}
	printf("-----------------------------------------\n\n");
	printf("Average d = %.8lf\nDisperssion = %.8lf\nStandart deviation= %.8lf\nAbsolute error = %.8lf\nRelative error = %.8lf", average, dispersion, standDelt, absDelt, otnDelt);

	system("pause");
	return 0;
}

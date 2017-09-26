#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>

int main() 
{

	int jack;
	int jill;
	int sell = 0;


	while(std::cin >> jack >> jill) 
	{
		sell = 0;

		if (jack + jill == 0) break;

		int jackn[jack];
		int *p1 = jackn;

		for(int i = 0; i<jack;i++)
			scanf("%d", &jackn[i]);

		for(int i = 0; i<jill;i++)
		{
			int p;
			scanf("%d", &p);
			
			if (p1 < (jackn+jack))
			{
				if (p > *p1)
				{
					while(p > *p1)	
						p1++;
				}

				if (p==*p1)
				{	
					sell++;
					p1++;
				}
			}
		
		}

		printf("\n%d", sell);
	}
}

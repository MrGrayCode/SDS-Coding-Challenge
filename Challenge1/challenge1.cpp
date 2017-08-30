#include<bits/stdc++.h>
#define N 100001
using namespace std;

int main()
{
	// Sieve
	bool primes[N];
	memset(primes,true,sizeof(primes));
	for(int i=2;i*i<N;i++)
	{
		if(primes[i])
		{
			for(int j=2*i;j<N;j+=i)
			{
				primes[j] = false;
			}
		}
	}
	
	//Input
	int n;
	cin>>n;
	
	// Algo
	int n1 = -1;
	int n2 = -1;
	for(int i=n-1;i>0;i--)
	{
		if(primes[i])
		{
			n1 = i;
			break;
		}
	}	
	for(int i=n+1;i<N;i++)
	{
		if(primes[i])
		{
			n2 = i;
			break;
		}
	}
	cout<<n1<<","<<n<<","<<n2<<endl;	
}

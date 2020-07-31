#include <iostream>
#define MAX 1001
#define MODER 10007
using namespace std;

int array[MAX] = {0};

int dp(int n)
{
    if(n<1) return 0;
    if(array[n]!=0)
    {
        return array[n];
    }
    else
    {
        array[n]  = (dp(n-2) + dp(n-1)) % MODER;
        return array[n];
    }
}

int main()
{
    int N;
    array[1] = 1;
    array[2] = 2;
    cin >> N;
    cout << dp(N);
}

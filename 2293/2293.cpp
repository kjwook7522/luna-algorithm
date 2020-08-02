#include <iostream>
#include <vector>
#define MAX 100+1
#define K_MAX 10000+1
using namespace std;
int num_cases[K_MAX] = {0};
int main()
{
    int n,k;
    vector<int> coins_val;
    int val;
    cin >> n >> k;
    for(int i=0; i<n; i++)
    {
        cin >> val;
        coins_val.push_back(val);  
    }
    num_cases[0] = 1;
    for(int i=0;i<n;i++)
    {
        for(int j=coins_val[i]; j<=k; j++)
        {
            num_cases[j] += num_cases[j-coins_val[i]];
        }
    }   
    cout << num_cases[k];
    return 0;
}

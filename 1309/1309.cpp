#include <iostream>
#include <vector>
#define DIV 9901
#define MAX 100000+1
using namespace std;

int lions[MAX][3] = {0};

int main()
{
    int N,answer;
    cin >> N;
    lions[1][0] = 1;
    lions[1][1] = 1;
    lions[1][2] = 1;
    for(int i=2; i<=N; i++)
    {
        lions[i][0] = (lions[i-1][0] + lions[i-1][1] + lions[i-1][2]) % DIV;
        lions[i][1] = (lions[i-1][0] + lions[i-1][2]) % DIV;
        lions[i][2] = (lions[i-1][0] + lions[i-1][1]) % DIV;
    }
    answer = (lions[N][0] + lions[N][1] + lions[N][2]) % DIV;
    cout << answer;
}

#include <iostream>
#define MAX_SONG 101
#define MAX_VOL 1001
using namespace std;

int volumes[MAX_SONG] = {0};
bool tree[MAX_SONG][MAX_VOL] = {false};

void dp(int N,int S,int M)
{
    int answer = -1;
    bool isFail = true;
 
    tree[0][S] = true;
    for(int n=0; n <= N-1; n++)
    {
        for(int m=0;m<=M;m++)
        {
            if(tree[n][m])
            {
                if(m-volumes[n+1] >= 0)
                {
                    tree[n+1][m-volumes[n+1]] = true;
                }
                if(m+volumes[n+1] <= M)
                {
                    tree[n+1][m+volumes[n+1]] = true;
                }
            }

        }
    }
    for(int v=0; v<=M; v++)
    {
        if(tree[N][v])
        {
            answer = v;
        }
    }
    cout << answer << "\n";
}

int main()
{
    int N,S,M;
    cin >> N >> S >> M;
    for(int i=1; i<=N; i++)
    {
        cin >> volumes[i];
    }
    dp(N,S,M);

}

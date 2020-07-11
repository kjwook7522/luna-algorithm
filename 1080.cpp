#include <iostream>
#include <string.h>
#define MAX 50

using namespace std;

void toggle(bool (*arr)[MAX],int n,int m)
{
    for(int i=n; i<n+3; i++)
    {
        for(int j=m; j<m+3; j++)
        {
            if(arr[i][j])
            {
                arr[i][j] = false;
            }
            else
            {
                arr[i][j] = true;
            }
        }
    }
}

int main(){
    int N,M;
    string A[MAX];
    string B[MAX];
    bool ans[MAX][MAX] = {false};
    int answer=0;
    cin >> N >> M;

    for(int n=0 ; n<N; n++)
    {
        cin >> A[n];
    }
    for(int n=0; n<N; n++)
    {
        cin >> B[n];
        for(int m=0; m<M; m++)
        {
            if(A[n][m] == B[n][m])
            {
                ans[n][m] = true;
            }          
        }
    }
    if(N < 3 || M < 3)
    {
        for(int n=0;n<N;n++)
        {
            for(int m=0;m<M;m++)
            {
                if(!ans[n][m])
                {
                    cout <<"-1"<<"\n";
                    return 0;
                }
            }
        }
        cout <<"0\n";
        return 0;
    }

    for(int n=0; n<=N-3; n++)
    {
        for(int m=0; m<=M-3; m++)
        {
            if(!ans[n][m])
            {
                toggle(ans,n,m);
                answer++;
            }
        }
    }
    for(int n=0; n<N; n++)
    {
        for(int m=0; m<M; m++)
        {
            if(!ans[n][m])
            {
                cout << "-1"<<"\n";
                return 0;
            }
        }
    }
    cout<<answer<<"\n";
    return 0;
}

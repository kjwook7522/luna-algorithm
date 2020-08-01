#include <iostream>
#include <vector>
#define MAX 100
using namespace std;

int N;
bool isException(int x,int y)
{
    if(x > N-1 || x < 0 || y > N-1 || y < 0)
    {
        return true;
    }
    else
    {
        return false;
    }
    
}
int main()
{
    vector<int> board[MAX];
    vector<long> routes[MAX];
    cin >> N;
    int move;
    for(int i=0; i<N; i++)
    {
        for(int j=0; j<N; j++)
        {
            cin >> move;
            board[i].push_back(move);
            routes[i].push_back(0);
        }
    }
    routes[0][0] = 1;
    for(int i=0; i<N; i++)
    {
        for(int j=0; j<N; j++)
        {
            move = board[i][j];
            if(move==0)
            {
                continue;
            }
            if(!isException(i+move,j))
            {
                routes[i+move][j] += routes[i][j];
            }
            if (!isException(i,j+move))
            {
                routes[i][j+move] += routes[i][j];
            }
        }
    }
    cout << routes[N-1][N-1] <<"\n";

}

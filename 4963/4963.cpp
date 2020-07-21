#include <iostream>
#include <string.h>

#define MAX 50
using namespace std;
int row,col = 1;

struct move{
    int x[3] = {-1,0,1};
    int y[3] = {-1,0,1};
};

bool isException(int x,int y)
{
    if(x>=row || y>=col || x < 0 || y < 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void checkArea(bool(* map)[MAX],int w,int h)
{
    struct move move;
    int move_x = 0;
    int move_y = 0;
    for(int i=0; i<3; i++)
    {
        for(int j=0;j<3;j++)
        {
            move_x = w+move.x[i];
            move_y = h+move.y[j];
            if(isException(move_x,move_y)) //  || (i==1 && j==1)
            {
                continue;
            }
            else
            {
                if(map[move_x][move_y])
                {
                    map[move_x][move_y] = false;
                    checkArea(map,move_x,move_y);
                }
            }
            
        }
    }
}

void countIsland(bool(* map)[MAX])
{
    int numberOfIsland = 0;
    for(int w=0; w<row; w++)
    {
        for(int h=0;h<col;h++)
        {
            if(map[w][h])
            {
                map[w][h] = false;
                checkArea(map,w,h);
                numberOfIsland++;
            }
        }
    }
    cout << numberOfIsland<<"\n";
}

int main()
{
    bool map[MAX][MAX] = {false};
    while(1)
    {
        cin >> col >> row;
        if(row==0 && col==0)
        {
            return 0;
        }
        for(int w=0; w<row; w++)
        {
            for(int h=0;h<col;h++)
            {
                cin >> map[w][h];
            }
        }
        countIsland(map);

        for(int i=0; i<MAX; i++)
        {
            memset(map[i], false, sizeof(bool)*MAX); //모든 값 0으로 초기화
        }
    }
    return 0;
}

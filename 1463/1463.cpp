#include <iostream>
#define MAX 1000001
using namespace std;
int array[MAX] = {0};

void dp(int input)
{
    if(input==1) return;
    if(input % 3 == 0)
    {
        if(array[input/3] == 0 || (array[input/3] > array[input]+1))
        {
            array[input/3] = array[input]+1;
            dp(input/3);
        }
    }
    if(input % 2 == 0)
    {
        if(array[input/2] == 0 || (array[input/2] > array[input]+1))
        {
            array[input/2] = array[input]+1;
            dp(input/2);
        }
    }
    if(array[input-1] == 0 || (array[input-1] > array[input]+1))
        {
            array[input-1] = array[input]+1;
            dp(input-1);
        }
    return;
}

int main()
{
    int input;
    cin >> input;
    dp(input);
    cout << array[1];
}

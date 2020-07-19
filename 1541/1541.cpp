/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <string>
using namespace std;

int main()
{
    string tmp;
    bool flag = false;
    int answer=0;
    string input;
    cin >> input;
    for(int i=0; i<=input.size();++i)
    {
        if(input[i]=='-' || input[i] == '+' || input[i]=='\0')
        {
            if(flag)
            {
                answer -= atoi(tmp.c_str());
                
            }
            else
            {
                answer += atoi(tmp.c_str());
            }
            if(input[i]=='-')
            {
                flag = true;
            }
            tmp = "";
            continue;
        }
        tmp += input[i];
    }
    cout << answer;

    return 0;
}

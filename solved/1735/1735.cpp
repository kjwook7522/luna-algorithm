#include <iostream>
using namespace std;

int gcd(int a, int b)
{
    int c;
    while(b!=0)
    {
        c = a % b;
        a = b;
        b = c;
    }
    return a;
}
int main()
{
    int c1,p1,c2,p2;
    int P,C;
    cin >> c1 >> p1;
    cin >> c2 >> p2;
    C = c1*p2 + c2*p1;
    P = p1*p2;
    int div = gcd(C,P);
    cout << C/div << " " << P/div << "\n";
    return 0;
}

#include <iostream>
#include <vector>
#include <algorithm>
#define CARD_MAX 500000
using namespace std;

vector<int> cards;
vector<int> answer;
int N,M;
void bin_search(int card)
{
    int low = 0;
    int high = N-1;
    int mid = 0;
    bool isfound = false;
    while(low <= high)
    {
        mid = (low + high) / 2;
        if(cards[mid] != card)
        {
            if(cards[mid] > card) // 중간 위치 카드가 찾으려는 카드보다 크면 왼쪽
            {
                high = mid - 1;
            }
            else // 반대면 오른쪽
            {
                low = mid + 1;
            }
        }
        else // mid의 card가 찾으려는 카드의 값과 일치하면
        {
            isfound = true;
            break;
        }
    }
    if(isfound)
    {
        answer.push_back(1);
    }
    else answer.push_back(0);
    return;

}

int main()
{

    int card;
    cin >> N;
    for(int i=0; i<N; i++)
    {
        cin >> card; 
        cards.push_back(card);
    }
    sort(cards.begin(),cards.end());
    cin >> M;
    for(int i=0; i<M;i++)
    {
        cin >> card;
        bin_search(card);
    }
    for(int i=0; i<M; i++)
    {
        cout << answer[i] << " ";
    }

}

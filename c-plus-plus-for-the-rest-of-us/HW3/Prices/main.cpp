#include <iostream>
#include <iomanip>

using namespace std;

void print_amount(const char *message, float amount)
{

    cout<<message<<right<<setw(15)<<setprecision(2)<<amount<<'\n';

}

int main()
{
    double price1, price2, price3, total;
    cout<<"enter a price"<<endl;
    cin>>price1;
    cout<<"enter a price"<<endl;
    cin>>price2;
    cout<<"enter a price"<<endl;
    cin>>price3;
    cout<<endl<<endl;

    total=price1+price2+price3;

    cout << setiosflags(ios::fixed);

    print_amount("Price 1 is   ", price1);
    print_amount("Price 2 is   ", price2);
    print_amount("Price 3 is   ", price3);
    cout<<endl;
    print_amount("Total price: ", total);

    return 0;
}



#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    double price1, price2, price3, total;
    cout<<"enter a price"<<endl;
    cin>>price1;
    cout<<"enter a price"<<endl;
    cin>>price2;
    cout<<"enter a price"<<endl;
    cin>>price3;

    total=price1+price2+price3;

     cout << setiosflags(ios::fixed);

cout<<"Price 1 is "<<setprecision(2)<<setw(10)<<right<<price1<<endl;
cout<<"Price 2 is "<<setprecision(2)<<setw(10)<<right<<price2<<endl;
cout<<"Price 3 is "<<setprecision(2)<<setw(10)<<right<<price3<<endl;
cout<<"Total price: "<<setprecision(2)<<setw(7)<<right<<total<<endl;
    return 0;
}

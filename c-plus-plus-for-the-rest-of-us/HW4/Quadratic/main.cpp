#include <iostream>
#include<math.h>


using namespace std;

int main()
{
float a,b,c,x1,x2;

cout<<"enter the value for a" << endl;
cin>>a;
cout<<"enter the value for b" << endl;
cin>>b;
cout<<"enter the value for c" << endl;
cin>>c;

x2=((-1*b)+sqrt((b*b)-(4*a*c)))/(2*a);

x1=((-1*b)-sqrt((b*b)-(4*a*c)))/(2*a);

cout<<"This quadratic has the following roots: X = "<<x1<<", X = "<<x2<<endl;

    return 0;
}

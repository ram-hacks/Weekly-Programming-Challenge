#include <iostream>
using namespace std;

int main() {
    for(int i = 1; i <= 50; i++) {
        if(((i % 3) == 0) && ((i % 5) != 0)) {
            cout<<"RAM\n";
        }
        else if(((i % 5) == 0) && ((i % 3) != 0)) {
            cout<<"Hacks\n";
        }
        else if(((i % 3) == 0) && ((i % 5) == 0)) {
            cout<<"RAMHacks\n";
        }
        else {
            cout<<i<<endl;
        }
    }
    return 0;
}

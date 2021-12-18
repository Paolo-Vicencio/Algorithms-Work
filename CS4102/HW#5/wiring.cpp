#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> vec;
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(3);
    cout << vec[1] << endl;
    for (int i = 0; i < vec.size(); i++) {
        cout << vec[i] << endl;
    }
    return 0;
}
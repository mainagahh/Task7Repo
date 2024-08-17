#include <bits/stdc++.h>
using namespace std;

int main(){
    // take the number of elements
    int n, a, g =0;
    cin >> n;
    int arr[n];
    // assign elements' values
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    } 
        cin >> a;
        // compare and print the index of the desired element
     for(int i = 0; i < n; i++){
        if(a == arr[i]){
            cout << i <<endl;
            g = 1;
        }
    }
     // print -1 if the value does not exist
        if(g == 1){}
        else {cout << -1;}
        return 0;
}
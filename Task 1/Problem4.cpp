#include <bits/stdc++.h>
using namespace std;

int main(){
    int l, m;
    cin >> l >> m;
    long int arr1[l][m], arr2[l][m];
    int s=0 , a=0;
    for (int i = 0; i < l; i++) {
        for (int j = 0; j < m; j++) {
            cin >>  arr1[i][j] ;
        }
    }

    for (int i = 0; i < l; i++) {
        for (int j = 0; j < m; j++) {
            cin >>  arr2[i][j] ;
        }
    }

    for (int i = 0; i < l; i++) {
        for (int j = 0; j < m; j++) {
           if( arr1[i][j] > arr2[i][j] ){
            s++;
           }
           else if(arr1[i][j] < arr2[i][j]){
            a++;
           }
        }
    }

    if( s > a){
        cout << "Justice League";
    }
    else if( s < a) {
        cout << "Villains";
    }
    else{
        cout << "Tie";
    }
    return 0;
}
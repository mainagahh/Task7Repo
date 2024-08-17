#include <bits/stdc++.h>
using namespace std;

struct course {
    string name;
    int credit;
    float score;
    float grade;

};

float getGrade(float score){
    if(score >= 85){
        return 4.0;
    }
    else if (score >= 70){
        return 3.0;
    }
    else if (score >= 60){
        return 2.0;
    }
    else if(score > 50) {
        return 1.0;
    }
    else {
        return 0.0;
    }
}

int main() {
    course crs1;
    cout << "Enter Course name" <<endl;
    getline(cin, crs1.name);
    cout << "Enter Course credit" <<endl;
    cin >> crs1.credit;
    cout << "Enter Course score" <<endl;
    cin >> crs1.score;
    crs1.grade = getGrade(crs1.score);
    cout << "course name is:" << crs1.name <<endl;
    cout << "course credit is:" << crs1.credit <<endl;
    cout << "course score is:" << crs1.score <<endl;
    cout << "course grade is:" << crs1.grade <<endl;
    return 0;
}
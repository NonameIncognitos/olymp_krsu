#include<bits/stdc++.h>

using namespace std;

int main() {
    int N;
    cin >> N;

    int current = 0;
    int answer = 0;

    for (int i = 0; i < N; i++) {
        int A, T;
        cin >> A >> T;

        if (T > -1) {
            current = max(0, current-T-2);
        }

        current += (A == 1 ? 20 : 0);

        answer = max(answer, current);
    }

    cout << answer;

    return 0;
}


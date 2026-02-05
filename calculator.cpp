#include <iostream>

using namespace std;


int add(int a, int b) {
    return a + b;
}

int sub(int a, int b) {
    return a - b;
}

int mul(int a, int b) {
    return a * b;
}

int divide(int a, int b) {
    return a / b;
}

int main() {
    int a, b;
    char op;

    cout << "Enter two numbers: ";
    cin >> a >> b;

    cout << "Enter operation (+, -, *, /): ";
    cin >> op;

    if (op == '+')
        cout << "Result: " << add(a, b);
    else if (op == '-')
        cout << "Result: " << sub(a, b);
    else if (op == '*')
        cout << "Result: " << mul(a, b);
    else if (op == '/') {
        if (b != 0)
            cout << "Result: " << divide(a, b);
        else
            cout << "Error: division by zero";
    } else {
        cout << "Unknown operation";
    }

    return 0;
}

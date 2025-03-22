// This is a single-line comment

/* 
   This is a multi-line comment 
   to test block comment highlighting
*/

// Variables
int myNumber = 10;
double price = 1.2345;
string message = "Hello, MQL5!";

// Print to the log
void OnStart() {
    Print("Testing MQL5 syntax highlighting!");
    
    // Conditional statement
    if (myNumber > 5) {
        Print("Number is greater than 5");
    } else {
        Print("Number is 5 or less");
    }
    
    // Loop test
    for(int i = 0; i < 3; i++) {
        Print("Loop iteration: ", i);
    }
}

// Test built-in MQL5 functions
void OrderTest() {
    double lotSize = 0.1;
    int ticket = OrderSend(Symbol(), OP_BUY, lotSize, Ask, 10, 0, 0, "Test Order", 0, 0, clrNONE);

    if (ticket > 0) {
        Print("Order placed successfully: ", ticket);
    } else {
        Print("Order failed! Error: ", GetLastError());
    }
}

// Arrays and math operations
double prices[5] = {1.234, 1.235, 1.236, 1.237, 1.238};

void ArrayTest() {
    for (int i = 0; i < 5; i++) {
        double newPrice = prices[i] * 1.01; // Increase by 1%
        Print("New price: ", newPrice);
    }
}

// Object-oriented programming in MQL5
class MyClass {
public:
    int value;
    
    void SetValue(int v) {
        value = v;
    }

    int GetValue() {
        return value;
    }
};

void ObjectTest() {
    MyClass obj;
    obj.SetValue(42);
    Print("Object Value: ", obj.GetValue());
}

### 1. (5 pts) Given the C++ declaration:
```c++
struct {
  int n;
  char c;
} A[10][10];
```
On your machine, find the address of A[0][0] and A[3][7]. Explain why these values are what you found them to be.
> The address of A[0][0] is 0x7fff5fbff300 and the address for A[3][7] is 0x7fff5fbff428. The values either end in a 0 or an 8. It is a pattern for example, I tested A[3][0], A[3][1], A[3][2],... and so one till A[3][7] and the out put was  0x7fff5fbff3f8, 0x7fff5fbff400, 0x7fff5fbff408, 0x7fff5fbff410, 0x7fff5fbff418, 0x7fff5fbff420, 0x7fff5fbff428. Therefore, the difference between the two address is 296.

### 2. (5 pts) Explain the meaning of the following C++ declarations:
```c++
double *a[n];
double (*b)[n];
double (*c[n])();
double (*d())[n];
```
> double *a[n] is an array of double pointers size n.
> double (*b)[n] is a pointer to an array size n.
> double (*c[n])() is an array size n of pointers to functions that return doubles.
> double (*d())[n] is a function that returns a pointer to an array size n of doubles.


### 3. (5 pts) Consider the following declaration in C++:
```c++
double (*f(double (*)(double, double[]), double)) (double, ...);
```
Describe rigorously, in English, the type of f.


> The declaration above is a function that returns a function and accepts certain arguments. It is clear that the most left double states that what ever is on the right is a double. The fist function is double  and only takes in the parameters (double, ...) and returns a double. The declaration also consists on three functions. The second function is (*f(double (*)(double, double[]), double)) that returns a function. The most inner function is  The third function is (*)(double, double[]), double)), which is an argument that returns a double and takes in the parameters of a double and a double array. It also includes arguments that is accepted by the function.  

### 4. (5 pts) What happens when we “redefine” a field in a C++ subclass? For example, suppose we have:
```c++
class Base {
public:
  int a;
  std::string b;
};


class Derived: public Base {
public:
  float c;
  int b;
};
```
Does the representation of a Derived object contain one b field or two? If two, are both accessible, or only one? Under what circumstances? Tell the story of how things are.

> It contains 2. The code that demonstrates this is:
```c++
class Base {
public:
  int a;
  std::string b = "hey";
};


class Derived: public Base {
public:
  float c;
  int b = 4;
};


int main() {
    Base *outer = new Base();
    Derived *inner = new Derived();
    std::cout << outer->b << "\n";
    std::cout << inner->b << "\n";
    std::cout << ((Base*)inner)->b << "\n";
    return 0;
}
```
>of which the output is "hey 4 hey", so the inner class when referred to, prints the local variable b, rather than the inherited variable b, and it hides the inherited variable b. However, when inner is referenced with a Base pointer, the base pointer references the variable that it would have found in the Base class, in turn, revealing the Base class variable b, 4. 

### 5. (5 pts) What does the following C++ program output?
```c++
#include <iostream>
int x = 2;
void f() {
  std::cout << x << '\n';
}
void g() {
  int x = 5;
  f();
  std::cout << x << '\n';
}
int main() {
  g();
  std::cout << x << '\n';
}
```
Verify that the answer you obtained is the same that would be inferred from applying the rules of static scoping. If C++ used dynamic scoping, what would the output have been?

> The output for this program is 2,5,2 because when the main function is called the g function will first display the global variable because that is what was stated first, then it will output the local variable. Next, when std::cout << x << '\n'; is called it will display the global variable. If dynamic scoping was used the output would have been 5,2,2 because dynamic scoping can be thought of as context-specific scoping. Dynamic scoping means that when a symbol is referenced, the compiler will walk up the symbol-table stack to find the correct instance of the variable to use.

### 6. (5 pts) Suppose you were asked to write a function to scramble (shuffle) a given array, in a mutable fashion. Give the function signature for a shuffle function for (a) a raw array, and (b) a std::array.

a)

```c++
template <typename T>
void shuffleRawArray(T* a, int length)
```

b)

```c++
template<typename T, std::size_t length>
void shuffleStdArray(array<T, length> a)
```
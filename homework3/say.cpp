#include <iostream>
#include <cassert>

using namespace std;

struct Adder {
//private:
  string phrase = "";
public:

  Adder operator()(string word) {
    return Adder {phrase + (phrase != "" ? " " : "") + word };
  }
  string operator()() {
    return phrase;
  }

};

Adder f;

int main() {
  assert(f() == "");
  assert(f("all")() == "all");
  assert(f("hi")("you")() == "hi you");
  assert(f("all")("your")("tests")("pass")() == "all your tests pass");
  cout << "Yep, all tests passed, LIT AF!\n";
}

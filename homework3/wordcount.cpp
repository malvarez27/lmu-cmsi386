#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

auto getCounts(std::string &sentence){
  string word;
  map<string, int> counts;
  for (char c: sentence) {
    c = tolower(c);
    if (isalpha(c)) {
      word += c;
    } else if (word != ""){
      counts[word]++;
      word = "";
    }
  }
  return counts;
}

void printCounts(map<string,int> counts) {
  for (auto pair: counts) {
    cout << pair.first << ' ' << pair.second << '\n';
  }
}

string get_standard_input() {
  string contents = "";
  string line;
  while (getline(cin, line)) {
    contents += line;
  }
  return contents;
}

int main() {
  string sentence = get_standard_input();
  printCounts(getCounts(sentence));
}

#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

void remove_nonletters(std::string &sentence){
  int i = 0;
  for (i = 0; i < sentence.length(); i++){
    sentence[i] = tolower(sentence[i]) ;
    if(!(isalpha(sentence[i]))) {
      if(isalpha(sentence[i+1])){
        sentence[i] = ' ';
    }
      else{
    sentence[i] = ' ';
      }
    }
    else{
      sentence[i] = tolower(sentence[i]);
    }
  }
}

string sentence= " ";


map<string, int> getCounts(vector<string> words, string sentence) {
  map<string, int> counts;
  for (string word: words) {
    counts[word]++;
  }
  return counts;
}

void printCounts(map<string,int> counts) {
  for (auto pair: counts) {
    cout << pair.first << ' ' << pair.second << '\n';
  }
}

int main() {
    string s = "hi, my name is123";
    remove_nonletters(s);
  printCounts(getCounts((sentence)));
}

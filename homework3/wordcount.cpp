#include <cassert>
#include <iostream>
#include <string>

using namespace std;

void remove_nonletters(){
  int i = 0;
  string sentence = " ";
  for (i = 0; i < sentence.length; i++){
    sentence[i] = tolower(sentence[i]) ;
    if(!(isalpha(sentence[i]))) {
      if(isalpha(sentence[i+1])){
        sentence[i] = " ";
      }
      else{
        sentence[i] = "";
      }
    }
    else{
      sentence[i] = tolower(sentence[i])
    }
  }
}

void group_words(){
  //i is increments
  //j repetition finder
  for(i = 0, j=0; i < sentence.length; i++){

  }
}

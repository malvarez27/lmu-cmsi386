//11/9/17
#include <cassert>
#include <iostream>

using namespace std;

template <typename T>
class Queue {

  struct Node {
    T data;
    Node* next;
  };

  int size = 0;
  Node* tail = nullptr;
  Node* head = nullptr;

public:
  ~Queue() {
      while (tail != nullptr) {
        //dequeue();
      }
    }
    Queue() = default;
    Queue(const Queue& s)= delete;
    Queue& operator = (const Queue& s) = delete;

    int get_size(){
      return size;
    }
    T get_tail() {
    return tail->data;
    }

    void enqueue(T x) {
      tail = new Node {x, tail};
      if (head == nullptr){
        head = tail;
      }
      size++;
     }

     T dequeue() {
     Node* nodeToDelete = head;
     T valueToReturn = head->data;
     head = head->next;
     size--;
     delete nodeToDelete;
     return valueToReturn;
     }
   };

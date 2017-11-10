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
        dequeue();
      }
    }

    Queue() = default;
    Queue(const Queue& s)= delete;
    Queue& operator = (const Queue& s) = delete;

    Queue(Queue&& s) {
      head = s.head;
      tail = s.tail;
      size = s.size;
      s.head = nullptr;
      s.tail = nullptr;
      s.size = 0;
    }

    Queue& operator = (Queue&& s) {
      if (&s != this) {
        size = s.size;
        head = s.head;
        tail = s.tail;
        s.head = nullptr;
        s.tail = nullptr;
        s.size = 0;
      }
      return *this;
    }

    int get_size(){
      return size;
    }

    T get_tail() {
      return tail->data;
    }

    void enqueue(T x) {
      Node* newNode = new Node {x, nullptr};
      if (head == nullptr) {
        head = newNode;
      } else {
        tail->next = newNode;
      }
      tail = newNode;
      size++;
     }

     T dequeue() {
       if ( head == nullptr) {
         throw underflow_error("EMPTYYYY!");
       }
       Node* nodeToDelete = head;
       T valueToReturn = head->data;
       head = head->next;
       size--;
       if (size == 0) {
         tail = nullptr;
       }
       delete nodeToDelete;
       return valueToReturn;
     }
   };

#include <unordered_map>

class Node {
 public:
  int val;
  Node* next;
  Node* random;

  Node(int _val) {
    val = _val;
    next = NULL;
    random = NULL;
  }
};

class Solution {
 public:
  Node* copyRandomList(Node* head) {
    std::unordered_map<Node*, Node*> o2n;
    auto curr = head;
    while (curr) {
      o2n[curr] = new Node(curr->val);
      curr = curr->next;
    }

    curr = head;

    while (curr) {
      o2n[curr]->next = o2n[curr->next];
      o2n[curr]->random = o2n[curr->random];
    }
    return o2n[head];
  }
};

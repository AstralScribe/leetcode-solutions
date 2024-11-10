

struct ListNode {
  int val;
  ListNode* next;
  ListNode() : val(0), next(nullptr) {}
  explicit ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
 public:
  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode result;
    ListNode* trav = &result;
    int carry = 0;

    while (l1 || l2 || carry) {
      int l1val, l2val;
      if (l1) {
        l1val = l1->val;
        l1 = l1->next;
      } else {
        l1val = 0;
      }
      if (l2) {
        l2val = l2->val;
        l2 = l2->next;
      } else {
        l2val = 0;
      }

      int temp_val = l1val + l2val + carry;
      int out_val = temp_val % 10;
      carry = temp_val / 10;
      trav->next = new ListNode(out_val);
      trav = trav->next;
    }

    return result.next;
  }
};

int main() {
  ListNode l1(2);
  l1.next = new ListNode(4);
  l1.next->next = new ListNode(3);

  ListNode l2(5);
  l2.next = new ListNode(6);
  l2.next->next = new ListNode(4);

  Solution s;
  ListNode* result = s.addTwoNumbers(&l1, &l2);

  return 0;
}

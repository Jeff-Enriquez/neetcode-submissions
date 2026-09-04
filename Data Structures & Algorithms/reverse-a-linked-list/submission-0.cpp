/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* next = nullptr;
        while(curr != nullptr) {
            next = curr->next; // Temporarily store the next pointer
            curr->next = prev; // Reverse the pointer
            prev = curr; // Move prev forward
            curr = next; // Move curr forward
        }
        return prev; // The new head
    }
};

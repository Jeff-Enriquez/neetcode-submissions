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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // Get the first node
        ListNode* head = nullptr;
        if(list1 != nullptr && list2 != nullptr) {
            if(list1->val < list2->val) {
                head = list1;
                list1 = list1->next;
            }
            else {
                head = list2;
                list2 = list2->next;
            }
        }
        else if(list1 != nullptr) {
            return list1;
        }
        else {
            return list2;
        }
        // Store the merged list
        ListNode* merged_list = head;
        while(list1 != nullptr && list2 != nullptr) {
            if(list1->val < list2->val) {
                merged_list->next = list1;
                merged_list = list1;
                list1 = list1->next;
            }
            else {
                merged_list->next = list2;
                merged_list = list2;
                list2 = list2->next;
            }
        }
        if(list1 != nullptr) {
            merged_list->next = list1;
        }
        else if(list2 != nullptr) {
            merged_list->next = list2;
        }
        return head;
    }
};

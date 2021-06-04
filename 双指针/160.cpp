struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(headA && headB){
            ListNode* pA = headA;
            ListNode* pB = headB;
            while(pA!=pB){
                pA = pA==nullptr? headB:pA->next;
                pB = pB==nullptr? headA:pB->next;
            }
        }
        return nullptr;
    }
};
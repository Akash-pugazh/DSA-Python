class Node:
    def __init__(self, data=None, nextPtr=None):
        self.data = data
        self.next = nextPtr


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        tempNode = Node(data, self.head)
        self.head = tempNode

    def print(self, head):
        if head is None:
            return "Empty"
        itr = head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        return llstr

    # ^ Reverse Linked List
    def reverseLL(self):
        curr = self.head
        prev = None
        while curr:
            self.head = self.head.next
            curr.next = prev
            prev = curr
            curr = self.head
        return prev

    def reorderList(self):
        buildPtr = self.head
        tempPtr = self.head
        while tempPtr and tempPtr.next:
            tempPtr = tempPtr.next
            runningPtr = buildPtr
            slowPtr = None
            while runningPtr.next:
                slowPtr = runningPtr
                runningPtr = runningPtr.next
            if tempPtr.next is None:
                break
            slowPtr.next = None
            buildPtr.next = runningPtr
            buildPtr = buildPtr.next
            buildPtr.next = tempPtr
            buildPtr = buildPtr.next
        return self.head


def mergeTwoLL(head1, head2):
    if head1 is None or head2 is None:
        return head1 if head2 is None else head2

    if head1 is None and head2 is None:
        return None

    tempPtr1 = head1
    tempPtr2 = head2

    if tempPtr1.data >= tempPtr2.data:
        finalHead = tempPtr1
        tail = tempPtr1
    else:
        finalHead = tempPtr2
        tail = tempPtr2

    while tempPtr1 or tempPtr2:
        if tempPtr1 is None:
            tail.next = tempPtr2
            return finalHead
        elif tempPtr2 is None:
            tail.next = tempPtr1
            return finalHead
        elif tempPtr1.data >= tempPtr2.data:
            tail.next = tempPtr1
            tempPtr1 = tempPtr1.next
        else:
            tail.next = tempPtr2
            tempPtr2 = tempPtr2.next

    return finalHead


test = LinkedList()

test.insertAtBegin(3)
test.insertAtBegin(1)
test.insertAtBegin(2)
test.insertAtBegin(4)


print(test.print(test.head))


def mergeList(firstHead, secondHead):
    if firstHead is None or secondHead is None:
        return firstHead if secondHead is None else secondHead
    if firstHead is None and secondHead is None:
        return None
    tempPtr1 = firstHead
    tempPtr2 = secondHead
    if tempPtr1.data <= tempPtr2.data:
        finalHead = tempPtr1
        tail = tempPtr1
        tempPtr1 = tempPtr1.next
    else:
        finalHead = tempPtr2
        tail = tempPtr2
        tempPtr2 = tempPtr2.next
    while tempPtr1 and tempPtr2:
        if tempPtr1.data <= tempPtr2.data:
            tail.next = tempPtr1
            tempPtr1 = tempPtr1.next
        else:
            tail.next = tempPtr2
            tempPtr2 = tempPtr2.next
        tail = tail.next

    if tempPtr1 is None:
        tail.next = tempPtr2
        return finalHead
    if tempPtr2 is None:
        tail.next = tempPtr1
        print(finalHead.data, finalHead.next.data, finalHead.next.next)
        return finalHead
    return finalHead


def sortList(head):
    if head.next is None:
        return head
    fPtr = head
    sPtr = head
    while fPtr and fPtr.next and fPtr.next.next:
        fPtr = fPtr.next.next
        sPtr = sPtr.next
    first = head
    second = sPtr.next
    sPtr.next = None
    print(first.data, second.data)
    firstH = sortList(first)
    print(test.print(firstH))
    secondH = sortList(second)
    print(test.print(secondH))
    return mergeList(firstH, secondH)


sortList(test.head)

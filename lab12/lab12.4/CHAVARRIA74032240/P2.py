from LinkedList import LinkedList

def invertirLista(ll):
    prev = None
    curr = ll.getHead()
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    ll.setHead(prev)

ll = LinkedList()
ll.addLast(1)
ll.addLast(2)
ll.addLast(3)
ll.addLast(4)
print(ll)

invertirLista(ll)
print(ll)

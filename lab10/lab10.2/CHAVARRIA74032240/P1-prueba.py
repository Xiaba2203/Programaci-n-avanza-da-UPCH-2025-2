from LinkedList import LinkedList, Stack, add_numbers_as_lists, reverse_stack_iterative, evaluate_postfix

def prueba_linkedlist_y_stack():
    # LinkedList: crear lista 1,2,3
    ll = LinkedList()
    ll.addLast(1)
    ll.addLast(2)
    ll.addLast(3)
    print("LinkedList:", ll)             # debe mostrar [1, 2, 3]
    print("getFirst:", ll.getFirst())   # 1
    print("getLast:", ll.getLast())     # 3

    # Stack: push/pop
    s = Stack()
    s.push(10)
    s.push(20)
    print("Stack peek (esperado 20):", s.peek())
    print("Stack pop (esperado 20):", s.pop())
    print("Stack pop (esperado 10):", s.pop())

def prueba_suma_listas():
    a = LinkedList()
    for d in [5,3,8]: a.addLast(d)    # 5->3->8 = 538
    b = LinkedList()
    for d in [4,8,8]: b.addLast(d)    # 4->8->8 = 488
    res = add_numbers_as_lists(a, b)
    print("538 + 488 ->", res)        # debe mostrar [1, 0, 2, 6]

def prueba_postfix():
    print("3 4 + ->", evaluate_postfix("3 4 +"))            # 7
    print("5 1 2 + 4 * + 3 - ->", evaluate_postfix("5 1 2 + 4 * + 3 -"))  # 14

if __name__ == "__main__":
    prueba_linkedlist_y_stack()
    prueba_suma_listas()
    prueba_postfix()

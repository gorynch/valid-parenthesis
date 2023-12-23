from datetime import datetime

'''
Пример сбалансированных последовательностей скобок:

    (((([{}]))))
    [([])((([[[]]])))]{()}
    {{[()]}}

Несбалансированные последовательности:

    }{}
    {{[(])]}}
    [[{())}]
'''

check_lst = ['(((([{}]))))','[([])((([[[]]])))]{()}','{{[()]}}','}{}','{{[(])]}}','[[{())}]']


# Stack LIFO
class Stack():
    def __init__(self):
        self.lst: list = []

    def is_empty(self) -> bool:
        if len(self.lst) == 0:
            return False
        else:
            return True

    def push(self, new_value):
        self.lst.append(new_value)

    def pop(self):
        if len(self.lst) != 0:
            res = self.lst[len(self.lst)-1]
            self.lst = self.lst[:-1]
            return res
        else:
            return None

    def peek(self):
        if len(self.lst) != 0:
            return self.lst[len(self.lst)-1]
        else:
            return None

    def size(self):
        return len(self.lst)


def check_valid_parenthesis(str_4_check: str) -> bool:
    close_look_up_dict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    if str_4_check[0] in close_look_up_dict:
        my_stack = Stack()
        my_stack.push(str_4_check[0])
        for char in str_4_check:
            try:
                if char != close_look_up_dict[my_stack.peek()]:
                    my_stack.push(char)
                else:
                    my_stack.pop()
            except KeyError:
                return False
    else:
        return False
    return my_stack.is_empty()



if __name__ == '__main__':
    print("\nLet's start")
    print()
    start_time = datetime.now()
    for el in check_lst:
        print(check_valid_parenthesis(el))
    print(f'Done in {datetime.now() - start_time}')

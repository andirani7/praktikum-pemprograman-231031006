# class Node :
    ## TULIS CONSTRUCTOR NODE DISINI ##
    def __init__(self, value):
        self.value = value
        self.next = None

# class Stack :
     ## TULIS CONSTRUCTOR STACK DISINI ## 
    def __init__(self, value):
        node_baru = Node(value)
        self.top = node_baru
        self.height = 1

## fungsi untuk mencetak isi dalam tumpukan (stack)
    def print_stack (self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next       
## fungsi push untuk menambahkan item dalam tumpukan (stack)
    def push (self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else :
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    
## fungsi pop untuk mengeluarkan item dari tumpukan (stack)
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    

## 1 Panggil Class Stack, isi item pertama dengan nomor absen
print('panggil stack')
stk = stack(2)
stk.print_stack()
## 2 Gunakan fungsi push untuk menambahkan item ke dalam stack
#masukkan item sesuai NIM
stk.push(2)
stk.push(2)
stk.push(1)
stk.push(0)
stk.push(1)
stk.push(1)
stk.push(0)
stk.push(9)
stk.push(1)
stk.print_stack()

## 3 Gunakan fungsi pop untuk mengeluarkan item paling yang paling terakhir dimasukkan
print('setelah di pop')
stk.pop()
stk.print_stack()
## 4 Gunakan fungsi print_stack untuk menampilkan isi stack
print('item hasil')
stk.print_stack()
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        self.height = 1
        
class AVL_Tree:
    def __init__(self):
        self.root=None
        self.flag = False
    def insert_Node(self,node,data): 
        if not node:
            return Node(data) 
        elif data < node.data: 
            node.left = self.insert_Node(node.left, data)
        else: 
            node.right = self.insert_Node(node.right, data)
        node.height = 1 + max(self.Height(node.left), self.Height(node.right))
        Balance_Factor = self.get_BalanceFactor(node)
        if Balance_Factor > 1 and data < node.left.data: 
            return self.Right_Rotate(node)
        if Balance_Factor < -1 and data > node.right.data: 
            return self.Left_Rotate(node)
        if Balance_Factor > 1 and data > node.left.data:
            node.left = self.Left_Rotate(node.left)
            return self.Right_Rotate(node)
        if Balance_Factor < -1 and data < node.right.data:
            node.right = self.Right_Rotate(node.right)
            return self.Left_Rotate(node)
        return node
    def Right_Rotate(self, node):
        y = node.left
        Y_Right = y.right
        y.right = node
        node.left = Y_Right
        node.height = 1 + max(self.Height(node.left), self.Height(node.right))
        y.height = 1 + max(self.Height(y.left), self.Height(y.right))
        return y
    def Left_Rotate(self, node):
        y = node.right
        Y_left = y.left
        y.left = node
        node.right = Y_left
        node.height = 1 + max(self.Height(node.left), self.Height(node.right))
        y.height = 1 + max(self.Height(y.left), self.Height(y.right))
        return y
    def Search_Node(self,data):
        if self.root:
            Found = self.Search(data,self.root)
            if Found:
                self.flag = True
    def Search(self,data,current_Node):
        if data > current_Node.data and current_Node.right:
            return self.Search(data,current_Node.right)
        elif data < current_Node.data and current_Node.left:
            return self.Search(data,current_Node.left)
        if data == current_Node.data:
            return True
    def Delete_Node(self, node, key): 
        if not node: 
            return node 
        elif key < node.data: 
            node.left = self.Delete_Node(node.left, key)
        elif key > node.data: 
            node.right = self.Delete_Node(node.right, key) 
        else: 
            if node.left is None: 
                temp = node.right 
                node = None
                return temp 
            elif node.right is None:
                temp = node.left 
                node = None
                return temp 
            temp = self.get_MinimumNode(node.right) 
            node.data = temp.data 
            node.right = self.Delete_Node(node.right, temp.data) 
        if node is None: 
            return node  
        node.height = 1 + max(self.Height(node.left), self.Height(node.right)) 
        Balance_Factor = self.get_BalanceFactor(node) 
        if Balance_Factor > 1 and self.get_BalanceFactor(node.left) >= 0: 
            return self.Right_Rotate(node) 
        if Balance_Factor < -1 and self.get_BalanceFactor(node.right) <= 0: 
            return self.Left_Rotate(node) 
        if Balance_Factor > 1 and self.get_BalanceFactor(node.left) < 0: 
            node.left = self.Left_Rotate(node.left) 
            return self.Right_Rotate(node) 
        if Balance_Factor < -1 and self.get_BalanceFactor(node.right) > 0: 
            node.right = self.Right_Rotate(node.right) 
            return self.Left_Rotate(node) 
        return node
    def get_MinimumNode(self, root): 
        if root is None or root.left is None: 
            return root 
        return self.get_MinimumNode(root.left)
    def get_BalanceFactor(self, node):
        if not node:
            return 0
        return self.Height(node.left) - self.Height(node.right)
    def Height(self, node):
        if not node:
            return 0
        return node.height
    def In_Order(self,node):
        if node != None:
            self.In_Order(node.left)
            print(node.data)
            self.In_Order(node.right) 
            return
    def Pre_Order(self,node):
        if node != None:
            print(node.data)
            self.Pre_Order(node.left)
            self.Pre_Order(node.right)
            return
    def Post_Order(self,node):
        if node != None:
            self.Post_Order(node.left)
            self.Post_Order(node.right)
            print(node.data)
            return
    # def Display(self):
    #     print("a. Insert (add a value in the AVL Tree)")
    #     print("b. search (search an element from the AVL Tree)")
    #     print("c. delete (to delete a value from AVL Tree)")
    #     print("d. Height (print Height of AVL Tree)")
    #     print("e. Preorder Traversal (print elements of AVL Tree in pre-order fashion)")
    #     print("f. In-order Traversal (print elements of AVL Tree in In-order fashion)")
    #     print("g. Post Traversal (print elements of AVL Tree in Post-order fashion)")
    #     print("h. Exist the program")
    #     AVL = AVL_Tree()
    #     while True:
    #         choice = input("pleased enter your choice from a,b,c,d,e,f,g,s,h: ") 
    #         if choice == "a":
    #             loop = input("enter how many time you want to insert node: ")
    #             for i in range(int(loop)):
    #                 N = int(input("please enter the value for node: "))
    #                 AVL.root = AVL.insert_Node(AVL.root,N)
    #         if choice == "b":
    #             Node = int(input("enter the node which you want to seach in tree: "))
    #             AVL.Search_Node(Node)
    #             if(AVL.flag):  
    #                 print("Node exists in the binary tree")  
    #             else:  
    #                 print("Node does not exist in the binary tree") 
    #         if choice == "c":
    #             Value = int(input("Enter the node which you want to delete from Binary tree: "))
    #             if (AVL.flag):
    #                 AVL.Delete_Node(AVL.root,Value)
    #                 print("Deleted")
    #             else:
    #                 print("Node not found")
    #         if choice == "d":
    #             print("The Height of BST is: ",AVL.Height(AVL.root)-1)
    #         if choice == "e":
    #             print("Pre_Order Values")
    #             AVL.Pre_Order(AVL.root)
    #         if choice == "f":
    #             print("In_Order Values")
    #             AVL.In_Order(AVL.root)   
    #         if choice == "g":
    #             print("Post_Order Values")
    #             AVL.Post_Order(AVL.root)
    #         if choice == "h":
    #             print("Program Is stopped")
    #             break
            
AVL = AVL_Tree()
AVL.root = AVL.insert_Node(AVL.root,10)
AVL.root = AVL.insert_Node(AVL.root,12)
AVL.root = AVL.insert_Node(AVL.root,5)
# AVL.In_Order(AVL.root)
# AVL.Delete_Node(AVL.root,10)
# AVL.In_Order(AVL.root)
print(AVL.Height(AVL.root)-1)
# AVL.Display()
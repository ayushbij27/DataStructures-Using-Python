# Node bnanae k liye
class Node:

	def __init__(self,data):
		self.data=data
		self.next=None


# Head initialize krne k liye
class linklist:

	def __init__(self):
		self.head=None

	def push(self,new_data):
		new_node=Node(new_data)
		new_node.next=self.head
		self.head=new_node

	def append(self, new_data):
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node			
			return
		last = self.head	
		while (last.next):
			last = last.next
		last.next =  new_node

	def insert(self,prev_node,new_data):
		if prev_node is None:
			print "No node present "
			return
		new_node=Node(new_data)

		new_node.next=prev_node.next
		prev_node.next=new_node
	
	def pos(self,no):
		temp=self.head
		if no==0:
			self.head=self.head.next
			return		
		for i in range(no-1):
			temp=temp.next
			if temp.next.next is None:
				temp.next=None
				return
		prev=temp	
		temp=temp.next
		prev.next=temp.next

	def dele(self,del_node):
		temp=self.head	
		if (temp is not None):
			if (temp.data==del_node):
				self.head=temp.next
				temp=None
				return
		while(temp is not None):
			if temp.data==del_node:
				break
			prev=temp
			temp=temp.next
		if(temp==None):
			return
		prev.next=temp.next
		temp=None

	def l_size(self):
		temp=self.head
		count=0
		while(temp):
			count+=1
			temp=temp.next
		return count

	def ele_search(self,del_node):
		temp=self.head
		if del_node==temp:
			return True
		while(temp is not None):
			if temp.data == del_node:
				return True
				break	 
			if temp.next is None:
				return False
			else:
				temp = temp.next
		return False

	def swap(self,first,second):
		if self.ele_search(first)==True and self.ele_search(second)==True:
			if(first==second):
				return
			prev_first=None
			curr_first=self.head
			while(curr_first is not None and curr_first.data!=first):
				prev_first=curr_first
				curr_first=curr_first.next

			prev_second=None
			curr_second=self.head
			while(curr_second is not None and curr_second.data!=second):
				prev_second=curr_second
				curr_second=curr_second.next
			a=raw_input("for data swapping press 1 else press 2")
			if (a==1):
				temp=curr_first.data
				curr_first.data=curr_second.data
				curr_second.data=temp
			else:
				prev_first.next= curr_second
				prev_second.next=curr_first
				temp=curr_first.next
				curr_first.next=curr_second.next
				curr_second.next=temp
		else:
			print("Data to be swapped is not present")

	def nthnode(self,pos):
		count=0
		temp=self.head
		if(pos==0):
			return temp
		while(pos!=0):
			temp=temp.next
			pos=pos-1
		print temp.data

	def mid_ele(self):
		if((self.l_size())% 2==0):
			self.nthnode((self.l_size()+1)/2)
		else:
			self.nthnode((self.l_size())/2)

	def end_linklist(self,pos):
		self.nthnode(self.l_size()-pos)

	def count_occ(self,value):
		temp=self.head
		count=0
		while(temp is not None):
			if(temp.data==value):
				count+=1
				temp=temp.next
			else:
				temp=temp.next
		print count		

	def rev(self):
		prev=None
		temp=self.head
		while(temp is not None):
			curr=temp
			curr.next=prev
			prev=curr
			temp=temp.next
			
	def printList(self):
		temp = self.head
		while (temp):
			print temp.data,
			temp = temp.next

if __name__=='__main__':
	llist= linklist()
	llist.append(4)
	llist.push(1)
	llist.insert(llist.head.next, 8)
	llist.insert(llist.head, 4)
	llist.append(0)
	llist.append(4)
	llist.append(6)
	llist.printList()
	print("\n")
	llist.count_occ(6)
	print("\n")
	# llist.nthnode(3)
	# print("\n")
	# llist.mid_ele()
	# print("\n")
	# llist.printList()
	# print("\n")
	llist.end_linklist(3)
	print("\n")
	llist.rev()
	llist.printList()
	# llist.swap(2,9)
	# print("\n")
	# print llist.l_size()
	# print("\n")
	# llist.printList()

	# print("\n")
	# llist.pos(3)
	# llist.pos(4)
	# print llist.l_size()
	# llist.printList()
	# print("\n")
	# llist.pos(5)
	# print llist.l_size()
	# print("\n")
	# print llist.ele_search(8)
	# llist.printList()	
	
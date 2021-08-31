# �������� ����
data = [20,6,8,12,78,32,65,32,7,9]
tree = BinarySearchTree()

# Ʈ�� ������ �ϼ�
for x in data: 
	tree.insert(x)

# Ʈ�� ���� ������ ���翡 ���� Ȯ�� �� ����
print(tree.find(9))
print(tree.find(3))

print(tree.delete(78))
print(tree.delete(6))
print(tree.delete(11))

# Ʈ�� ������ ������ ���
print("\n@@@@@@@")
tree.DFTravel() # ���� �켱 Ž�� �� ���� ��ȸ : �Ѹ� > ���� Ʈ�� > ������ Ʈ��
print("\n=====")
tree.LFTravel() # ���� �켱 Ž�� �� ���� ��ȸ : ���� Ʈ�� > �Ѹ� > ������ Ʈ��
print("\n*****")
tree.LRTravel() # ���� �켱 Ž�� �� ���� ��ȸ : ���� Ʈ�� > ������ Ʈ�� > �Ѹ� ���
print("\n&&&&&")
tree.layerTravel() # �ʺ� �켱 Ž�� : �Ѹ� ������ ���̼����� �湮
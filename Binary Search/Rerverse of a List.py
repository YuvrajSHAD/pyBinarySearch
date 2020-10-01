def reverse_l(li):
    length= len(li)
    first=list(n.split())
    for a in range(len(first)):
        li[a]=int(first[a])
    for i in range(length//2):
        li[i],li[(length-i)-1]=li[(length-i)-1],li[i]
n=input("Enter items for List: ")
reverse_l(li)
print(li)
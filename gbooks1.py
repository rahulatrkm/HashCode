from collections import OrderedDict
f = open("/home/rahul/hashcode/e.txt", "r")
lines = f.readlines()
fo = open("ope.txt", "w")
b, l, d = map(int,lines[0].split())
score = list(map(int,lines[1].split()))
score_dict = {}
for i in range(b):
    score_dict[i] = score[i]
sorted_score = OrderedDict(sorted(score_dict.items(), key=lambda x: x[1]), reverse=True)
curr = 2
lib_signup = []
library = {}
for i in range(l):
    n, t, m = map(int,lines[curr].split())
    curr += 1
    book_ids = list(map(int,lines[curr].split()))
    curr_lib_score = 0
    for book_id in book_ids:
        curr_lib_score += score_dict[book_id]
    curr += 1
    library[i] = set(book_ids)
    lib_signup.append((i,n,t,m, curr_lib_score))

book_signed = set()
lib_signup = sorted(lib_signup, key=lambda x: (d-x[1])*x[2]*x[3], reverse=True)
#print(lib_signup)
temp = []
i,j = 0, len(lib_signup)-1
while i<j:
    temp.append(lib_signup[i])
    temp.append(lib_signup[j])
    i += 1
    j -= 1

if len(lib_signup) % 2 != 0:
    temp.append(lib_signup[i])
lib_signup = temp

cnt = 0
curr_d = 0
ans = []
for num in lib_signup:
    if (curr_d+num[2]) < d:
        curr_d += num[2]
        cnt += 1
        num_of_books_from_lib = min(num[3]*(d-curr_d), num[1])
        #print(num_of_books_from_lib, "days", curr_d, d)
        books = []
        if num_of_books_from_lib == num[1]:
            book_signed = book_signed.union(library[num[0]])
            books = list(library[num[0]])
            #print(list(library[num[0]]))
        else:
            new_books = library[num[0]] - book_signed
            if len(new_books) <= num_of_books_from_lib:
                num_of_books_from_lib = len(new_books)
                book_signed.union(new_books)
                books = list(new_books)
            elif len(new_books) > num_of_books_from_lib:
                cnt_of_added_books = 0
                for curr_book in sorted_score:
                    if curr_book in new_books:
                        books.append(curr_book)
                books = books[:num_of_books_from_lib]
        #print([num[0], num_of_books_from_lib])
        #print(books)
        books = ' '.join(list(map(str, books)))
        ans.append([str(num[0])+' ' + str(num_of_books_from_lib), books])
print(cnt)
fo.write(str(cnt)+'\n')
for i in range(len(ans)):
    print(ans[i][0])
    fo.write(ans[i][0]+'\n')
    print(ans[i][1])
    fo.write(ans[i][1]+'\n')
f.close()
fo.close()

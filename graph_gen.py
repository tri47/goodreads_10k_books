import pandas as pd
df = pd.read_csv("ratings.csv")
b = pd.read_csv("books.csv")
#b = b.sample(20)
b = b[0:200]
top_books = b['book_id'].to_list()
#df = df[df['book_id'] in top_books]
df = df[df['rating'].isin([5])]
df = df[df['book_id'].isin(top_books)]
print(df)
books = {}
book_list = []

df = df.reset_index()
for i in range(0,df.shape[0]):
    book = df.loc[i,'book_id']
    user = df.loc[i,'user_id']

    if book not in books:
        books[book] = []
    books[book].append(user)

for key, val in books.items():
    book_list.append((key,val))

ofile = open('out.csv',"w+")
for i in range(0,len(book_list)-1):
    print('book ', i)
    for j in range(i+1,len(book_list)):
        b1 = book_list[i][0]
        b2 = book_list[j][0]
        common_users = list(set(book_list[i][1]) & set(book_list[j][1]))
        count = len(common_users)
        if count > 2000:
            line = str(b1) + ',' + str(b2) + '\n'#+ ',' + str(count) + '\n'
            ofile.write(line)
ofile.close()

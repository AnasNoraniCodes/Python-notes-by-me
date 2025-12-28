#Tables 

def table_generator(current_table_value):
    #new file create ki hai aor name diya hai
    with open(f'Tables of {current_table_value}.txt','w') as file:
        #loop se new table file main 1 se 10 tak table ki value print ki hai
        #range 11 pe aa ke jump kr jati hai
        for i in range(1,11):
            #table ka formula...
            data = f'{current_table_value} X {i} = {current_table_value*i}\n'
            #har line print ki hai...
            file.write(data)
         
     

# range is used here to tell the amout of tables we need...
for table_value in range(1,21):
    table_generator(table_value)



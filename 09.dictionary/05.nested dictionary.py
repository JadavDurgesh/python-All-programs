men = {

      1 :{
              'que' : '(1) what is name ?',

              'ans': 'my name is durgesh'
            },

      2 :{

              'que' : '(2) whow your you ?',

              'ans': 'i am fain'
      }
}

size = len(men)
print(size)

for i in range(1,size+1):
    print("men = ", men[i]['que'])

    ans = input("enter the your ans = ")
    
    if men[i]['ans'] == ans:
        print("raght answer...")
    else:
        print("rong answer...")
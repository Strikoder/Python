print('''
 __ __   ___   __ __  ____       _      ____  _____   ___      ____  ____       __    __    ___    ___  __  _  _____
|  T  T /   \ |  T  T|    \     | T    l    j|     | /  _]    l    j|    \     |  T__T  T  /  _]  /  _]|  l/ ]/ ___/
|  |  |Y     Y|  |  ||  D  )    | |     |  T |   __j/  [_      |  T |  _  Y    |  |  |  | /  [_  /  [_ |  ' /(   \_ 
|  ~  ||  O  ||  |  ||    /     | l___  |  | |  l_ Y    _]     |  | |  |  |    |  |  |  |Y    _]Y    _]|    \ \__  T
l___, ||     ||  :  ||    \     |     T |  | |   _]|   [_      |  | |  |  |    l  `  '  !|   [_ |   [_ |     Y/  \ |
|     !l     !l     ||  .  Y    |     | j  l |  T  |     T     j  l |  |  |     \      / |     T|     T|  .  |\    |
l____/  \___/  \__,_jl__j\_j    l_____j|____jl__j  l_____j    |____jl__j__j      \_/\_/  l_____jl_____jl__j\_j \___j
''')
age = int(input("Please enter your age:"))
days=(90-age)*365
weeks=(90-age)*48
months=(90-age)*12
print(f"if you lived until 90, then you have {days} days left or in another way {weeks} weeks left or let's say {months} months left")
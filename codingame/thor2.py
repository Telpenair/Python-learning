import time

#игра про Тора на КодГейминг. Нужно привести к Силе
#есть позиция Тора initial_cx и initial_cy
#позиция Силы light_x и light_y
#есть 8 сторон, в которые может пойти Тор

#из интересного - конкатенция строк для создания направления, упрощает код раза в 4

#из заметок от себя настоящего - нужно понятно называть ВСЕ переменные

start_time = time.time()

light_x, light_y, initial_tx, initial_ty = 36, 17, 0, 0

print('yep')
print(light_x == initial_tx, light_y == initial_ty, initial_tx < 0, initial_ty < 0)

while (light_x != initial_tx or light_y != initial_ty) and initial_tx >= 0 and initial_ty >= 0 :
    print('yep')
    if ( light_x > initial_tx):
        a='E'
        initial_tx+=1

    elif light_x == initial_tx :
        a=''

    else :
        a='W'
        initial_tx-=1

    
    if (light_y > initial_ty):
        b='S'
        initial_ty+=1

    elif light_y == initial_ty :
        b=''

    else:
        b='N'
        initial_ty-=1

    c=a+b
        
    
    print(c, '  ', initial_tx, '  ', initial_ty)

print("--- %s seconds" % (time.time() - start_time))

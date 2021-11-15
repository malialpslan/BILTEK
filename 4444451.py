print("Lütfen değerleri virgül ile ayırarak oluşturmak istediğiniz matrisin değerlerini giriniz:")
v_1 = list(map(int, input().split(",")))
print("Lütfen değerleri virgül ile ayırarak oluşturmak istediğiniz matrisin değerlerini giriniz:")
v_2 = list(map(int, input().split(",")))
if len(v_1) != len(v_2):
    print("Uzunluklar eşit olmadan çarpım yapamazsınız!!")
else:
    a_list = []
    for i in range(0,len(v_1)):
        a_list.append(v_1[i] * v_2[i])
        sum_list = sum(a_list)
    print(sum_list)

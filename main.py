def print_meniu():
    print("1. Citire lista")
    print("2. Cea mai lunga subsecventa cu toate numerele palindrom")
    print("3. Cea mai lunga subsecventa cu toate nr avand acelasi nr de divizori")
    print("4. Cea mai lunga subsecventa cu suma numerelor numar prim")
    print("5. Iesire")

def citire_lista():
    list=[]
    n = int(input("Numarul de elemente:"))
    for i in range(n):
        list.append(int(input()))
    return list

def oglindit(n):
    nr=0
    while n!=0:
        nr=nr*10+n%10
        n=n//10
    return nr

def is_palindrome(n):
    if n==oglindit(n):
        return True
    return False

def test_is_palindrome():
    assert is_palindrome(5)==True
    assert is_palindrome(12)==False
    assert is_palindrome(12321)==True

def toate_palindrom(list):
    for x in list:
        if is_palindrome(x)==False:
            return False
    return True

def get_longest_all_palindromes(list):
    secv_max=[]
    for i in range(len(list)):
        for j in range(i,len(list)):
            if toate_palindrom(list[i:j+1]) and len(list[i:j+1])>len(secv_max):
                secv_max = list[i:j+1]
    return secv_max

def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([3, 4, 5]) == [3,4, 5]
    assert get_longest_all_palindromes([12, 3, 131, 24]) == [3, 131]
    assert get_longest_all_palindromes([19, 12]) == []

def numar_divizori(x):
    n=2
    d=2
    while d!=x:
        if x%d==0:
            n=n+1
        d=d+1
    return n

def test_numar_divizori():
    assert numar_divizori(5)==2
    assert numar_divizori(10)==4
    assert numar_divizori(24)==8

def toate_acelasi_nr(list):
    k=numar_divizori(list[0])
    for x in list:
        if numar_divizori(x)!=k:
            return False
    return True

def get_longest_same_div_count(list):
    secv_max=[]
    for i in range(len(list)):
        for j in range(i,len(list)):
            if toate_acelasi_nr(list[i:j+1]) and len(list[i:j+1])>len(secv_max):
                secv_max = list[i:j+1]
    return secv_max

def test_get_longest_same_div_count():
    assert get_longest_same_div_count([3, 4,9]) == [4,9]
    assert get_longest_same_div_count([12, 3, 5, 7]) == [3, 5, 7]
    assert get_longest_same_div_count([24, 4, 5, 13, 19, 28]) == [5, 13, 19]

def prim(p):
    if p<2:
        return False
    else:
        for i in range(2,p//2+1):
            if p%i==0:
                return False
    return True

def test_prim():
    assert prim(7)==True
    assert prim(15)==False
    assert prim(29)==True

def toate_suma_prim(list):
    s=0
    for x in list:
        s=s+x
    if prim(s)==False:
        return False
    return True

def  get_longest_sum_is_prime(list):
    secv_max = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if toate_suma_prim(list[i:j + 1]) and len(list[i:j + 1]) > len(secv_max):
                secv_max = list[i:j + 1]
    return secv_max

def test_get_longest_sum_is_prime():
    assert get_longest_sum_is_prime([5, 1, 2, 3, 1]) == [5,1, 2, 3]
    assert get_longest_sum_is_prime([1,2]) == [1,2]
    assert get_longest_sum_is_prime([1, 1,5,5,3]) == [1,1,5]

def main():
    list=[]
    while True:
        print_meniu()
        option = int(input("Alegeti optiunea:"))
        if option == 1:
            list = citire_lista()
        elif option == 2:
            rezultat = get_longest_all_palindromes(list)
            print(rezultat)
        elif option==3:
            rez = get_longest_same_div_count(list)
            print(rez)
        elif option==4:
            rezz = get_longest_sum_is_prime(list)
            print(rezz)
        elif option == 5:
            break
        else:
            print("optiune invalida ! Reincercati !")
    test_is_palindrome()
    test_numar_divizori()
    test_prim()
    test_get_longest_all_palindromes()
    test_get_longest_same_div_count()
    test_get_longest_sum_is_prime()

if __name__ == '__main__':
    main()

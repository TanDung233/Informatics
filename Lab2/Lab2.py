def main():
    a = input("Input: ").strip()
    c = list(a)

    print("Original Message:", message(c))
    
    S = syndromeS(c)
    print("Syndrome S(s1;s2;s3) = ", S)
    
    n = checkdefine(c, S)
    correct(c, n)
    
    print("Correct Message:", message(c))

def message(c):
    return c[2] + c[4] + c[5] + c[6]

def syndromeS(c):
    s = ['0', '0', '0']

    if ((int(c[0])+int(c[2])+int(c[4])+int(c[6])) % 2 ==0):
        s[0] = '0'
    else:
        s[0] = '1'

    if ((int(c[1])+int(c[2])+int(c[5])+int(c[6])) % 2 ==0):
        s[1] = '0'
    else:
        s[1] = '1'

    if ((int(c[3])+int(c[4])+int(c[5])+int(c[6])) % 2 ==0):
        s[2] = '0'
    else:
        s[2] = '1'

    return ''.join(s)

def checkdefine(c, S):
    if S == "000":
        print("No error")
        return 1
    elif S == "001":
        print(f"Error in bit r3 (r3= {c[3]})")
        return 1
    elif S == "010":
        print(f"Error in bit r2 (r2= {c[1]})")
        return 1
    elif S == "011":
        print(f"Error in bit i3 (i3= {c[5]})")
        return 5
    elif S == "100":
        print(f"Error in bit r1 (r1= {c[0]})")
        return 1
    elif S == "101":
        print(f"Error in bit i2 (i2= {c[4]})")
        return 4
    elif S == "110":
        print(f"Error in bit i1 (i1= {c[2]})")
        return 2
    else:
        print(f"Error in bit i4 (i4= {c[6]})")
        return 6

def correct(c, n):
    if n != 1:
        if c[n] == '1':
            c[n] = '0'
        else:
            c[n] = '1'

main()

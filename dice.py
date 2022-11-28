
# 주사위 게임

# 같은 눈이 3개가 나오면 10000원 + (같은눈)*1000
one,two,three = map(int,(input().split()))

if one == two == three:
    print(10000+one *1000)

elif one == two or two == three :
        print(1000+ two*100)
elif one ==three:
    print(1000+one*100)
else:
    print(max(one,two,three)*100)
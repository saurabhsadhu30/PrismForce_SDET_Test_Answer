def can_cross_chakravyuha(p, a, b, k):
    n = len(k)
    skipped = [False] * n
    recharge_count = b
    skip_count = a

    for i in range(n):
        if skip_count > 0 and k[i] > p:
            skipped[i] = True
            skip_count -= 1
            continue

        if p < k[i]:
            return False  
        else:
            p -= k[i]

        if i == 2 or i == 6:
            k[i] //= 2  
            if i < n - 1 and not skipped[i + 1] and recharge_count > 0:
                p -= k[i]  
                if p < 0:
                    return False  
                recharge_count -= 1  

        if recharge_count > 0:
            p *= 2
            recharge_count -= 1

    return True  

def main():
    p = int(input("Enter initial power (p): "))
    a = int(input("Enter number of skips allowed (a): "))
    b = int(input("Enter number of recharges allowed (b): "))
    n = int(input("Enter the number of enemies: "))
    
    k = []
    print("Enter the power of each enemy: ")
    for _ in range(n):
        k.append(int(input()))

    if can_cross_chakravyuha(p, a, b, k):
        print("Abhimanyu can cross the Chakravyuha.")
    else:
        print("Abhimanyu cannot cross the Chakravyuha.")

if __name__ == "__main__":
    main()

#task1
def filter_list(l):
    filtered =[]
    for x in l:
        if type(x) != str:
            filtered.append(x)
    return filtered
#task2
def first_non_repeating_letter(word):
  char_order = []
  ctr = {}
  for c in word:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None
#task3
def digital_root(num):
    if (num == "0"):
        return 0

    ans = 0
    for i in range(0, len(num)):
        ans = (ans + int(num[i])) % 9

    if (ans == 0):
        return 9
    else:
        return ans % 9
#task4
def pairs_count(arr, n, target):
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                count += 1
    return count
#task5
def party_list(str):
    str = str.split(';')
    res = []
    for i in str:
        i = i.upper().split(':')
        i[0], i[1] = i[1], i[0]
        res.append(i[0]+', '+i[1])
    res = sorted(res)
    str = ''
    for i in res:
        str += '('+i+'),'
        str = str.strip(',')
    return str
#extra task1
def nextBigger(intnum):
    new_number = [str(i) for i in str(intnum)]
    new_number.sort(reverse=True)
    bigger_number = int(''.join(new_number))
    if (bigger_number > intnum):
        return bigger_number
    else:
        return -1
#extra_task2
def ip_adress(ip):
    ip = '{:032b}'.format(ip)
    ip = list(str(ip))
    total_result = ''
    for i in range(4):
        result = ''
        for j in range (i*8,i*8+8):
             result+=ip[j]
        total_result+=str(int(result,base=2))+'.'
    total_result = total_result.strip('.')
    return total_result

def main():
    list1 = [1, 2, 'a', 'b']
    list2 = [1, 'a', 'b', 0, 15]
    list3 = [1, 2, 'aasf', '1', '123', 123]

    print("First task results")

    print(filter_list(list1))
    print(filter_list(list2))
    print(filter_list(list3))

    print("Second task results")

    print(first_non_repeating_letter('sTreSS'))
    print(first_non_repeating_letter('stress'))
    print(first_non_repeating_letter('SsTtRr'))

    print("Third task results")

    print(digital_root('120347'))
    print(digital_root('735'))

    print("Fourth task results")

    arr = [1, 3, 6, 2, 2, 0, 4, 5]
    n = len(arr)
    target = 5
    print("Count of pairs is", pairs_count(arr, n, target))

    print("Fifth task results")

    print(party_list("Fred:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))

    print("Extra task 1 results")
    number1 = 34535
    print("Example 1 next number is", nextBigger(number1))
    number2 = 294358724
    print("Example 2 next number is", nextBigger(number2))

    print("IP adress example 1: ",ip_adress(2149583361))
    print("IP adress example 2: ",ip_adress(32))
    print("IP adress example 3: ", ip_adress(0))


if __name__=='__main__':
    main()
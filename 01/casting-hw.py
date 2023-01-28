""" def getLetterVal(letter):
    letterValue = ord(letter) - ord('a')
    print(letterValue)
    return letterValue

def castHomework(s, target, kmax):
    st_arr = []

    for i in range(len(s)-1,-1,-1):
        for j in range(len(st_arr)):
            st_arr.append(s[i]+st_arr[j])
        st_arr.append(s[i])

    for element in st_arr:
        print(element) """
def castHomework(givenString, givenTarger, givenK):
    return ""


givenString = input()
givenTarget, givenK = input()
givenTarget = int(givenTarget)
givenK = int(givenK)
castHomework(givenString, givenTarget, givenK)

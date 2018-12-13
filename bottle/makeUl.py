import sys

def uw(fn):
    def w():
        ul = fn()
        if ul[0] != '<ul>':
           ul.insert(0, '<ul>')
        if ul[-1] != '</ul>':
           ul.append('</ul>')

        for i in range(1, len(ul)-1):
            ul[i] = '   <li>' + ul[i] + '</li>'
        return ul
    return w



@uw
def re_l():
    if len(sys.argv)<2:
        num = int(input('input num:\n'))
    else:
        num = int(sys.argv[1])
    print('repeat num is {}'.format(num))
    l=[]
    while num>0:
        l.append(input('\ninput text:\n'))
        num -=1
    return l


if __name__ == '__main__':
    ul = re_l()

    for i in ul:
        print(i)

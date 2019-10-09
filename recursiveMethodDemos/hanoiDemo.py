'''
 * 汉诺塔
 *      有柱子 x z y，最终将x上的n个圆盘借助z移动到y上
 *      递归思想：
 *          1.将x上的n-1个放入到z上，借助y
 *          2.将x上的n圆盘放到y上
 *          3.将z上的n-1个圆盘放入y
 * @param n
 * @param plfrom
 * @param pltmp
 * @param plto
 '''
def  hanoi(number = 3, plfrom = 'A', pltmp = 'B', plto = 'C'):
    i = 0
    if number > 0:
        i = hanoi(number - 1, plfrom, plto, pltmp)
        print("take " + str(number) + " from " + plfrom + " to " + plto)
        i += 1
        i += hanoi(number - 1, pltmp, plfrom, plto)
        print("steps are ", i)
    return i

step = hanoi(20)
print(step)


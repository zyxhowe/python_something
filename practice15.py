#学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

def stratified(x):
    if x>=90:
        return 'A'
    elif x>=60:
        return 'B'
    else:
        return 'C'
    
n=int(input())

print(stratified(n))

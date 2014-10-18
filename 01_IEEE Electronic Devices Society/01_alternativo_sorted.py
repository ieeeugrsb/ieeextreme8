# -*- coding: utf-8 -*-

import random

#first_line = raw_input().split()

#N = int(first_line[0]) #Longitud secuencia
N = 100
#M = int(first_line[1]) #Longitud subsecuencia
M = 10
#K = int(first_line[2])
K = 9

#n_str = raw_input().split() #secuencia
n_str = []

for i in range(N):
    n_str.append(str(random.randint(1,10)))
    
n_str = ['74', '32', '28', '42', '5', '51', '57', '5', '59', '86', '55', '50', '18', '58', '75', '91', '20', '36', '87', '62']

print n_str

print "generado"

menor = 2147483647 #mayor numero posible

n=[]

for s in n_str: 
    n.append(int(s))

s = sorted(n)
e_anterior = -1
idx = 0
print s
for e in s:
    if e_anterior != e:
        print idx
        idx+=1
    e_anterior = e
    
    if idx == K:
        print e
        break
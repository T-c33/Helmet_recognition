

list =[[0.01851852 ,0.03814262],
 [0.02363636 ,0.046875  ],
 [0.0320122  ,0.05930931],
 [0.0671875  ,0.11378455],
 [0.01219512 ,0.02491694],
 [0.01485608 ,0.03198653],
 [0.046      ,0.07883987],
 [0.10533333 ,0.18      ],
 [0.19666667 ,0.33670886]]

result = []
for i in list:
    i[0] = i[0] * 416.0
    i[1] = i[1] * 416.0
    result.append([i[0],i[1]])

print(result)

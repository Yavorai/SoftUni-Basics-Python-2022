import math
n = int(input())
l = int(input())
b_ascii = 97
b2_ascii = 97
for a in range(1, n + 1):
    for a2 in range(1, n + 1):
        for b in range(b_ascii, b_ascii + l):
            c = chr(b)
            for b2 in range(b2_ascii, b2_ascii + l):
                c2 = chr(b2)
                for d in range(max(a,a2) + 1, n + 1):
                    print(f'{a}{a2}{c}{c2}{d}',end=' ')
#========================================
# function solve([arg1, arg2]) {
#   let n = Number(arg1);
#   let l = Number(arg2);
#   for (let b = 1; b <= n; b++) {
#     for (let b2 = 1; b2 <= n; b2++) {
#       for (let c1ascii = 97; c1ascii < 97 + l; c1ascii++) {
#         let c1 = String.fromCharCode(c1ascii);
#         for (let c2ascii = 97; c2ascii < 97 + l; c2ascii++) {
#           let c2 = String.fromCharCode(c2ascii);
#           for (let b3 = Math.max(b, b2) + 1; b3 <= n; b3++) {
#             process.stdout.write(`${b}${b2}${c1}${c2}${b3} `);
#           }
#         }
#       }
#     }
#   }
#   console.log();
# }
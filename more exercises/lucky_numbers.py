number = int(input())
result = ''

for a in range(1, 9 + 1):
    for b in range(1, 9 + 1):
        for c in range(1, 9 + 1):
            for d in range(1, 9 + 1):
                if (a + b) == (c + d) and (number % (a + b) == 0):
                    result += f'{a}{b}{c}{d} '
print(result)
#============================================
# function luckyNumbers(input) {
#   let N = Number(input);
#   let stringResult = '';
#   for (let a = 1; a <= 9; a++) {
#     for (let b = 1; b <= 9; b++) {
#       for (let c = 1; c <= 9; c++) {
#         for (let d = 1; d <= 9; d++) {
#           // if ((d <= 9) && ((a + b) === (c + d)) && (d > 0) && (a + b === N)) {
#           if (((a + b) === (c + d)) && (N % (a + b) === 0)) {
#             // console.log(`${a}${b}${c}${d}`);
#             stringResult += `${a}${b}${c}${d}` + ' ';
#           }
#         }
#       }
#     }
#   }
#   console.log(stringResult)
# }
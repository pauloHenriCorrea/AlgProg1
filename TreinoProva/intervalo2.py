N = int(input())
in_ = 0
out_ = 0

for i in range(N):
    x = int(input())

    if x >= 10 and x <= 20:
        in_ += 1
    else:
        out_ += 1
        
print(str(in_) + " in\n" + str(out_) + " out")

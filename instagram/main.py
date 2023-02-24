
start = 0
end = 0

with open("main.tex") as tex:
    for (n, l) in enumerate(tex):
        if l == "\\begin{tikzpicture}\n":
            start = n
        if l == "\\end{tikzpicture}\n":
            end = n

print(start)
print(end)
texfile = open("tex.tex", 'w')
with open("main.tex") as tex:
    for (n, l) in enumerate(tex):
        if n >= start and n <= end:
            print(l)
            texfile.write(l)


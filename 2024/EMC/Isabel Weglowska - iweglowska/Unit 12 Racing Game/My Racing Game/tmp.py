
row = 10

g = """
00012011020010021
11011000111000010
00011010000100100
01100010100001002
00000100100010000
10111001010000100
10100010011000001
00120000102111012
00111111100100010
01211000000101000
00000000000001000
""".split("\n")[row+1]



for i in range(len(g)):
    print(f'<td id="R{row}C{i}" { """class="wall" """ if g[i] == "1" else ("""class="fly" """ if g[i]=="2" else "")}/>')
            
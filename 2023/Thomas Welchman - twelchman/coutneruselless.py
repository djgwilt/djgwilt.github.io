w = 0
e=0
for i in range(17):
    print("<tr>")
    for i in range(40):
        print(' <td id="R{}C{}"></td>'.format(e,w))
        w +=1
    print("</tr>")
    e+=1
    w = 1

html = "<html><body><table>"
html += "<tr>"
for i in range(1, 11):
    html += "<td><a href=http://" + str(i) + ".ru>" + str(i) + "</a></td>"
html += "</tr>"
for i in range(2, 11):
    html += "<tr>"
    for j in range(1, 11):
        html += "<td><a href=http://" + str(i * j) + ".ru>" + str(i * j) + "</a></td>"
    html += "</tr>"
html += "</table></body></html>"
print(html)

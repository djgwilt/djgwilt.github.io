from os import walk
from re import search,match
from glob import glob
import os

links = {}

def test_folder(path):
    res = search(r'([^\./\\]*) - ',path)
    if not res:
        return False
    name = res.group(1)
    if os.path.isfile(f"{path}/index.html"):
      links[name] = f"{path}/index.html"
      return True
    elif os.path.isfile(f"{path}/document.html"):
      links[name] = f"{path}/document.html"
      return True
    else:
      return False

staff = ["DJG","EMC","GXD","IMA","SAG"]

for s in staff:
  students = glob(f"{s}/*")
  for student in students:
      test_folder(f"{student}") or test_folder(f"{student}/My Racing Game") or test_folder(f"{student}/Unit 12 Racing Game/My Racing Game")

patterns = (
  r'\A[a-c]',
  r'\A[d-g]',
  r'\A[h-j]',
  r'\A[k-m]',
  r'\A[n-r]',
  r'\A[s-z]'
)

headings = [p.upper().replace("\\A","").replace("[","").replace("]","") for p in patterns]

txt_url = [(txt,url) for txt,url in links.items()]
txt_url.sort()

sections = ["\n".join(f"<li><a href='{url}'>{txt}</a></li>" for txt,url in txt_url if match(p,txt.lower())) for p in patterns]

tds = [f"""
      <td>
        <h2>{headings[i]}</h2>
        <ul>
        {sections[i]}
        </ul>
      </td>
      """ for i in range(len(patterns))]

trs = "\n".join([f"""
    <tr>
      {tds[3*i + 0]}
      {tds[3*i + 1]}
      {tds[3*i + 2]}
    </tr>
""" for i in range(2)])

head = """
<head>
  <title>Year 9 Games</title>
  <style>

    body {
      background-color:MediumPurple;
    }
    
    h1 {
      color:white;
      font-size:30px;
      font-family: "Palatino Linotype";
    }

    h2 {
      color:white;
      font-size:20px;
      font-family:"Palatino Linotype";
    }

    a {
      color:white;
      font-size:15px;
      font-family:"Palatino Linotype";
    }

    table {
        border-collapse: collapse;
        width: 100%;
    }

    th, td {
        text-align: left;
        padding: 8px;
    }

    th {
        background-color: #4CAF50;
        color: white;
    }
  </style>
</head>
"""

body = f"""
<body>
  <h1>Year 9 Racing Games June 2023</h1>
  <table> {trs} </table>
</body>
"""

site = f"""
<!DOCTYPE html>
<html>
{head}
{body}
</html>
"""

with open('index.html','w') as f:
    print(site,file=f)
    
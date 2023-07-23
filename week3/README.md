# Week 3
## 用到的知識點:
### Python
#### urllib.request
*  urllib.request.Request(url, headers={
    "Content-Type":"application/json",
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
   })
*  with urllib.request.urlopen(request) as response:
    result = response.read().decode("utf-8")
#### json
* json.loads()
#### csv
* with open("attraction.csv", mode="w", newline="") as file:
    writer=csv.writer(file)
*  .writerow()
#### bs4
*  bs4.BeautifulSoup( ,"html.parser")
####
*  string.split("")
*  dict.update({ : })
*  list.append()
*  .find()
*  .find_all()
*  .find_previous_sibling()
*  .get()
*  .previous_sibling
*  .next_sibling
*  .get_text()
### HTML
*  <script src="task3&4.js"></script>
### Javascript
*  let promise = fetch(url, [options ( method[get or post], header... )]).then([function]).catch((error)=>{})
*  response.json();
*  document.getElementById("down")
*  .addEventListener("click", function(e){})
*  document.createElement("<tag name>")
*  .createTextNode("")
*  .appendChild(object)

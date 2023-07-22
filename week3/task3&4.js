function createTopData(start, data){
    let end = start+3;
    for(i=start; i<end; i++){
        //console.log( i, data[i]["stitle"], data[i]["file"].split("https://")[1]);
        var top = document.getElementById("top");
        let topContainer = document.createElement("div");
        topContainer.className="top_container";
        let topPhoto = document.createElement("img");
        topPhoto.className="top_photo";
        topPhoto.src="http://" + data[i]["file"].split("https://")[1];
        let topText = document.createElement("div");
        topText.className="top_text";
        let text = document.createTextNode(data[i]["stitle"]);
        topText.appendChild(text);
        topContainer.appendChild(topPhoto);
        topContainer.appendChild(topText);
        top.appendChild(topContainer);
    }
}
function createDownData(start,data){
    let end=start+12;
    if(end>data.length){
        end=data.length;
    }
    for(i=start; i<end; i++){
        //console.log( i, data[i]["stitle"], data[i]["file"].split("https://")[1]);
        var down = document.getElementById("down");
        let container = document.createElement("div");
        container.className="container";
        let photo = document.createElement("img");
        photo.className="photo";
        photo.src="http://" + data[i]["file"].split("https://")[1];
        let content = document.createElement("div");
        content.className="content";
        let text = document.createElement("div");
        text.className="text";
        let newText = document.createTextNode(data[i]["stitle"]);
        text.appendChild(newText);
        content.appendChild(text);
        container.appendChild(photo);
        container.appendChild(content);
        down.appendChild(container);
    }
}
function loadMore(n, data){
    createDownData( n, data)
    if(n+12<data.length) return n+12;
    else return data.length;
}
fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
.then((response) => {
    return response.json();
})
.then((responseJson) => {
    let data=responseJson.result.results;
    createTopData( 0, data);
    createDownData( 3, data);
    var n = 15;
    let button = document.getElementById("button");
    button.addEventListener("click", function(e){
        if(n<data.length){
            n=loadMore(n ,data);
        }
        else{
            alert('沒有資料了');
        }
    })
})
.catch((error) => {
    console.log(`Error: ${error}`);
})




var allText
function readTextFile(file)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                allText = rawFile.responseText;
            }
        }
    }
    rawFile.send(null);
}

function changeColorBox()
{
    var url_string = window.location; //window.location.href
    var url = new URL(url_string);
    var path = url.searchParams.get("c");
    readTextFile(path);
    var split_data = allText.split(/\r?\n/);
    for (var i = 0;i < split_data.length;i++){
        split_data2 = split_data[i].split(",");
        var cell_ID = split_data2[0];
        var cell_color = split_data2[4];
        document.getElementById(cell_ID).style.backgroundColor = cell_color;
    }

    //Get value from pameter

}
var list = [];
var test = ""
var test2 = ""
var path = ""
var menu1_path = "SaturnHD/DirName.txt"
var menu2_path = "SaturnHD/RP01/txt_Name.txt"
var menu1_text
var menu2_text
var allText

function setup() {
  readTextFile(menu1_path);
  menu1_text = allText;
  readTextFile(menu2_path);
  menu2_text = allText;
  test = menu1_text;
  test2 = menu2_text;
  console.log(test);
  console.log(test2);


  var select = document.getElementById("select"), main1 = test.split(/\r?\n/);

             for(var i = 0; i < main1.length; i++)
             {
                if (main1[i].search("RP") == 0){
                 var option = document.createElement("OPTION"),
                     txt = document.createTextNode(main1[i]);
                 option.appendChild(txt);
                 option.setAttribute("value",main1[i]);
                 select.insertBefore(option,select.lastChild);
                 }
                 else{
                    console.log(main1[i]);
                 }
             }

  var select2 = document.getElementById("select2"), main2 = test2.split(/\r?\n/);

             for(var i = 0; i < main2.length; i++)
             {
                if (main2[i].search("WW") == 0){
                 var option2 = document.createElement("OPTION"),
                     txt2 = document.createTextNode(main2[i].replace(".txt",""));
                 option2.appendChild(txt2);
                 option2.setAttribute("value",main2[i].replace(".txt",""));
                 select2.insertBefore(option2,select2.lastChild);
                 }
                 else{
                    console.log(main2[i].replace(".txt",""));
                 }
             }
}
function openMenu(evt, tabMenu) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabMenu).style.display = "block";
    evt.currentTarget.className += " active";
}
    function getSelectValue()
        {
        var selectedValue = document.getElementById("select").value;
        console.log(selectedValue);
        }
    getSelectValue();

    function getSelectValue2()
        {
            var selectedValue2 = document.getElementById("select2").value;
            console.log(selectedValue2);
        }
    getSelectValue2();

function openData(evt, tabMenu) {

    //document.getElementById(tabMenu).style.display = "block";
    var selectedValue = document.getElementById("select").value;
    var selectedValue2 = document.getElementById("select2").value;
    //selectedValue2 = selectedValue2.replace(".txt","");
    var FTempPath = "SaturnHD/" + selectedValue + "/" + selectedValue2 + ".txt"
    console.log(FTempPath)

    evt.currentTarget.className += " active";
    alert(selectedValue + "/" + selectedValue2);
    //FTemp.html?vname=value
    //FTemp_data_link
    var selectlink = document.getElementById("FTemp_data_link");
    selectlink.setAttribute('href','FTemp.html?c='+FTempPath);
}

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


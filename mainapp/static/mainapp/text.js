function convert() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        data=JSON.parse(this.responseText).data
      document.getElementById("text").innerHTML = data;
    }
    xhttp.open("GET", "getdata/"+document.getElementById("src_lang_code").value+"/"+document.getElementById("tgt_lang_code").value+"/"+document.getElementById("input").value, true);
    xhttp.send();
  }
function newRequest(method, url, body) {
    return new Promise((res, rej) => {
        let req = new XMLHttpRequest;
        req.onload = () => {
            if (req.status == 200) {
                res(req)
            } else {
                rej('Fail');
            }

        }
        req.open(method, url);
        req.send(body);
    }
    );
};

function getAllAccounts(){
    newRequest("GET", "/server/getAllAccounts").then((res) => {
        let resObj = JSON.parse(res.responseText);
        let var1 = document.getElementById(someid);
        var1.appendChild(resObj);
    }).catch((rej) => {console.log(rej)});
};

function addAnAccount(){
    let Stringfn = document.getElementById("FirstName").value;
    let Stringln = document.getElementById("LastName").value;
    let JSONString = "{firstname:" + Stringfn + "," + "lastname:" + Stringln + "}";
    newRequest("POST", "/server/addAccount", JSONString).then((res) => {
        let resObj = JSON.parse(res.responseText);
        let var1 = document.getElementById(someid);
        var1.appendChild(resObj);
    }).catch((rej) => {console.log(rej)});
};

function newRequest(method, url, body) {
    return new Promise((res, rej) => {
        let req = new XMLHttpRequest();
        req.onload = () => {
            if (req.status == 200) {
                res(req)
            } else {
                rej(req);
            }

        }
        req.open(method, url);
        req.send(body);
    });
}

function getAllAccounts(){
    newRequest("GET", "/server/getAllAccounts").then((res) => {
        let resObj = JSON.parse(res.responseText);
        let var1 = document.getElementById("someid");
	console.log(resObj);
        var1.innerText = resObj;
    }).catch((rej) => {console.log(rej)});
}

function addAnAccount(){
    let Stringfn = document.getElementById("FirstName").value;
    let Stringln = document.getElementById("LastName").value;
    let account = accMaker(Stringfn, Stringln);
    newRequest("POST", "/server/addAccount", JSON.stringify(account)).then((res) => {
        let resObj = JSON.parse(res.responseText);
        let var1 = document.getElementById(someid);
        let newAcc = accMakerObj(resObj);
        console.log(newAcc);
    }).catch((rej) => {console.log(rej.responseText)});
}

function accMaker(fName, lName){
    const acc = {
        firstName: fName,
        lastName: lName
    }
    return acc;
}

function accMakerObj(accObj){
    const acc = {
        firstName: accObj.firstName,
        lastName: accObj.lastName,
        accountNumber: accObj.accountnumber,
        prize: accObj.prize
    }
    return acc;
}

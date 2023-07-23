function findGetParameter(parameterName) {
    let result = null;
    location.search.substr(1).split("&").forEach(function (item) {
        let tmp = item.split("=");
        if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
    });
    return result;
}

function mdToHtml(text) {
    var converter = new showdown.Converter();
    return converter.makeHtml(text);
}

function copyToClipboard(elementId) {
    const content = document.getElementById(elementId).innerHTML;

    function listener(e) {
        e.clipboardData.setData("text/html", content);
        e.clipboardData.setData("text/plain", content);
        e.preventDefault();
    }

    document.addEventListener("copy", listener);
    document.execCommand("copy");
    document.removeEventListener("copy", listener);
}


function htmlDecode(input) {
  var doc = new DOMParser().parseFromString(input, "text/html");
  return doc.documentElement.textContent;
}

const translate = () => {
  const text = document.getSelection().toString();
  fetch("http://localhost:5009", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      // your expected POST request payload goes here
      text,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      // enter you logic when the fetch is successful
      console.log(data.translation);
      navigator.clipboard.writeText(htmlDecode(data.translation));
    })
    .catch((error) => {
      // enter your logic for when there is an error (ex. error toast)
      console.log(error);
    });
};

document.onkeydown = function (e) {
  if (e.ctrlKey && e.keyCode == 84) {
    translate();
  }
};

function htmlDecode(input) {
  var doc = new DOMParser().parseFromString(input, "text/html");
  return doc.documentElement.textContent;
}

const translate = () => {
  text = document.getSelection().toString();
  const encodedParams = new URLSearchParams();
  encodedParams.append("q", text);
  encodedParams.append("target", "en");
  encodedParams.append("source", "uk");

  const options = {
    method: "POST",
    headers: {
      "content-type": "application/x-www-form-urlencoded",
      "Accept-Encoding": "application/gzip",
      "X-RapidAPI-Key": "9c26b1418bmsh010a810df6744cap1fa314jsn9ac5abbcdec5",
      "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
    },
    body: encodedParams,
  };

  fetch(
    "https://google-translate1.p.rapidapi.com/language/translate/v2",
    options
  )
    .then((response) => response.json())
    .then((response) =>
      navigator.clipboard.writeText(
        htmlDecode(response?.data?.translations[0]?.translatedText)
      )
    )
    .catch((err) => console.error(err));
};

document.onkeydown = function (e) {
  if (e.ctrlKey && e.keyCode == 84) {
    // translate(document.getSelection().toString());
    translate();
  }
};

const translates = () => {
  fetch("http://localhost:5009", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      // your expected POST request payload goes here
      text: "Круто",
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      // enter you logic when the fetch is successful
      console.log(data);
    })
    .catch((error) => {
      // enter your logic for when there is an error (ex. error toast)
      console.log(error);
    });
};

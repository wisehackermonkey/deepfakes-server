// summit script for ml deepfake website
// by oran collins
// github.com/wisehackermonkey
// oranbusiness@gmail.com
// 20200407
const CORS_REVERSE_PROXY = "http://localhost:10900/"
const SERVER_URL = "http://requestbin.net/r/1383i921" //"http://64.227.84.118:8080/function/figlet"

const TEST_IMAGE_URL = "https://i.imgur.com/N0OfBon.png";
const TEST_VIDEO_URL = "https://i.imgur.com/N0OfBon.png";

let send_deepfake = async (json_data) => {
  try {
    //  NOTE: to fix cors issues im sending all the data to a redocly/cors-anywhere (docker) server
    // that turns a access-control-allow-origin: * for all requests sent to
    // CORS_REVERSE_PROXY + reqested url
    // EX:
    //  redocly/cors-anywhere  URL           actual requests
    //  http://localhost:10900/  +   http://64.227.84.118:8080/function/figlet
    let server_response = await fetch(CORS_REVERSE_PROXY + SERVER_URL, {
      method: "POST",
      mode: "cors",
      headers: {
        "Content-Type": "text/plain", //"application/json",
        "Access-Control-Allow-Origin": "http://64.227.84.118:8080",
        origin: "*",
      },
      body: JSON.stringify(json_data),
    })
      .then((response) => response.text()) //or use .json is being set back to client
      .then((data) => {
        return data;
      });

    console.log(server_response);

  } catch (error) {
    console.error("ERROR inside function send_deepfake(): " + error);
  }
};

window.onload = () => {
  console.log("DeepFake Generator");
  console.log("Wait someone is looking at the console???");
  console.log("note from developer: the code is super ugly heads up!");
  console.log("Any questions feel to email me at oranbusiness@gmail.com");

  let image_url_field_element = document.getElementById("image_text_box_field");
  let GenerateButton = document.getElementById("GenerateButton");

  image_url_field_element.focus();
  image_url_field_element.select();

  let summit_button = GenerateButton.addEventListener("click", (e) => {
    console.log("Sending data to deepfake Generator server");
    // alert(
    //   "Please be patient, this can take up to 15 minuts to complete! so get a coffee its going to bee a while :)"
    // );

    let image_url_element = document.getElementById("image_text_box");
    let video_url_element = document.getElementById("video_text_box");

    // TODO
    // var jobValue = document.getElementsByName('txtJob')[0].value  // first element in DOM  (index 0) with name="txtJob"

    let json_data = { image: TEST_IMAGE_URL, video: TEST_VIDEO_URL };
    console.log(TEST_IMAGE_URL + " " + TEST_VIDEO_URL);

    send_deepfake(json_data);

    image_url_element.value = ""; //clean out text box after submit to stop resumiting
  });
};

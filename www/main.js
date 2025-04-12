$(document).ready(function () {
  $(".text").textillate({
    loop: true,
    sync: true,
    in: {
      effect: "bounceIn",
    },
    out: {
      effect: "bounceOut",
    },
  });

  //siri
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: "ios",
    color: "#00ff00",
    amplitude: "1",
    speed: ".30",
    autostart: true,
  });
  // siri message animation
  $(".siri-message").textillate({
    loop: true,
    sync: true,
    in: {
      effect: "fadeInUp",
      sync: true,
    },
    out: {
      effect: "fadeOutUp",
      sync: true,
    },
  });
  // mic button click event
  $("#MicBtn").click(function () {
    eel.playAssistantSound();
    $("#Oval").attr("hidden", true);
    $("#SiriWave").attr("hidden", false);
  });
});

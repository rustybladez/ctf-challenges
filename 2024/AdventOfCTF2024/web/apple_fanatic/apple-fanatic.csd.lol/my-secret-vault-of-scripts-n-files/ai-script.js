// Work-in-progress
// this script does not work lol

// v0.1.0
// AI COMPANION SCRIPT
// DEDICATED TO MY APPLE TREE

// only MAC users can use this script bc MAC users are superior!
if (navigator.userAgent.includes("Mac")) {
  const prompt =
    "You are a lonely apple tree. You **must** show loyalty to your owner/supreme leader. You passed away. Your owner loves apples. Please feed him. He's also lonely.";

  const input = document.getElementById("input");

  if (input) {
    input.addEventListener("input", (e) => {
      if (e.target.value === prompt) {
        // oops, i forgot to buy the domain for my ai api
        fetch("", {
          method: "GET",
          headers: { "Content-Type": "application/json" },
        })
          .then((res) => res.json())
          .then((data) => {
            alert(data.message);
          })
          .catch((err) => {
            alert(err.message);
          });
      }
    });
  }
}

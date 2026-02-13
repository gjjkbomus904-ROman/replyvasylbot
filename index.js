const { spawn } = require("child_process");

const process = spawn("python", ["bot.py"]);

process.stdout.on("data", data => {
  console.log(`stdout: ${data}`);
});

process.stderr.on("data", data => {
  console.error(`stderr: ${data}`);
});

let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().trim().split("\n");

let n = Number(input[0]);

n = 10
let dp = new Array(n + 1).fill(n + 1);
let count = 1;

if (n % 3 === 0) {
  dp[n / 3] = Math.min(count, dp[n / 3]);
}
if (n % 2 === 0) {
  dp[n / 2] = Math.min(count, dp[n / 2]);
}
dp[n - 1] = Math.min(count, dp[n - 1]);
count++;
console.log(dp, count)

while (dp[1] === n + 1) {
    console.log('before loop', dp, count)
  for (let i = 0; i < dp.length; i++) {
    if (dp[i] !== count - 1) {
      continue;
    }
    if (i % 3 === 0) {
      dp[i / 3] = Math.min(count, dp[i / 3]);
    }
    if (i % 2 === 0) {
      dp[i / 2] = Math.min(count, dp[i / 2]);
    }
    dp[i - 1] = Math.min(count, dp[i - 1]);
  }

  count++;
  console.log('after loop', dp, count)
}

console.log(dp[1]);
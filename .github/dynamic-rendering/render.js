const Mustache = require("mustache");
const fs = require("fs");
const request = require("sync-request");
const README_MUSTACHE_FILE = "./.github/dynamic-rendering/main.mustache";
const README_FILE = "README.md"
const INDEX_MUSTACHE_FILE = "./.github/dynamic-rendering/index.mustache";
const INDEX_FILE = "docs/index.md"

/** Functions to retrieve data from github API */

function getContributors() {
  let apiEndPoint = "https://api.github.com/repos/ia-z/ia-z/contributors"
  let headers = { "User-Agent": "request" }
  let response = request("GET", apiEndPoint, { headers })
  let parsedResponse = JSON.parse(response.getBody("utf8"))
  return parsedResponse
    .filter(contributor => contributor.type.toLowerCase() !== "bot")
    .sort((c1, c2) => c2.contributions - c1.contributions)
    .map(contributor => {
      return {
        avatar: contributor.avatar_url,
        login: contributor.login,
        github_profile: contributor.html_url,
        width_markup: "150px",
        width_avatar: "36px"
      }
    })
}

/** Define DATA to be rendered through Mustache */

const contributors = getContributors()

let DATA = {
  title: "IA-Z",
  isBuilding: true,
  contributors: contributors,
  contributors_length: contributors.length
}

/**
 * Generate README from Mustache Template
 * @param {Object} mustacheData 
 */
function generateReadMe(mustacheData) {
  fs.readFile(README_MUSTACHE_FILE, (err, data) => {
    if (err) throw err;
    const output = Mustache.render(data.toString(), mustacheData);
    fs.writeFileSync(README_FILE, output);
  });
}

/**
 * Generate index (main website page) from Mustache Template
 * @param {Object} mustacheData 
 */
function generateIndex(mustacheData) {
  fs.readFile(INDEX_MUSTACHE_FILE, (err, data) => {
    if (err) throw err;
    const output = Mustache.render(data.toString(), mustacheData);
    fs.writeFileSync(INDEX_FILE, output);
  });
}

generateReadMe(DATA);
generateIndex(DATA);

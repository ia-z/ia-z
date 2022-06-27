const Mustache = require("mustache");
const fs = require("fs");
const request = require("sync-request");
const MUSTACHE_FILE = "./.github/dynamic-rendering/main.mustache";
const README_FILE = "README.md"

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
                width_markup: "20%",
                width_avatar: "20%"
            }
        })
}

/** Define DATA to be rendered through Mustache */

let DATA = {
    title: "IA-Z",
    isBuilding: true,
    contributors: getContributors()
}

/**
 * Generate README from Mustache Template
 * @param {Object} mustacheData 
 */
function generateReadMe(mustacheData) {
    fs.readFile(MUSTACHE_FILE, (err, data) => {
      if (err) throw err;
      const output = Mustache.render(data.toString(), mustacheData);
      fs.writeFileSync(README_FILE, output);
    });
}
  
generateReadMe(DATA);
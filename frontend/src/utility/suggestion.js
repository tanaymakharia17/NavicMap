
const getSuggestion = (places, input) => {
    // sort(options, input);
    if (input.length === 0) return new Array();

    let closestOption = {};

    for (let place of places) {
        closestOption[place] = distance(place.toLowerCase(), input);
    }

    let sortable = Object.fromEntries(
        Object.entries(closestOption).sort(([, a], [, b]) => a - b)
    );

    return Object.keys(sortable).slice(0, 6);
}

const distance = (target, source) => {
    let tLen = target.length;
    let sLen = source.length;

    let dp = new Array(tLen + 1);
    for (let i = 0; i <= tLen; i++) dp[i] = new Array(sLen + 1);

    for (let i = 0; i <= tLen; i++) dp[i][0] = i;
    for (let i = 0; i <= sLen; i++) dp[0][i] = i;

    for (let i = 1; i <= tLen; i++) {
        for (let j = 1; j <= sLen; j++) {
            if (target[i - 1] === source[j - 1]) dp[i][j] = dp[i - 1][j - 1];
            else dp[i][j] = Math.min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1;
        }
    }

    return dp[tLen][sLen];
}

exports.getSuggestion = getSuggestion;
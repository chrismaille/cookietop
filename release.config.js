module.exports = {
    branch: 'master',
    repositoryUrl: "https://github.com/noverde/cookietop",
    plugins: [
        '@semantic-release/commit-analyzer',
        '@semantic-release/release-notes-generator',
        '@semantic-release/github'
    ]
}

## What is this about?

This is a Python experiment to identify technologies and APIs used in a Devpost project. I'll start by retreiving a json representation of the project using our unofficial API. Then I'll search the project's title, tagline, description, and author contributions statements for common keywords (node.js, python, elasticsearch, heroku, etc.), normalize them (node.js / node js / node are all the same thing), and return an array of tags.

## Why bother?

Most hackers only tag languages and key APIs. Hosting providers, build tools, and other tech almost never gets captured. I want to improve the likelihood that a mentioned tech/api will be tagged. If we can suggest tags based on the project description, users could then just click "add all" or whatever and be on their way. 

## And then what?

If this all works out, I want to think about relationships between tags. Is a project hosted on heroku more likely to be a RoR project? If so, maybe we could suggest that tag even if RoR isn't mentioned explicitly. Or hey, are you building a webapp with node? Well then you're probably using express or some other common framework. 

## Bruh&hellip;

Hey, if you've got some feedback, better ideas, whatevers, I'd love to hear it. 

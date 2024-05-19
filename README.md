# LectureMe

<!-- ![LectureMe Logo](logo.png) -->

LectureMe is a revolutionary tool that transforms lengthy lecture recordings into concise, engaging reels! It uses advanced AI algorithms to identify key points and condense hours of content into bite-sized, digestible formats!

## Features

- **AI-Powered Summarization**: Our advanced AI algorithm identifies and extracts key points from your lecture recordings.
- **High-Quality Audio**: LectureMe ensures that the audio quality is preserved during the condensation process.
- **Easy Sharing**: Share your reels easily with classmates or keep them for future reference.
<!-- - **Customizable Length**: You can specify the desired length of your reel, and LectureMe will adjust accordingly. -->

<!-- ## Installation

```bash
git clone https://github.com/yourusername/LectureMe.git
cd LectureMe
pip install -r requirements.txt -->

## Links

GitHub repo: https://github.com/aransaseelan/LectureMe

## Inspiration

As we were brainstorming for an idea to pursue in this Hackathon competition, one of our friends was scrolling to TikTok and came across a movie organized into a short series of digestible clips. He was fully encaptivated by this format and was not even aware of us attempting to interact with him. From this, we instantly realized that this format of sharing information is very effective in delivery and could be applied to our everyday life in school in regards to the way lecture are being implemented. This led us to LectureMe.


## What it Does

LectureMe is a project that aims to make the lectures more engaging and understandable. The user is required upload a URl of their recorded lecture and the project will convert this into an .mp4 file, find the most important and key moments of the full video, and return them in small, comprehensible videos. This is then delivered in a "scrollable" format.


## How We Built It

LectureMe is a multi-component application built with a combination of technologies. The frontend is developed using React, which is housed in the `frontend/lectureme` directory. It provides a user-friendly interface for uploading lecture recordings and viewing the generated summaries.

The backend is written in Python and is located in the `server` directory. It uses various libraries and APIs to process the uploaded videos. The `MainPointsAPI.py` script is responsible for identifying and extracting key points from the lecture transcripts. The `VideoCutter.py` script then uses these key points to cut the original video into smaller, digestible clips.

The entire application is orchestrated using Node.js, as specified in the `package.json` files in both the frontend and backend directories. This setup allows for seamless integration between the frontend and backend, making LectureMe a cohesive and efficient tool for lecture summarization.


## Accomplishments That We're Proud Of

Having found a way to download the video to our local device from simply using a URL, finding the "highlights" and cutting them accordnigly while seamlessly integrating the backend and frontend components has proven to be something that we are truly proud of.

## Challenges We Ran Into

The biggest challenge we ran into is project management and figuring out how to divide up the tasks among our group. As this is our first in-person hackathon, we were finding it hard to assign tasks and work with deadlines; however, we were able to overcome that and deliver this project on time.


## What We Learned

1. How to work on a new project within a short timeframe and minimal instructions

2. How to implement Flask to define routes (endpoints) that the application will respond to.


## What's Next?

1. More dashboard features

2. Data management

4. Login system

5. Saving video conversions to history

And more!

import './App.css';
import {Image} from 'react-native';
import React, {useState} from 'react';
import TextField from '@material-ui/core/TextField';
<<<<<<< Updated upstream
import cloudinary from 'cloudinary-video-player';
=======
>>>>>>> Stashed changes
import "cloudinary-video-player/cld-video-player.min.css";
import 'cloudinary-video-player/chapters';
import 'cloudinary-video-player/playlist';


function App() {
  const [hidden, setHidden] = useState(true);
  const [hidden2, setHidden2] = useState(true);
  const [hidden3, setHidden3] = useState(true);
  const [hiddenClip, setHiddenClip] = useState(true);
<<<<<<< Updated upstream
=======
  const [hiddenSupport, setHiddenSupport] = useState(true);
>>>>>>> Stashed changes
  const startRef = React.useRef();
  const [inputValue, setInputValue] = useState('');

  async function fetchVideos() {
    try {
        const youtubeLink = document.getElementById('youtubeLink').value;
        const response = await fetch(`/fetch_videos/${encodeURIComponent(youtubeLink)}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });
        
        if (!response.ok) {
            throw new Error(`Server error: ${response.statusText}`);
        }

        const videos = await response.json();

        if (!Array.isArray(videos)) {
            throw new Error('Invalid response format');
        }

        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';


        videos.forEach(video => {
            const videoElement = document.createElement('div');
            videoElement.innerHTML = `<video>${video}</video>`;
            resultsDiv.appendChild(videoElement);
        });
    } catch (error) {
        // const resultsDiv = document.getElementById('results');
        // resultsDiv.innerHTML = `<p>Error fetching videos: ${error.message}</p>`;
    }
}


  return (
    <div className="App">
      <header className="App-header">
        <div id="header">
          <h1 id="main-text">LectureMe</h1>
          <h1 id="log-in">log in</h1>
          <div id="get-started" onClick={() => startRef.current.scrollIntoView({behavior: 'smooth'})}>
            get started
          </div>
        </div>
        <div id="hero">
          <h1 id="hero-text">Learn <span id="gradient-text">smarter</span>. Use your time <span id="gradient-text">better</span>.<br />Get <span id="gradient-text">LectureMe</span>.</h1>
          <div id="glass-cover"></div>
<<<<<<< Updated upstream
          <TextField id="new-text-field" label="Enter a YouTube link" variant="filled" style={{position: 'relative', top: '50vh'}}
            onKeyDown={(event) => {
              setHiddenClip(false);
            }} />
=======
          <TextField 
            id="new-text-field" 
            ref={startRef}
            label="Enter a YouTube link" 
            variant="filled" 
            style={{position: 'relative', top: '50vh', backgroundColor: 'white', borderRadius: '10px', width: '50%'}} 
            value={inputValue}
            onChange={(event) => setInputValue(event.target.value)}
            onKeyDown={(event) => {
              
              setTimeout(() => {
                setHiddenClip(false);
              }, 3000);

              if (event.key === 'Enter') {
                fetchVideos(inputValue);
                event.preventDefault(); // Prevent form submission
              }
            }}
          />
>>>>>>> Stashed changes
          <Image source={require('./television.png')} id="tv-pic" onMouseEnter={() => setHidden(false)} onMouseLeave={() => setHidden(true)} />
          <Image source={require('./orb.png')} id="orb-pic" onMouseEnter={() => setHidden2(false)} onMouseLeave={() => setHidden2(true)} />
          <Image source={require('./gba.png')} id="gba-pic" onMouseEnter={() => setHidden3(false)} onMouseLeave={() => setHidden3(true)}/>
          {hidden ? null : <h1 id="test">take your long, <br /> boring videos...</h1>}
          {hidden2 ? null: <h1 id="test2">transform them using<br />our AI algorithm...</h1>}
          {hidden3 ? null : <h1 id="test3">and get all the<br />important takeaways!</h1>}
<<<<<<< Updated upstream
          {hiddenClip ? null : <video src='./test-assets/Mind-bending new programming language for GPUs just dropped.mp4'></video>}
          <div id="video-enter" ref={startRef}></div>
          <p id="youtube-link">Enter a YouTube link:</p>
=======
          <div id="video-enter">
            {hiddenClip ? null : <video src="/test-assets/video.mp4" controls id="main-video" onClick={(event) => {
              setTimeout(() => {
                setHiddenSupport(false);
              }, 3000);
            }}/>}
          </div>
          {hiddenSupport ? null : <video class="support-videos" src="/clipped/clip0.mp4" controls style={{position: 'relative', top: '-50vh', width: '50%', height: '50%'}}/>}
          {hiddenSupport ? null : <video class="support-videos" src="/clipped/clip1.mp4" controls style={{position: 'relative', top: '-50vh', width: '50%', height: '50%'}}/>}
          {hiddenSupport ? null : <video class="support-videos" src="/clipped/clip2.mp4" controls style={{position: 'relative', top: '-40vh', width: '50%', height: '50%'}}/>}
          {hiddenSupport ? null : <video class="support-videos" src="/clipped/clip4.mp4" controls style={{position: 'relative', top: '-40vh', width: '50%', height: '50%'}}/>}
>>>>>>> Stashed changes
          {/* <video
            id="demo-player"
            controls
            autoplay
            class="cld-video-player">
          </video> */}
<<<<<<< Updated upstream
=======


          <script>

          </script>

>>>>>>> Stashed changes
        </div>
      </header>
    </div>
  );
}

export default App;

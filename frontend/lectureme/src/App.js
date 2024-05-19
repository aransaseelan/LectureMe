import './App.css';
import {Image} from 'react-native';
import React, {useState} from 'react';
import {TextField} from '@material-ui/core';
import cloudinary from 'cloudinary-video-player';
import "cloudinary-video-player/cld-video-player.min.css";
import 'cloudinary-video-player/chapters';
import 'cloudinary-video-player/playlist';


function App() {
  const [hidden, setHidden] = useState(true);
  const [hidden2, setHidden2] = useState(true);
  const [hidden3, setHidden3] = useState(true);
  const startRef = React.useRef();

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
          <Image source={require('./television.png')} id="tv-pic" onMouseEnter={() => setHidden(false)} onMouseLeave={() => setHidden(true)} />
          <Image source={require('./orb.png')} id="orb-pic" onMouseEnter={() => setHidden2(false)} onMouseLeave={() => setHidden2(true)} />
          <Image source={require('./gba.png')} id="gba-pic" onMouseEnter={() => setHidden3(false)} onMouseLeave={() => setHidden3(true)}/>
          {hidden ? null : <h1 id="test">take your long, <br /> boring videos...</h1>}
          {hidden2 ? null: <h1 id="test2">transform them using<br />our AI algorithm...</h1>}
          {hidden3 ? null : <h1 id="test3">and get all the<br />important takeaways!</h1>}
          <div id="video-enter" ref={startRef}></div>
          <TextField id="filled-basic" label="Filled" variant="filled" />
          <video
            id="demo-player"
            controls
            autoplay
            class="cld-video-player">
          </video>
          
        </div>
      </header>
    </div>
  );
}

export default App;

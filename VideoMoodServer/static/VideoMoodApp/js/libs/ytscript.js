/*
 * Change out the video that is playing
 */

// Update a particular HTML element with a new value
function updateHTML(elmId, value) {
	document.getElementById(elmId).innerHTML = value;
}

// Loads the selected video into the player.
function nextVideo() {
	//var video1 = "ylLzyHk54Z0";
	//var video3 = "GMUlhuTkM3w";
	//var videoID = video3;
    videos_now = videos_now + 1;
    if (videos_now>=videos_length){ 
		videos_now =0;
	}
    if(ytplayer) {
		ytplayer.loadVideoById(videos[videos_now]);
	}
    
}

function sleep(ms)
{
	var dt = new Date();
	dt.setTime(dt.getTime() + ms);
	while (new Date().getTime() < dt.getTime());
}



// This function is called when an error is thrown by the player
function onPlayerError(errorCode) {
	alert("An error occured of type:" + errorCode);
}

// This function is automatically called by the player once it loads
function onYouTubePlayerReady(playerId) {
	ytplayer = document.getElementById("ytPlayer");
	setInterval(updatePlayerInfo, 0);
	updatePlayerInfo();
	ytplayer.addEventListener("onStateChange", "onPlayerStateChange");
	ytplayer.addEventListener("onError", "onPlayerError");
}


// Display information about the current state of the player
function updatePlayerInfo() {
	// Also check that at least one function exists since when IE unloads the
	// page, it will destroy the SWF before clearing the interval.
	if(ytplayer && ytplayer.getDuration) {
		var duration = ytplayer.getDuration();
		var currentTime = ytplayer.getCurrentTime();
		if (duration!=0 && duration-currentTime<=0) {
			//alert("LOAD NEW VIDEO: duration-" + duration +" current:"+ currentTime);
			nextVideo();
		}
	}
}


// The "main method" of this sample. Called when someone clicks "Run".
function loadPlayer() {
	// The video to load
	//var videoID = "ylLzyHk54Z0"
		// Lets Flash from another domain call JavaScript
		var params = { allowScriptAccess: "always" };
	// The element id of the Flash embed
	var atts = { id: "ytPlayer" };
	// All of the magic handled by SWFObject (http://code.google.com/p/swfobject/)
	swfobject.embedSWF("http://www.youtube.com/v/" + videos[0] +
			"?version=3&enablejsapi=1&playerapiid=player1",
			"videoDiv", "480", "295", "9", null, null, params, atts);
}

function _run() {
    loadPlayer();
}
// Copyright 2018 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

'use strict';

chrome.runtime.onInstalled.addListener(function (details) {
  if (details.reason == "install") {
    chrome.app.window.create('options.html', {
      bounds: {
        'width': 1024,
        'height': 768
       }
      
       });
  } 
});



function load_popup(data){

  
  if('email' in data){

    document.getElementById("configured").style.display="inline";
    document.getElementById("not-configured").style.display="none";

    
    document.getElementById("email").innerHTML=data.email;
    
    document.querySelector("#logslink a").onclick = function () {
      chrome.tabs.create({active: true, url: "https://streaming-sniffer-api.nextnet.top/"+data.email+"/logs"});
  };
    
  
    changeColor.onclick = function(element) {
      
      chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        chrome.tabs.executeScript(
            tabs[0].id,
            {code:`
            for(let a of document.querySelectorAll("#content #contents #contents a#thumbnail")){
              const xhr = new XMLHttpRequest();
              xhr.open('POST', 'https://streaming-sniffer-api.nextnet.top/`+data.email+`/'+a.href.substring(32,43));
              xhr.send();
            }
            `});
      });
    };
    }
    else{
  
      document.getElementById("not-configured").style.display="inline";
      document.getElementById("configured").style.display="none";
      let submit = document.getElementById('submit');
  submit.addEventListener('click', function() {
        let email=document.getElementById("name").value;
        chrome.storage.sync.set({email: email}, function() {
          console.log('email saved ' + email);
          const xhr = new XMLHttpRequest();
          xhr.open('POST', 'https://streaming-sniffer-api.nextnet.top/'+email);
          xhr.send();
          xhr.onreadystatechange=function(){
            if (xhr.readyState==4 && xhr.status==200){
              chrome.storage.sync.get(['email'], function(data2) {
                load_popup(data2);
              });
            }
          };
        });
      });
    }
  
}
chrome.storage.sync.get(['email'], function(data) {
  load_popup(data);
});


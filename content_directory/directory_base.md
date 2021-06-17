---
layout: page
title: Notes index
---
<style>
    /* @import url(https://fonts.googleapis.com/css?family=Roboto);

body{
  font-family: "Roboto", "Sans Serif";
  font-size: 18pt;
  color: #000000;
  background: #FFFFFF;
} */

ul{
  list-style: none;
  /* margin: 0; */
  padding: 0;
}

label{
  cursor: pointer;
  padding: 10px;
  border-bottom: none;
}

ul ul li{
  padding: 10px;
  background: #FFFFFF;
}


input[type="checkbox"]{
  position: absolute;
  left: -9999px;
}

input[type="checkbox"] ~ ul{
  height: 0;
  transform: scaleY(0);
}

input[type="checkbox"]:checked ~ ul{
  height: 100%;
  transform-origin: top;
  transition: transform .2s ease-out;
  transform: scaleY(1); 
}


</style>
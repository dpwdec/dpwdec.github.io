---
layout: page
title: 📂
---
<style>

ul{
  list-style: none;
  padding: 0;
  margin-bottom: 2px;
  margin-top: 0px;
}

label{
  cursor: pointer;
  border-bottom: none;
  font-weight: 450 
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

/* turns the check into a closed folder by target labels AFTER an input */
input + label:before {
    content: "📁";
    margin-right: 10px;
}

/* toggles to open folder on label when checked */
input[type="checkbox"]:checked ~ label:before {
  content: "📂";
  margin-right: 10px;
}

</style>

https://spencer07.github.io/ships/
**Recommended To Use Google Chrome For Best Use Of This Website**
<!DOCTYPE html>
<html>
<head>
<title>Coronavirus!</title>
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  <style>
    #header{
      backgound-color:orange;float:top;width: 100%;height: 50px;
    }
    #sidebar{
      background-color:lightskyblue;float:top;width: 100%;height: 1100px;
    }
    #content{
      background-color:yellow;float:middle;width: 100%;height :900px;
    }
    #footer{
      background-color:pink;float:bottom;width: 100%;height :1500px;
    }
    #survey{
      background-color:greenyellow;float:bottom;width: 100%;height :1300px;
    }
    #actual_survey{
      background-color:orange;float:bottom;width: 100%;height :500px;
    }
    table, th, td {
      border: 1px solid black;
    }
    button{
      background:black;
      color:white;
    }
  </style>
</head>
<body>
<script>
function myFunction(id) {
  var x = document.getElementById(id);
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}
</script>
<div id="header">
  <h1>Hello! This is a webside about Coronavirus. </h1>
</div>
<div id="sidebar">
  <p>On the website, You will see information about coronavirus. </p>
</div>

<div id="content">
  <table>
    <tr>
      <th>State</th>
      <th>How many people with the COVID-19(Coronavirus)</th>
      <th>How many people died</th>
      <th>City with the most people with the COVID-19</th>
      <th>How many people sick in that city</th>
      <th>How many people died in that city</th>
    </tr>
    <tr>
      <td>Washington</td>
      <td>167</td>
      <td>23</td>
      <td>King</td>
      <td>116</td>
      <td>21</td>
    </tr>
    <tr>
      <td>New York</td>
      <td>173</td>
      <td>0</td>
      <td>Westchester</td>
      <td>98</td>
      <td>0</td>
    </tr>
    <tr>
      <td>California</td>
      <td>144</td>
      <td>2</td>
      <td>Santa Clara</td>
      <td>43</td>
      <td>1</td>
    </tr>
    <tr>
      <td>California</td>
      <td>144</td>
      <td>2</td>
      <td>Santa Clara</td>
      <td>43</td>
      <td>1</td>
    </tr>
  </table>
</div>
</html>

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Calculator")

st.title("🧮 Animated Calculator")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
body{
    background:linear-gradient(135deg,#667eea,#764ba2);
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    font-family:Arial;
}

.calculator{
    background:#1e1e2f;
    padding:25px;
    border-radius:15px;
    box-shadow:0 10px 25px rgba(0,0,0,0.4);
}

#display{
    width:240px;
    height:50px;
    font-size:24px;
    text-align:right;
    border:none;
    border-radius:8px;
    padding:10px;
    margin-bottom:15px;
}

button{
    width:55px;
    height:55px;
    font-size:18px;
    margin:5px;
    border:none;
    border-radius:10px;
    cursor:pointer;
}

.operator{ background:#ff9f43; color:white; }
.number{ background:#576574; color:white; }
.equal{ background:#1dd1a1; color:white; }
.clear{ background:#ee5253; color:white; }
</style>
</head>

<body>

<div class="calculator">
<input id="display" readonly>

<br>

<button class="clear" onclick="clearScreen()">C</button>
<button class="operator" onclick="append('/')">÷</button>
<button class="operator" onclick="append('*')">×</button>
<button class="operator" onclick="append('-')">−</button>

<br>

<button class="number" onclick="append('7')">7</button>
<button class="number" onclick="append('8')">8</button>
<button class="number" onclick="append('9')">9</button>
<button class="operator" onclick="append('+')">+</button>

<br>

<button class="number" onclick="append('4')">4</button>
<button class="number" onclick="append('5')">5</button>
<button class="number" onclick="append('6')">6</button>
<button class="equal" onclick="calculate()">=</button>

<br>

<button class="number" onclick="append('1')">1</button>
<button class="number" onclick="append('2')">2</button>
<button class="number" onclick="append('3')">3</button>
<button class="number" onclick="append('0')">0</button>

</div>

<script>
function append(value){
 document.getElementById("display").value += value;
}

function clearScreen(){
 document.getElementById("display").value="";
}

function calculate(){
 try{
  document.getElementById("display").value = eval(document.getElementById("display").value);
 }catch{
  document.getElementById("display").value="Error";
 }
}
</script>

</body>
</html>
"""

components.html(html_code, height=500)
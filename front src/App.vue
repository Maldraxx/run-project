<template>
  <header>
    <link rel="icon" href="./assets/mini.ico" />
    <div class="position">
      <h1 class="header_title"><img src="./assets/minilogo.png" /></h1>
      <div class="header-buttons">
        <button type="button">로그인</button>
      </div>
      <div class="svg-wrapper">
        <svg height="40" width="150" xmlns="http://www.w3.org/2000/svg">
          <rect id="shape" height="40" width="150" />
          <div id="text">
            <a href="">
              <span class="spot"></span>
              문제
            </a>
          </div>
        </svg>
      </div>
      <!--Next button -->
      <div class="svg-wrapper">
        <svg height="40" width="150" xmlns="http://www.w3.org/2000/svg">
          <rect id="shape" height="40" width="150" />
          <div id="text">
            <a href="">
              <span class="spot"></span>
              해답
            </a>
          </div>
        </svg>
      </div>
      <!--Next button -->
      <div class="svg-wrapper">
        <svg height="40" width="150" xmlns="http://www.w3.org/2000/svg">
          <rect id="shape" height="40" width="150" />
          <div id="text">
            <a href="">
              <span class="spot"></span>
              문제 등록
            </a>
          </div>
        </svg>
      </div>
      <!--Next button -->
      <div class="svg-wrapper">
        <svg height="40" width="150" xmlns="http://www.w3.org/2000/svg">
          <rect id="shape" height="40" width="150" />
          <div id="text">
            <a href="">
              <span class="spot"></span>
              커뮤니티
            </a>
          </div>
        </svg>
      </div>
      <!--Next button -->
      <div class="svg-wrapper">
        <svg height="40" width="150" xmlns="http://www.w3.org/2000/svg">
          <rect id="shape" height="40" width="150" />
          <div id="text">
            <a href="">
              <span class="spot"></span>
              내 정보
            </a>
          </div>
        </svg>
      </div>
      <!--End button -->
    </div>
  </header>

  <div class="text-center">
    <img src="./assets/MainLogo.png" alt="main image" />
  </div>

  <footer>
    <p>&copy; DevOps Team project</p>
  </footer>
  <div>
    <p>{{ price1 }}이이이</p>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      price1: 60,
    };
  },
  components: {},
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
/* 전체 스타일 */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f2f2f2; /* 전체 배경색 */
  font-family: nanumgothic;
}
.container {
  width: 90%;
  margin: 0 auto;
}
header {
  background-color: #f2f2f2; /* 헤더 배경색 */
  color: #004aad; /* 헤더 텍스트 색상 */
  padding: 20px 0;
  margin-left: 5%;
  /* text-align: center; */
}
header h1 {
  margin: 0;
  font-size: 20px;
}
nav {
  background-color: #004aad; /* 내비게이션 배경색 */
  padding: 10px 0;
}
nav ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  text-align: center;
}
nav ul li {
  display: inline;
  margin-right: 20px;
}
nav ul li a {
  color: #fff;
  text-decoration: none;
  font-size: 18px;
}
section.problem-list {
  padding: 20px 0;
}
section.problem-list h2 {
  margin: 0;
  font-size: 24px;
  color: #333;
}
footer {
  background-color: #393939; /* 푸터 배경색 */
  color: #d9d9d9; /* 푸터 텍스트 색상 */
  text-align: center;
  padding: 10px 0;
  position: fixed;
  bottom: 0;
  width: 100%;
}

/* 로그인 버튼*/
.header-buttons {
  float: right;
  margin-right: 5%;
}
.header_title {
  float: left;
}
.header-buttons button {
  margin-left: 10px;
  padding: 8px 16px;
  background-color: #003a9a; /* 버튼 배경색 */
  color: #f2f2f2; /* 버튼 텍스트 색상 */
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.header-buttons button:hover {
  background-color: #004aad; /* 버튼 호버 시 배경색 */
}
/* 센터 이미지 */
.text-center {
  margin-top: 5%;
  text-align: center;
}

/* 새 버튼*/
.position {
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  margin-top: 0;
}
.svg-wrapper {
  margin-top: 0;
  position: relative;
  width: 150px;
  /*make sure to use same height/width as in the html*/
  height: 40px;
  display: inline-block;
  border-radius: 3px;
  margin-left: 5px;
  margin-right: 5px;
}
/*
    This is where we define the fill, color, thickness,
    and stroke pattern of the SVG when there is no hover.
    The dasharray and offset together define the line position
    under the words. Here's also where the transition speed is set.
    */

#shape {
  stroke-width: 6px;
  fill: transparent;
  stroke: #009ffd;
  stroke-dasharray: 85 400;
  stroke-dashoffset: -220;
  transition: 1s all ease;
}
/* 
        Pushing the text up into the SVG. Without this the
        text would be below the div's.
    */

#text {
  margin-top: -35px;
  text-align: center;
}

#text a {
  color: #004aad;
  text-decoration: none;
  font-weight: 100;
  font-size: 1.1em;
}
/* 
        Changing the shape on hover. I change the color of the stroke,
    make it thinner, then set it to again wrap around the entire parent element.
    */

.svg-wrapper:hover #shape {
  stroke-dasharray: 50 0;
  stroke-width: 3px;
  stroke-dashoffset: 0;
  stroke: #06d6a0;
}
</style>

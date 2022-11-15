<template>
  <div class="SearchFlexDiv">
    <div class="LeftDiv">
      <div>
        <input class="searchInput" type="text" ref="cursor" />
      </div>
      <div class="searchSelectDiv">
        <div class="searchSelect">All</div>
        <div class="searchSelect">드라마</div>
        <div class="searchSelect">코미디</div>
        <div class="searchSelect">액션</div>
        <div class="searchSelect">스릴러</div>
        <div class="searchSelect">모험</div>
        <div class="searchSelect">애니메이션</div>

      </div>
    </div>
    <div class="RightDiv">
      <!-- for 문으로 detailDiv 여러개 돌릴꺼 -->
      <div class="detailDiv">
        <div class="detailImgDiv">
          <img src="../../assets/starisborn.jpg" class="detailImg" />
        </div>
        
        <div>
          <div class="detailTitle">title</div>
          <div>
            Greed and class discrimination threaten the newly formed symbiotic
            relationship between the wealthy Park family and the destitute Kim
            clan.
          </div>
        </div>
      </div>
      <div class="detailDiv">
        <div class="detailImgDiv">
          <img src="../../assets/starisborn.jpg" class="detailImg" />
        </div>
        <div>
          <div class="detailTitle">title</div>
          <div>
            Greed and class discrimination threaten the newly formed symbiotic
            relationship between the wealthy Park family and the destitute Kim
            clan.
          </div>
        </div>
      </div>

      <div class="detailDiv">
        <div class="detailImgDiv">
          <img src="../../assets/starisborn.jpg" class="detailImg" />
        </div>
        
        <div>
          <div class="detailTitle">title</div>
          <div>
            Greed and class discrimination threaten the newly formed symbiotic
            relationship between the wealthy Park family and the destitute Kim
            clan.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
  <script>
export default {
  name: "SearchPage",
};
</script>
  
  <style>
.SearchFlexDiv {
  display: flex;
  margin-left: 3rem;
  color: white;
}
.LeftDiv {
  width: 30%;
  margin-top: 3rem;
  padding: 30px;
}
.searchInput{
  width: 300px;
  padding: 0;
  border: none;
  color: white;
  font-size: 1.5rem;
  border-bottom: 2px solid white;
  background-color: black;
  box-shadow: none;
}
.searchSelectDiv{
  width: 270px;
  margin-top: 3rem;
}
.searchSelect{
  margin: 1rem;
  padding: 0.3rem 1rem;
}
.searchSelect:hover{
  border:1px solid #ffda4f;
  border-radius: 5px;
}
.searchSelect:focus{
  border:1px solid #ffda4f;
}

.searchInput:focus{
  border: none;
  box-shadow: none;
  border-bottom: 3px solid white;
  outline: none;

}

.RightDiv {
  margin-top: 3rem;
  margin-right: 3rem;
}
.detailDiv {
  display: flex;
  margin: 40px 0 ;
}
.detailImg {
  width: 150px;
  height: 150px;
  object-fit: cover;
  border-radius: 15%;
  margin: 0 20px;
}
.detailImgDiv{
  padding: 0;
  margin: 0;
  width: 200px;
}
.detailTitle {
  font-size: 1.3rem;
  font-weight: bold;
  margin-bottom: 10px;
}

</style>
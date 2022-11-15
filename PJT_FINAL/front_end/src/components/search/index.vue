<template>
  <div class="SearchFlexDiv">
    <div class="LeftDiv">
      <div>
        <input type="text" />
      </div>
      <div>selectBox</div>
    </div>
    <div class="RightDiv">
      <!-- for 문으로 detailDiv 여러개 돌릴꺼 -->
      <div class="detailDiv">
        <div class="bg-crop">
          <img class="bg-img" src="../../assets/starisborn.jpg" />
        </div>
        <!-- <img src="../../assets/starisborn.jpg" class="detailImg"> -->
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
        <img src="../../assets/starisborn.jpg" class="detailImg" />
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
  color: white;
}
.LeftDiv {
  border: 1px solid red;
  padding: 30px;
}
.RightDiv {
  border: 1px solid blue;
}
.detailDiv {
  display: flex;
  margin: 20px 0 20px 20px;
  
}
.detailImg {
  width: 200px;
  height: 200px;
  object-fit: cover;
  border-radius: 15%;
  margin: 0 20px;
  border: 1px solid red;

  /* height: 120px;
    border-radius: 10px;
    margin-right: 20px; */
}
.detailTitle {
  font-size: 1.3rem;
  font-weight: bold;
  margin-bottom: 10px;
}
.bg-crop {
    position: relative;
    width: 120px; 
    height: 120px;
    overflow: hidden;
    border-radius: 15%;
    margin: 0 20px;
  }
.bg-img {
  position: absolute; 
  top: 0; 		 
  left: 0;
  width: 120px; 
  height: 120px;
  /* object-fit: cover; */
  /* margin: auto; */
}

</style>
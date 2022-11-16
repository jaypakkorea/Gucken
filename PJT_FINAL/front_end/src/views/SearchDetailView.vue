<template>
    <div class="SearchContainer">
        <DetailVue/>
    </div>

</template>

<script>
import DetailVue from '@/components/search/SearchDetail.vue';
export default {
    name:'SearchDetailView',
    components:{
        DetailVue,
    }
}
</script>

<style>
.SearchContainer{
    margin-left: 50px;
    font-family: Staatliches;
}

</style>
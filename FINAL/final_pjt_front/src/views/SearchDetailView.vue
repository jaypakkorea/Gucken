<template>
    <div class="SearchContainer">
        <DetailVue :movie="movie"/>
    </div>
</template>

<script>
import DetailVue from '@/components/search/SearchDetail.vue';
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name:'SearchDetailView',
    data() {
        return {
        movie: null,
        }
    },
    components:{
        DetailVue,
    },
    created() {
        this.getMovieDetail()
    },
    methods: {
        getMovieDetail() {
        axios({
            method: 'get',
            url: `${API_URL}/movies/${this.$route.params.moviePk}`
        })
        .then((res) => {
        this.movie = res.data
        })
        .catch((err) => {
        console.log(err)
    })
    }
    },
    watch: {
        movie: {
        deep : true,

      }
    }
}
</script>

<style>
.SearchContainer{
    font-family: Staatliches;
}

</style>
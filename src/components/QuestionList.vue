<template>
	<div class="container-card">
		<question v-for="question in questions" v-bind:key="question.pk" v-bind:question="question"></question>
	</div>
</template>

<script>
	const axios = require('axios');
	import Question from './Question'
	export default {
		name: 'QuestionList',
		components: {
			'question': Question,
		},
		mounted(){
			axios({
				method: 'GET',
				url: '/questions/'
			})
			.then((response) => {
				console.log(response);
				this.questions = response.data;
			})
			.catch((response) => {
				console.log(response);
			})
		},
		data () {
			return {
				questions: []
			}
		}
	}
</script>

<style>
</style>
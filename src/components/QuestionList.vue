<template>
	<div class="container">
		<question></question>
		<question></question>
		<question></question>
		<question></question>
		<question></question>
		<question></question>
	</div>
</template>

<script>
	import Question from './Question'
	export default {
		name: 'QuestionList',
		components: {
			'question': Question,
		},
		data () {
			return {

			}
		}
	}
</script>

<style>
</style>
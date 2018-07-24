<template>
	<div class="card container-card" >
			<div class="card-header header-red">
				<h3> {{ question.fields.question }} </h3>
			</div>
			<div class="card-body background-red">
				<p> {{ question.fields.description }} </p>
			</div>
	</div>
</template>

<script>
	export default {
		props: {
			question: {
				type: Object,
				required: true,
			}
		},
		name: 'Question',
		data () {
			return {
			}
		}
	}
</script>

<style src="../stylesheets/style.css">

</style>
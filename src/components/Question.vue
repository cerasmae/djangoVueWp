<template>
	<div class="card container-card">
		<!-- <div class="container"> -->
			<div class="card-header">
				<h3> {{ cardTitle }} </h3>
				<h5> {{ cardSubtitle }} </h5>
			</div>
			<div class="card-body">
				<p> {{ cardDescription }} </p>
			</div>
			
		<!-- </div> -->
	</div>
</template>

<script>
	export default {
		name: 'Question',
		data () {
			return {
				cardTitle: "All Too Well",
				cardSubtitle: "Taylor Swift",
				cardDescription: "HEY YOU CALLED ME UP AGAIN JUST TO BREAK ME LIKE A PROMISE SO CASUALLY CRUEL IN THE NAME OF BEING HONEST",
			}
		}
	}
</script>

<style src="../stylesheets/style.css">

</style>
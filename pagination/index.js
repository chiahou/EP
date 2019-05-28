Vue.component('pagination-template',{
	props: 'pagination',
	template: '<p>{{pagination.firstid}} to {{pagination.lastid}} of {{row.length}}</p>'

})

new Vue({
	el: "#app",
	data:{
		firstid: 1,
		lastid: 10,
	}
})
document.querySelectorAll('[name=type]').forEach(s => {
	s.addEventListener('change', function() {
		document.querySelectorAll('.someClass').forEach(d => d.classList.add('deactive'));
		document.getElementById(this.value).classList.remove('deactive');
	});
});
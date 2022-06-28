
$(document).ready(function(){

	var dropZone = $('#upload-container');

	$('#file-input').focus(function() {
		$('label').addClass('focus');
	})
	.focusout(function() {
		$('label').removeClass('focus');
	});


	dropZone.on('drag dragstart dragend dragover dragenter dragleave drop', function(){
		return false;
	});

	dropZone.on('dragover dragenter', function() {
		dropZone.addClass('dragover');
	});

	dropZone.on('dragleave', function(e) {
		let dx = e.pageX - dropZone.offset().left;
		let dy = e.pageY - dropZone.offset().top;
		if ((dx < 0) || (dx > dropZone.width()) || (dy < 0) || (dy > dropZone.height())) {
			dropZone.removeClass('dragover');
		}
	});

	dropZone.on('drop', function(e) {
		dropZone.removeClass('dragover');
		let files = e.originalEvent.dataTransfer.files;
		console.log('hello');
		$("#load_label").text(path.dirname(files[0]));
		console.log(path.dirname(files[0]));
	});

	$('#file-input').change(function() {
		let files = this.files;
		console.log('hello');
		$("#load_label").text(path.dirname(files[0]));
		console.log(path.dirname(files[0]));
	});


//	function sendFiles(files) {
//		let maxFileSize = 5242880;
//		let Data = new FormData();
//		$(files).each(function(index, file) {
//			if ((file.size <= maxFileSize) && ((file.type == 'image/png') || (file.type == 'image/jpeg'))) {
//				Data.append('images[]', file);
//			};
//		});
//
//		$.ajax({
//			url: dropZone.attr('action'),
//			type: dropZone.attr('method'),
//			data: Data,
//			contentType: false,
//			processData: false,
//			success: function(data) {
//				alert ('Файлы были успешно загружены!');
//			}
//		});
//	}
//})


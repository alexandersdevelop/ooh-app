function exportToCsv() {
		var processRow = function (row) {
			var finalVal = '';
			for (var j = 0; j < row.length; j++) {
				var innerValue = row[j] === null ? '' : row[j].toString();
				if (row[j] instanceof Date) {
					innerValue = row[j].toLocaleString();
				};
				var result = innerValue.replace(/"/g, '""');
				if (result.search(/("|,|\n)/g) >= 0)
					result = '"' + result + '"';
				if (j > 0)
					finalVal += ',';
				finalVal += result;
			}
			return finalVal + '\n';
		};

		var csvFile = '';

		var downloadarray = param;
		for (var k = 0; k < downloadarray.length; k++) {
			downloadarray[k].splice(1, 11);
		}
			
		for (var i = 0; i < downloadarray.length; i++) {
			csvFile += processRow(downloadarray[i]);
		}
		
		Data = new Date();
		Year = Data.getFullYear();
		Month = Data.getMonth();
		Day = Data.getDate();
		Hour = Data.getHours();
		Minutes = Data.getMinutes();
		
		var blob = new Blob([csvFile], { type: 'text/csv;charset=utf-8;' });
		if (navigator.msSaveBlob) { // IE 10+
			navigator.msSaveBlob(blob, campaign + "_" + Year + "-" + Month + "-" + Day + "_" + Hour + "-" + Minutes + ".csv");
		} else {
			var link = document.createElement("a");
			if (link.download !== undefined) { // feature detection
				// Browsers that support HTML5 download attribute
				var url = URL.createObjectURL(blob);
				link.setAttribute("href", url);
				link.setAttribute("download", campaign + "_" + Year + "-" + Month + "-" + Day + "_" + Hour + "-" + Minutes + ".csv");
				link.style.visibility = 'hidden';
				document.body.appendChild(link);
				link.click();
				document.body.removeChild(link);
			};
		};
	}